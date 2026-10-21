"""Exploratory secondary verdict: separate "not expressed" from "not measurable".

Specified on 2026-10-19, after all results were known. Reanalysis of existing result files only:
no model is called, no existing file is modified, and the strict verdicts are read unchanged from
c_predictions.csv (OSCE) and aci_predictions.csv (ACI-Bench). Writes only to this folder.

A prediction is untestable if
  (a) its marker's agreement with the human counts is below a threshold (reliability), or
  (b) the largest effect possible in the predicted direction (headroom) is below the minimum
      detectable effect (MDE) of the cluster bootstrap.
Headroom: for a decrease, the mean of the reference condition (markers cannot go below 0); for an
increase on a bounded marker (share or presence, at most 1), 1 minus the reference mean; for an
increase on an unbounded rate, unlimited. MDE = (1.96 + 0.84) x bootstrap SE, i.e. 80% power at
alpha 0.05, with SE = (CI high - CI low) / 3.92 from the existing 2,000-resample percentile interval.
An opposite verdict always stands, whether or not the prediction is testable.

Secondary realization rule (pre-specified predictions against P0, as in the strict rule): recall
above chance, no opposite verdict, no testable prediction not confirmed, and at least two testable
predictions confirmed.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
PAPER = Path("paper_analysis")
MODELS = ["gemini", "claude", "gpt", "llama3instruct", "biomedllama", "medgemma"]
ACI_DIRS = {"gemini": "exp23_results", "claude": "exp23_results", "gpt": "exp23_results_gpt4o",
            "llama3instruct": "exp23_results_llama3q4", "biomedllama": "exp23_results_biomed",
            "medgemma": "exp23_results_med"}

# Agreement of each marker with the human counts (Table A5). Medical terms use the Spearman
# correlation: persona effects are paired within-context differences, which depend on ranking.
# The open share and question presence use the lower ICC of open and closed questions.
RELIABILITY = {"psychosocial_per_100": 0.95, "med_per_100": 0.80, "share_open": 0.77,
               "has_question": 0.77, "n_leading": 0.40, "instruction_per_100": 0.61,
               "plan_statement_present": 0.72, "invitation_per_100": 0.63}
BOUNDED = {"share_open", "has_question", "plan_statement_present"}
THRESHOLD = 0.50
SWEEP = [0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
Z_MDE = 1.96 + 0.84


def headroom(marker: str, direction: str, reference_mean: float) -> float:
    if direction == "lower":
        return reference_mean
    return 1.0 - reference_mean if marker in BOUNDED else np.inf


def annotate(pred: pd.DataFrame, feats: pd.DataFrame) -> pd.DataFrame:
    out = pred.copy()
    out["reference_mean"] = [feats.loc[feats.condition == r, m].mean() for r, m in zip(out.right, out.marker)]
    out["headroom"] = [headroom(m, d, x) for m, d, x in zip(out.marker, out.direction, out.reference_mean)]
    out["mde"] = Z_MDE * (out.ci_high - out.ci_low) / 3.92
    out["reliability"] = out.marker.map(RELIABILITY)
    out["powered"] = out.headroom >= out.mde
    return out


def secondary(frame: pd.DataFrame, threshold: float) -> pd.Series:
    testable = (frame.reliability >= threshold) & frame.powered
    return np.where(frame.verdict == "opposite", "opposite",
                    np.where(~testable, "untestable", frame.verdict))


def realised(frame: pd.DataFrame, recall: dict, col: str) -> dict:
    res = {}
    for persona in ["P1", "P3", "P4", "P5"]:
        f = frame[(frame.left == persona) & (frame.right == "P0") & (frame.in_realised_rule == 1)]
        ok = (recall[persona] > 1 / 6 and not (f[col] == "opposite").any()
              and not (f[col] == "not confirmed").any() and (f[col] == "confirmed").sum() >= 2)
        res[persona] = ok
    return res


def aci_features(model: str) -> Path:
    """ACI-Bench features were not saved for Gemini and Claude; rebuild them exactly as analysis_exp2_exp3.py does."""
    out_path = HERE / f"aci_features_{model}.csv"
    if out_path.exists():
        return out_path
    import sys, warnings
    warnings.filterwarnings("ignore")
    sys.path.insert(0, str(PROJECT / "src"))
    import run_measurement as rm
    from prompting import load_prompt_file
    plan = rm.load_plan(rm.PLAN_PATH)
    config = rm.load_config(PROJECT / "config.yaml")
    persona_texts = [t for t in load_prompt_file(PROJECT / str(config["prompt_file"]))["personas"].values() if isinstance(t, str)]
    ctx = pd.read_csv(PROJECT / "data/aci_bench/aci_contexts.csv")
    ctx["dlg"] = ctx["dataset"] + "_" + ctx["dialogue_id"]
    out = pd.read_csv(PROJECT / f"outputs/aci_{model}_cleaned.csv").merge(ctx[["context_id", "dlg"]], on="context_id")
    out["dialogue_id"] = out["dlg"]
    feats, _ = rm.build_features(model, out, ctx[["context_id", "context_word_count"]], persona_texts, plan, "na")
    rm.usable_rows(feats).to_csv(out_path, index=False)
    return out_path


def load(model: str, corpus: str):
    if corpus == "OSCE":
        pred = pd.read_csv(PROJECT / f"analysis/results/{model}/c_predictions.csv")
        feats = pd.read_csv(PROJECT / f"analysis/features_{model}.csv")
        rec = pd.read_csv(PROJECT / f"analysis/results/{model}/b_recall.csv")
    else:
        d = PAPER / ACI_DIRS[model]
        pred = pd.read_csv(d / "aci_predictions.csv")
        pred = pred[pred.model == model]
        path = d / f"aci_features_{model}.csv"
        feats = pd.read_csv(path if path.exists() else aci_features(model))
        rec = pd.read_csv(d / "aci_recall.csv")
        rec = rec[rec.model == model]
    feats = feats[feats["analysis_text"].notna()] if "analysis_text" in feats else feats
    pred = pred[(pred.scope == "overall") & (pred.specification == "pre-specified")]
    rec = rec[(rec.variant == "B1") & (rec.scope == "overall")]
    return pred, feats, dict(zip(rec.condition, rec.recall))


def main() -> None:
    rows, real_rows, sweep_rows = [], [], []
    for corpus in ["OSCE", "ACI-Bench"]:
        for m in MODELS:
            pred, feats, recall = load(m, corpus)
            a = annotate(pred, feats)
            a["secondary_verdict"] = secondary(a, THRESHOLD)
            a = a.drop(columns=["model"], errors="ignore"); a.insert(0, "corpus", corpus); a.insert(1, "model", m)
            rows.append(a)
            strict = realised(a.assign(v=a.verdict), recall, "v")
            sec = realised(a, recall, "secondary_verdict")
            for p in strict:
                real_rows.append({"corpus": corpus, "model": m, "persona": p,
                                  "realised_strict": int(strict[p]), "realised_secondary": int(sec[p])})
            for t in SWEEP:
                s = realised(a.assign(v=secondary(a, t)), recall, "v")
                sweep_rows += [{"corpus": corpus, "model": m, "threshold": t, "persona": p, "realised": int(s[p])} for p in s]
    keep = ["corpus", "model", "contrast", "marker", "direction", "in_realised_rule", "estimate", "ci_low", "ci_high",
            "verdict", "reference_mean", "headroom", "mde", "reliability", "powered", "secondary_verdict"]
    pd.concat(rows)[keep].to_csv(HERE / "testability_predictions.csv", index=False)
    real = pd.DataFrame(real_rows); real.to_csv(HERE / "testability_realised.csv", index=False)
    sweep = pd.DataFrame(sweep_rows); sweep.to_csv(HERE / "testability_sweep.csv", index=False)
    print(real.pivot_table(index=["corpus", "model"], columns="persona", values=["realised_strict", "realised_secondary"]).to_string())
    print(sweep.groupby(["corpus", "threshold", "persona"]).realised.sum().unstack().to_string())


if __name__ == "__main__":
    main()
