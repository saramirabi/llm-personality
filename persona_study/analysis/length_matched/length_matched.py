"""Post hoc length-matched robustness analysis for Experiment 1 (OSCE).

Specified on 2026-10-05, after the Experiment 1 results were known.
Reanalysis of existing outputs only: no model is called and no existing file is changed.

Versions of every output, applied to analysis_text (that is, after the patient-label rule):
  FULL  the unchanged analysis_text
  T25   the first 25 whitespace-separated words
  T1S   the first sentence, from measure_text.sentences (the splitter the marker code uses)

The measurement code in src/run_measurement.py is imported and run unchanged.
Writes only to analysis/length_matched/.
"""
from __future__ import annotations

import hashlib
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")
PROJECT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT / "src"))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import run_measurement as rm  # noqa: E402
from measure_text import sentences  # noqa: E402

OUT = Path(__file__).resolve().parent
MODELS = ["gemini", "claude", "gpt"]
VERSIONS = ["FULL", "T25", "T1S"]
T25_WORDS = 25


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def truncate(text: str, version: str) -> str:
    text = "" if pd.isna(text) else str(text)
    if version == "FULL":
        return text
    if version == "T25":
        return " ".join(text.split()[:T25_WORDS])
    if version == "T1S":
        parts = sentences(text)
        return parts[0] if parts else text
    raise ValueError(version)


def presence_columns(features: pd.DataFrame) -> pd.DataFrame:
    features = features.copy()
    features["psychosocial_present"] = ((features["emotion_present"] > 0) | (features["life_context_present"] > 0)).astype(int)
    features["leading_present"] = (features["n_leading"] > 0).astype(int)
    return features


# Lexicon presence markers for Table F. plan_statement_present is already a presence marker.
PRESENCE = {
    "psychosocial_per_100": "psychosocial_present",
    "instruction_per_100": "instruction_present",
    "invitation_per_100": "invitation_present",
    "n_leading": "leading_present",
    "plan_statement_present": "plan_statement_present",
}
PRESENCE_ALL = ["psychosocial_present", "emotion_present", "life_context_present", "empathy_phrases_present",
                "instruction_present", "plan_statement_present", "invitation_present", "hedge_present", "leading_present"]
CONTRASTS = [("P1", "P0"), ("P2", "P0"), ("P3", "P0"), ("P4", "P0"), ("P5", "P0"), ("P2", "P1"), ("P4", "P3")]


def main() -> None:
    plan = rm.load_plan(rm.PLAN_PATH)
    plan_sha = rm.sha256_file(rm.PLAN_PATH)
    seed = int(plan["seed"])
    np.random.seed(seed)
    config = rm.load_config(PROJECT / "config.yaml")
    frames, frozen, persona_texts = rm.load_inputs(config)
    frames = [(name, frame) for name, frame in frames if name in MODELS]
    assert [name for name, _ in frames] == MODELS, [name for name, _ in frames]

    log = [f"# Length-matched robustness analysis log", "",
           f"Run at {datetime.now(timezone.utc).isoformat()}", "",
           "Post hoc robustness analysis, specified on 2026-10-05 after the Experiment 1 results were known.",
           "No model API was called and no existing output or result file was modified.", "",
           "## Input file SHA-256", ""]
    for item in config["analysis_output_files"]:
        log.append(f"- `{item}`: `{sha(PROJECT / str(item))}`")
    log.append(f"- `{(PROJECT / str(config['frozen_dir']) / str(config['main_frozen_filename'])).relative_to(PROJECT)}`: "
               f"`{sha(PROJECT / str(config['frozen_dir']) / str(config['main_frozen_filename']))}`")
    log.append(f"- `analysis/analysis_plan_v1.yaml`: `{plan_sha}`")
    log.append(f"- `src/run_measurement.py`: `{sha(PROJECT / 'src' / 'run_measurement.py')}`")
    log.append(f"- `src/measure_text.py`: `{sha(PROJECT / 'src' / 'measure_text.py')}`")
    log.append(f"- `analysis/length_matched/length_matched.py`: `{sha(Path(__file__))}`")
    log.append("")
    for name, frame in frames:
        log.append(f"- {name}: {len(frame)} rows, {frame['context_id'].nunique()} contexts, "
                   f"conditions {frame.groupby('condition').size().to_dict()}")

    length_rows, pred_parts, real_parts, acc_parts, base_rows, presence_rows = [], [], [], [], [], []
    cross_acc_parts, cross_rec_parts, cross_conf_parts = [], [], []
    for version in VERSIONS:
        text_frames = []
        for name, frame in frames:
            print(f"{version} {name}", flush=True)
            out = frame.copy()
            full_words = out["analysis_text"].fillna("").astype(str).str.split().str.len()
            out["analysis_text"] = out["analysis_text"].map(lambda t: truncate(t, version))
            kept_words = out["analysis_text"].str.split().str.len()
            # Table A
            for cond, idx in out.groupby("condition").groups.items():
                full_c = full_words.loc[idx]
                kept_c = kept_words.loc[idx]
                if version == "T25":
                    shorter = float((full_c < T25_WORDS).mean())
                elif version == "T1S":
                    shorter = float((kept_c == full_c).mean())
                else:
                    shorter = np.nan
                length_rows.append({"version": version, "model": name, "condition": cond,
                                    "median_words_full": float(full_c.median()), "median_words_kept": float(kept_c.median()),
                                    "share_shorter_than_cutoff": shorter})
            features, echo = rm.build_features(name, out, frozen, persona_texts, plan, plan_sha)
            features = presence_columns(rm.usable_rows(features))
            features.to_csv(OUT / f"features_{version}_{name}.csv", index=False)
            text = out.merge(features[["context_id", "condition"]], on=["context_id", "condition"])
            text["model"] = name
            text_frames.append(text)
            # Table D (within model)
            preds = rm.fit_variant(text, "B1", echo, plan, seed)
            accuracy, recall, _ = rm.metric_tables(preds, plan, seed)
            for t in (accuracy,):
                t.insert(0, "model", name); t.insert(0, "version", version)
            acc_parts.append(accuracy)
            recall.insert(0, "model", name); recall.insert(0, "version", version)
            # Table B and C
            table, _h2 = rm.prediction_table(features, plan, seed)
            realised = rm.realised_table(recall, table)
            for t in (table, realised):
                t.insert(0, "model", name); t.insert(0, "version", version)
            pred_parts.append(table); real_parts.append(realised)
            # Table E
            base = features.loc[features["condition"] == "P0"]
            base_rows.append({"version": version, "model": name,
                              "baseline_psychosocial_per_100": float(base["psychosocial_per_100"].mean()),
                              "baseline_share_no_psychosocial_word": float((base["psychosocial_present"] == 0).mean())})
            # Table F
            for marker in PRESENCE_ALL:
                wide = rm.paired_frame(features, marker)
                for left, right in CONTRASTS:
                    diff = (wide[left] - wide[right]).dropna()
                    est, low, high, p = rm.bootstrap_mean(diff, wide["dialogue_id"], plan, seed)
                    direction = None
                    for item in plan["predictions"]:
                        if item["contrast"] == [left, right] and PRESENCE.get(item["marker"]) == marker:
                            direction = item["direction"]
                    presence_rows.append({"version": version, "model": name, "contrast": f"{left} - {right}",
                                          "marker": marker, "estimate": est, "ci_low": low, "ci_high": high,
                                          "predicted_direction": direction or "",
                                          "verdict": rm.verdict(low, high, direction) if direction else ""})
        # Table D (held-out model)
        c_acc, c_rec, c_conf = rm.cross_model_generalise(text_frames, plan, seed)
        for t in (c_acc, c_rec, c_conf):
            t.insert(0, "version", version)
        cross_acc_parts.append(c_acc); cross_rec_parts.append(c_rec); cross_conf_parts.append(c_conf)

    pd.DataFrame(length_rows).to_csv(OUT / "A_length.csv", index=False)
    preds = pd.concat(pred_parts, ignore_index=True)
    full = preds.loc[preds["version"] == "FULL", ["model", "scope", "contrast", "marker", "verdict"]].rename(columns={"verdict": "verdict_full"})
    preds = preds.merge(full, on=["model", "scope", "contrast", "marker"], how="left")
    preds["changed_from_full"] = (preds["verdict"] != preds["verdict_full"]).astype(int)
    preds.to_csv(OUT / "B_verdicts.csv", index=False)
    overall = preds.loc[preds["scope"] == "overall"]
    counts = overall.groupby(["version", "model"]).apply(lambda b: pd.Series({
        "confirmed_of_15_base": int(((b["verdict"] == "confirmed") & (b["in_realised_rule"] == 1)).sum()),
        "confirmed_of_2_extra_p5": int(((b["verdict"] == "confirmed") & (b["in_realised_rule"] == 0)).sum()),
        "opposite": int((b["verdict"] == "opposite").sum()),
        "changed_from_full": int(b["changed_from_full"].sum()),
    })).reset_index()
    counts.to_csv(OUT / "B_counts.csv", index=False)
    pd.concat(real_parts, ignore_index=True).to_csv(OUT / "C_realised.csv", index=False)
    pd.concat(acc_parts, ignore_index=True).to_csv(OUT / "D_accuracy_within.csv", index=False)
    pd.concat(cross_acc_parts, ignore_index=True).to_csv(OUT / "D_accuracy_heldout.csv", index=False)
    pd.concat(cross_rec_parts, ignore_index=True).to_csv(OUT / "D_recall_heldout.csv", index=False)
    conf = pd.concat(cross_conf_parts, ignore_index=True)
    conf.to_csv(OUT / "D_confusion_heldout.csv", index=False)
    pd.DataFrame(base_rows).to_csv(OUT / "E_baseline_psychosocial.csv", index=False)
    pd.DataFrame(presence_rows).to_csv(OUT / "F_presence.csv", index=False)
    (OUT / "log.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
