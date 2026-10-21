"""Experiments 2 (rollouts) and 3 (ACI-Bench) using the frozen measurement code unchanged."""
import sys, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
PROJECT = Path("persona_study")
sys.path.insert(0, str(PROJECT / "src"))
import numpy as np, pandas as pd
import run_measurement as rm
from prompting import load_prompt_file

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "results"
OUT.mkdir(exist_ok=True)
plan = rm.load_plan(rm.PLAN_PATH)
seed = int(plan["seed"])
config = rm.load_config(PROJECT / "config.yaml")
persona_texts = [t for t in load_prompt_file(PROJECT / str(config["prompt_file"]))["personas"].values() if isinstance(t, str)]
MODELS = sys.argv[2].split(",") if len(sys.argv) > 2 else ["gemini", "claude", "gpt"]
ROLL_MODELS = sys.argv[3].split(",") if len(sys.argv) > 3 else MODELS
FLAGS = ["flag_empty", "flag_truncated", "flag_patient_turn", "flag_multiple_doctor_turns", "flag_refusal_or_ai_meta"]
B = int(plan["bootstrap_resamples"])


def cluster_ci(values, groups):
    values = np.asarray(values, float); groups = np.asarray(groups).astype(str)
    uniq = np.unique(groups); idx = {g: np.flatnonzero(groups == g) for g in uniq}
    rng = np.random.default_rng(seed); s = np.empty(B)
    for b in range(B):
        s[b] = values[np.concatenate([idx[g] for g in rng.choice(uniq, len(uniq))])].mean()
    return float(values.mean()), *rm.percentile_ci(s)


# ---------------- Experiment 3: ACI-Bench ----------------
aci_ctx = pd.read_csv(PROJECT / "data/aci_bench/aci_contexts.csv")
aci_ctx["dlg"] = aci_ctx["dataset"] + "_" + aci_ctx["dialogue_id"]
acc_rows, rec_rows, pred_rows, h2_rows, real_rows, dist_rows, xfer_rows = [], [], [], [], [], [], []
for m in MODELS:
    out = pd.read_csv(PROJECT / f"outputs/aci_{m}_cleaned.csv")
    out = out.merge(aci_ctx[["context_id", "dlg"]], on="context_id")
    out["dialogue_id"] = out["dlg"]
    feats, echo = rm.build_features(m, out, aci_ctx[["context_id", "context_word_count"]], persona_texts, plan, "na")
    feats = rm.usable_rows(feats)
    feats.to_csv(OUT / f"aci_features_{m}.csv", index=False)
    text = out.merge(feats[["context_id", "condition"]], on=["context_id", "condition"]); text["model"] = m
    preds = pd.concat([rm.fit_variant(text, v, echo, plan, seed) for v in ["B1", "B2"]])
    acc, rec, _ = rm.metric_tables(preds, plan, seed)
    pt, h2 = rm.prediction_table(feats, plan, seed)
    real = rm.realised_table(rec, pt)
    for t in (acc, rec, pt, h2, real):
        t.insert(0, "model", m)
    acc_rows.append(acc); rec_rows.append(rec); pred_rows.append(pt); h2_rows.append(h2); real_rows.append(real)
    d = feats.groupby(["condition"])[["persona_distance", "n_words"]].mean().reset_index(); d.insert(0, "model", m); dist_rows.append(d)
    # Cross-corpus transfer: train on OSCE outputs of the same model, test on ACI.
    osce = pd.read_csv(PROJECT / f"outputs/main_{m}_cleaned.csv")
    osce = osce[osce["analysis_text"].fillna("").str.strip() != ""]
    vec = rm.vectorizer(plan); clf = rm.classifier(seed, plan)
    clf.fit(vec.fit_transform(osce["analysis_text"].astype(str)), osce["condition"])
    yhat = clf.predict(vec.transform(text["analysis_text"].astype(str)))
    corr = (yhat == text["condition"].to_numpy()).astype(float)
    for scope in ["overall", *rm.POSITIONS]:
        mask = np.ones(len(text), bool) if scope == "overall" else (text["position"] == scope).to_numpy()
        e, lo, hi = cluster_ci(corr[mask], text["dialogue_id"].to_numpy()[mask])
        xfer_rows.append({"model": m, "scope": scope, "accuracy": e, "ci_low": lo, "ci_high": hi})
    for c in rm.CONDITIONS:
        mask = (text["condition"] == c).to_numpy()
        e, lo, hi = cluster_ci(corr[mask], text["dialogue_id"].to_numpy()[mask])
        xfer_rows.append({"model": m, "scope": f"recall_{c}", "accuracy": e, "ci_low": lo, "ci_high": hi})
    print("aci done", m, flush=True)
for name, rows in [("aci_accuracy", acc_rows), ("aci_recall", rec_rows), ("aci_predictions", pred_rows), ("aci_h2", h2_rows),
                   ("aci_realised", real_rows), ("aci_descriptive", dist_rows)]:
    pd.concat(rows).to_csv(OUT / f"{name}.csv", index=False)
pd.DataFrame(xfer_rows).to_csv(OUT / "aci_transfer.csv", index=False)

# ---------------- Experiment 2: rollouts ----------------
MARKERS = ["psychosocial_per_100", "med_per_100", "share_open", "instruction_per_100", "has_question",
           "plan_statement_present", "invitation_per_100", "n_words"]
roll_rec, roll_mark, roll_close = [], [], []
for m in ROLL_MODELS:
    r = pd.read_csv(PROJECT / f"outputs/rollouts/{m}_cleaned.csv")
    doc = r[r["role"] == "doctor"].copy()
    doc["base_context"] = doc["context_id"]
    doc["context_id"] = doc["base_context"] + "_t" + doc["turn"].astype(str)
    for f in FLAGS:
        doc[f] = 0
    frozen = doc[["context_id"]].drop_duplicates().assign(context_word_count=0)
    feats, echo = rm.build_features(m, doc, frozen, persona_texts, plan, "na")
    feats = feats.merge(doc[["context_id", "condition", "turn", "base_context", "closing_detected"]], on=["context_id", "condition"])
    feats.to_csv(OUT / f"roll_features_{m}.csv", index=False)
    # Classifier trained on Experiment 1 outputs of the same model, excluding the rollout dialogues.
    osce = pd.read_csv(PROJECT / f"outputs/main_{m}_cleaned.csv")
    osce = osce[(osce["analysis_text"].fillna("").str.strip() != "") & (~osce["dialogue_id"].isin(doc["dialogue_id"].unique()))]
    vec = rm.vectorizer(plan); clf = rm.classifier(seed, plan)
    clf.fit(vec.fit_transform(osce["analysis_text"].astype(str)), osce["condition"])
    doc = doc[doc["analysis_text"].fillna("").str.strip() != ""]
    doc["y_pred"] = clf.predict(vec.transform(doc["analysis_text"].astype(str)))
    doc["correct"] = (doc["y_pred"] == doc["condition"]).astype(float)
    for turn in range(1, 5):
        block = doc[doc["turn"] == turn]
        e, lo, hi = cluster_ci(block["correct"], block["dialogue_id"])
        roll_rec.append({"model": m, "turn": turn, "condition": "all", "recall": e, "ci_low": lo, "ci_high": hi, "n": len(block)})
        for c in rm.CONDITIONS:
            b2 = block[block["condition"] == c]
            e, lo, hi = cluster_ci(b2["correct"], b2["dialogue_id"])
            roll_rec.append({"model": m, "turn": turn, "condition": c, "recall": e, "ci_low": lo, "ci_high": hi, "n": len(b2)})
        fb = feats[feats["turn"] == turn]
        close = fb.groupby("condition")["closing_detected"].mean()
        for c, v in close.items():
            roll_close.append({"model": m, "turn": turn, "condition": c, "closing_rate": float(v)})
        for marker in MARKERS:
            wide = fb.pivot(index="base_context", columns="condition", values=marker)
            dl = fb.groupby("base_context")["dialogue_id"].first()
            for c in ["P1", "P2", "P3", "P4", "P5"]:
                diff = (wide[c] - wide["P0"]).dropna()
                if len(diff) == 0:
                    continue
                e, lo, hi = cluster_ci(diff.to_numpy(), dl.loc[diff.index].to_numpy())
                roll_mark.append({"model": m, "turn": turn, "contrast": f"{c} - P0", "marker": marker,
                                  "estimate": e, "ci_low": lo, "ci_high": hi, "n": len(diff)})
            for c in rm.CONDITIONS:
                roll_mark.append({"model": m, "turn": turn, "contrast": f"mean {c}", "marker": marker,
                                  "estimate": float(wide[c].mean()), "ci_low": np.nan, "ci_high": np.nan, "n": int(wide[c].notna().sum())})
    print("rollouts done", m, flush=True)
pd.DataFrame(roll_rec).to_csv(OUT / "roll_recall.csv", index=False)
pd.DataFrame(roll_mark).to_csv(OUT / "roll_markers.csv", index=False)
pd.DataFrame(roll_close).to_csv(OUT / "roll_closing.csv", index=False)
print("ALL DONE")
