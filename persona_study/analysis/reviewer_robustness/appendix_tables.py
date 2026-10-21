"""LaTeX tables for the appendix, from existing result files only (no new statistics beyond reference means).

1. effect_sizes.tex: paired persona effect and 95% cluster-bootstrap interval for every OSCE prediction
   and model, read from results/<model>/c_predictions.csv.
2. family_baseline.tex: baseline-adjusted family comparison, from family_comparison_q4/predictions_paired.csv,
   with each model's reference mean and the room left in the predicted direction (headroom).
"""
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
MODELS = ["gemini", "claude", "gpt", "llama3instruct", "biomedllama", "medgemma"]
LABEL = {"psychosocial_per_100": "psychosocial", "med_per_100": "medical terms", "share_open": "open share",
         "n_leading": "leading questions", "instruction_per_100": "instructions", "invitation_per_100": "invitations",
         "has_question": "questions", "plan_statement_present": "plan statements"}
BOUNDED = {"share_open", "has_question", "plan_statement_present"}
ARROW = {"higher": r"$\uparrow$", "lower": r"$\downarrow$"}
MARK = {"confirmed": "", "not confirmed": r"$^{\circ}$", "opposite": r"$^{\times}$"}


def fmt(x):
    return f"{x:.2f}".replace("-0.00", "0.00").replace("-", "$-$")


def effect_sizes():
    preds = {m: pd.read_csv(PROJECT / f"analysis/results/{m}/c_predictions.csv").query("scope == 'overall'")
             .set_index(["contrast", "marker"]) for m in MODELS}
    order = preds["gemini"].index.tolist()
    lines, last = [], None
    for contrast, marker in order:
        r0 = preds["gemini"].loc[(contrast, marker)]
        dag = r"$^{\dagger}$" if r0.specification != "pre-specified" else ""
        c = contrast.replace(" - ", "$-$") if contrast != last else ""
        last = contrast
        cells = []
        for m in MODELS:
            r = preds[m].loc[(contrast, marker)]
            spec_mark = MARK[r.verdict]
            cells.append(rf"\makecell{{{fmt(r.estimate)}{spec_mark}\\{{\tiny[{fmt(r.ci_low)},{fmt(r.ci_high)}]}}}}")
        lines.append(f"{c} & {LABEL[marker]}{dag} {ARROW[r0.direction]} & " + " & ".join(cells) + r" \\")
    (HERE / "effect_sizes.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def family_baseline():
    p = pd.read_csv(PROJECT / "analysis/family_comparison_q4/predictions_paired.csv")
    p = p[(p.corpus == "OSCE") & (p.scope == "overall")]
    fa = pd.read_csv(PROJECT / "analysis/features_llama3instruct.csv")
    fb = pd.read_csv(PROJECT / "analysis/features_biomedllama.csv")
    rows = [("P1 - P0", "psychosocial_per_100"), ("P1 - P0", "med_per_100"), ("P3 - P0", "psychosocial_per_100"),
            ("P4 - P0", "psychosocial_per_100"), ("P4 - P0", "share_open"), ("P5 - P0", "instruction_per_100"),
            ("P5 - P0", "invitation_per_100"), ("P5 - P0", "share_open"), ("P5 - P0", "has_question"),
            ("P5 - P0", "plan_statement_present")]
    lines = []
    for contrast, marker in rows:
        r = p[(p.contrast == contrast) & (p.marker == marker)].iloc[0]
        ref = contrast.split(" - ")[1]
        ma, mb = fa.loc[fa.condition == ref, marker].mean(), fb.loc[fb.condition == ref, marker].mean()
        room = (lambda x: x) if r.direction == "lower" else ((lambda x: 1 - x) if marker in BOUNDED else None)
        ha, hb = (fmt(room(ma)), fmt(room(mb))) if room else ("--", "--")
        sig = r"$^{\ast}$" if r.difference_significant else ""
        lines.append(f"{contrast.replace(' - ', '$-$')} {LABEL[marker]} {ARROW[r.direction]} & {fmt(ma)} & {fmt(mb)} & "
                     f"{ha} & {hb} & {fmt(r.delta_instruct)} & {fmt(r.delta_biomed)} & "
                     f"{fmt(r.difference_instruct_minus_biomed)}{sig} {{\\tiny[{fmt(r.ci_low_diff)},{fmt(r.ci_high_diff)}]}} \\\\")
    (HERE / "family_baseline.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    effect_sizes()
    family_baseline()
    print((HERE / "effect_sizes.tex").read_text()[:900])
    print((HERE / "family_baseline.tex").read_text())
