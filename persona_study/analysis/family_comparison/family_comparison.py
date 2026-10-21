"""Within-family comparison: Llama-3-8B-Instruct versus its bio-medical fine-tune.

Post hoc analysis, specified on 2026-10-08 after the results of both models were known.
Both models received byte-identical prompts (same tokenizer and chat template; identical input token
totals in the run reports), so every comparison is paired on the same context and condition.
Reanalysis of existing outputs and result files only. Writes only to this folder.
Rerun for Llama-3-8B-Instruct at Q4_K_S (2026-10-19): both models now share the quantization level.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
sys.path.insert(0, str(PROJECT / "src"))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import run_measurement as rm  # noqa: E402

A, B = "llama3instruct", "biomedllama"
PAPER = Path("paper_analysis")
plan = rm.load_plan(rm.PLAN_PATH)
seed = int(plan["seed"])
PREDICTIONS = [(tuple(p["contrast"]), p["marker"], p["direction"]) for p in plan["predictions"]]
BASELINE_MARKERS = ["n_words", "psychosocial_per_100", "med_per_100", "has_question", "share_open",
                    "plan_statement_present", "invitation_per_100", "instruction_per_100", "hedge_per_100"]


def boot(values: pd.Series, dialogues: pd.Series):
    est, low, high, p = rm.bootstrap_mean(values, dialogues, plan, seed)
    return est, low, high


def paired_delta(features: pd.DataFrame, marker: str, left: str, right: str) -> pd.Series:
    wide = features.pivot(index="context_id", columns="condition", values=marker)
    return (wide[left] - wide[right])


def compare_features(fa: pd.DataFrame, fb: pd.DataFrame, corpus: str) -> pd.DataFrame:
    dialogues = fa.groupby("context_id")["dialogue_id"].first()
    positions = fa.groupby("context_id")["position"].first()
    rows = []
    for (left, right), marker, direction in PREDICTIONS:
        da = paired_delta(fa, marker, left, right)
        db = paired_delta(fb, marker, left, right)
        both = pd.concat([da.rename("a"), db.rename("b")], axis=1).dropna()
        for scope in ["overall", "Early", "Middle", "Late"]:
            sub = both if scope == "overall" else both[positions.loc[both.index] == scope]
            ea, la, ha = boot(sub["a"], dialogues)
            eb, lb, hb = boot(sub["b"], dialogues)
            ed, ld, hd = boot(sub["a"] - sub["b"], dialogues)
            rows.append({"corpus": corpus, "scope": scope, "contrast": f"{left} - {right}", "marker": marker,
                         "direction": direction, "delta_instruct": ea, "ci_low_instruct": la, "ci_high_instruct": ha,
                         "verdict_instruct": rm.verdict(la, ha, direction),
                         "delta_biomed": eb, "ci_low_biomed": lb, "ci_high_biomed": hb,
                         "verdict_biomed": rm.verdict(lb, hb, direction),
                         "difference_instruct_minus_biomed": ed, "ci_low_diff": ld, "ci_high_diff": hd,
                         "difference_significant": int(ld > 0 or hd < 0), "n_pairs": len(sub)})
    return pd.DataFrame(rows)


def baseline_profile(fa: pd.DataFrame, fb: pd.DataFrame, corpus: str) -> pd.DataFrame:
    rows = []
    for cond in ["P0"]:
        a = fa[fa.condition == cond].set_index("context_id")
        b = fb[fb.condition == cond].set_index("context_id")
        dialogues = a["dialogue_id"]
        for marker in BASELINE_MARKERS:
            both = pd.concat([a[marker].rename("a"), b[marker].rename("b")], axis=1).dropna()
            ed, ld, hd = boot(both["a"] - both["b"], dialogues)
            rows.append({"corpus": corpus, "condition": cond, "marker": marker, "mean_instruct": both["a"].mean(),
                         "mean_biomed": both["b"].mean(), "difference": ed, "ci_low": ld, "ci_high": hd, "n_pairs": len(both)})
    return pd.DataFrame(rows)


def compare_accuracy() -> pd.DataFrame:
    rows = []
    oa = pd.read_csv(PROJECT / f"analysis/results/{A}/oof_predictions.csv")
    ob = pd.read_csv(PROJECT / f"analysis/results/{B}/oof_predictions.csv")
    for variant in ["B1", "B2"]:
        a = oa[oa.variant == variant].set_index(["context_id", "condition"])
        b = ob[ob.variant == variant].set_index(["context_id", "condition"])
        joined = a[["dialogue_id", "position"]].join((a.y_pred == a.y_true).astype(float).rename("a")).join(
            (b.y_pred == b.y_true).astype(float).rename("b"), how="inner")
        joined = joined.reset_index()
        scopes = [("overall", joined)] + [(p, joined[joined.position == p]) for p in ["Early", "Middle", "Late"]] + \
                 [(f"recall_{c}", joined[joined.condition == c]) for c in rm.CONDITIONS]
        for scope, sub in scopes:
            diff = (sub["a"] - sub["b"]).reset_index(drop=True)
            ed, ld, hd = boot(diff, sub["dialogue_id"].reset_index(drop=True))
            rows.append({"variant": variant, "scope": scope, "accuracy_instruct": sub["a"].mean(),
                         "accuracy_biomed": sub["b"].mean(), "difference": ed, "ci_low": ld, "ci_high": hd, "n": len(sub)})
    return pd.DataFrame(rows)


def compare_rollouts() -> pd.DataFrame:
    fa = pd.read_csv(PAPER / "exp23_results_llama3q4" / f"roll_features_{A}.csv")
    fb = pd.read_csv(PAPER / "exp23_results_biomed" / f"roll_features_{B}.csv")
    rows = []
    for (left, right), marker, direction in [(("P4", "P0"), "psychosocial_per_100", "higher"),
                                             (("P3", "P0"), "psychosocial_per_100", "higher"),
                                             (("P5", "P0"), "instruction_per_100", "higher"),
                                             (("P5", "P0"), "has_question", "lower"),
                                             (("P5", "P0"), "plan_statement_present", "higher")]:
        for k in range(1, 5):
            def delta(f):
                sub = f[f.turn == k]
                wide = sub.pivot(index="base_context", columns="condition", values=marker)
                return (wide[left] - wide[right]), sub.groupby("base_context")["dialogue_id"].first()
            da, dia = delta(fa)
            db, _ = delta(fb)
            both = pd.concat([da.rename("a"), db.rename("b")], axis=1).dropna()
            ea, la, ha = boot(both["a"], dia)
            eb, lb, hb = boot(both["b"], dia)
            ed, ld, hd = boot(both["a"] - both["b"], dia)
            rows.append({"turn": k, "contrast": f"{left} - {right}", "marker": marker,
                         "delta_instruct": ea, "verdict_instruct": rm.verdict(la, ha, direction),
                         "delta_biomed": eb, "verdict_biomed": rm.verdict(lb, hb, direction),
                         "difference": ed, "ci_low": ld, "ci_high": hd, "n_pairs": len(both)})
    return pd.DataFrame(rows)


def main() -> None:
    fa = rm.usable_rows(pd.read_csv(PROJECT / f"analysis/features_{A}.csv"))
    fb = rm.usable_rows(pd.read_csv(PROJECT / f"analysis/features_{B}.csv"))
    assert set(zip(fa.context_id, fa.condition)) == set(zip(fb.context_id, fb.condition))
    out = [compare_features(fa, fb, "OSCE")]
    base = [baseline_profile(fa, fb, "OSCE")]
    aa = rm.usable_rows(pd.read_csv(PAPER / "exp23_results_llama3q4" / f"aci_features_{A}.csv"))
    ab = rm.usable_rows(pd.read_csv(PAPER / "exp23_results_biomed" / f"aci_features_{B}.csv"))
    out.append(compare_features(aa, ab, "ACI-Bench"))
    base.append(baseline_profile(aa, ab, "ACI-Bench"))
    pd.concat(out).to_csv(HERE / "predictions_paired.csv", index=False)
    pd.concat(base).to_csv(HERE / "baseline_profile.csv", index=False)
    compare_accuracy().to_csv(HERE / "accuracy_paired.csv", index=False)
    compare_rollouts().to_csv(HERE / "rollouts_paired.csv", index=False)
    print("DONE")


if __name__ == "__main__":
    main()
