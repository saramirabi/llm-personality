"""Figure: Llama-3-8B-Instruct versus its bio-medical fine-tune, paired persona effects (Experiment 1, OSCE)."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
F = Path("persona_study/analysis/family_comparison")
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
C_INST, C_BIO = "#4a3aa7", "#eda100"
plt.rcParams.update({"font.family": "serif", "font.size": 7.5, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": INK, "axes.spines.top": False, "axes.spines.right": False,
                     "legend.frameon": False, "pdf.fonttype": 42})
MINUS = "\u2212"
ROWS = [  # (contrast, marker, label, scale)
    ("P3 - P0", "psychosocial_per_100", f"P3{MINUS}P0 psychosocial", 1),
    ("P4 - P0", "psychosocial_per_100", f"P4{MINUS}P0 psychosocial", 1),
    ("P4 - P3", "psychosocial_per_100", f"P4{MINUS}P3 psychosocial", 1),
    ("P1 - P0", "med_per_100", f"P1{MINUS}P0 medical terms", 1),
    ("P4 - P0", "share_open", f"P4{MINUS}P0 open share (\u00d710)", 10),
    ("P5 - P0", "invitation_per_100", f"P5{MINUS}P0 invitations", 1),
    ("P5 - P0", "plan_statement_present", f"P5{MINUS}P0 plan statements (\u00d710)", 10),
    ("P5 - P0", "instruction_per_100", f"P5{MINUS}P0 instructions", 1),
]
p = pd.read_csv(F / "predictions_paired.csv")
p = p[(p.corpus == "OSCE") & (p.scope == "overall")]
fig, ax = plt.subplots(figsize=(3.4, 2.6))
for i, (c, mk, label, sc) in enumerate(ROWS):
    r = p[(p.contrast == c) & (p.marker == mk)].iloc[0]
    for off, key, col, mark, name in [(-0.14, "instruct", C_INST, "P", "Llama-3 8B Instruct"),
                                      (0.14, "biomed", C_BIO, "D", "Bio-Medical Llama-3 8B")]:
        est, lo, hi = r[f"delta_{key}"] * sc, r[f"ci_low_{key}"] * sc, r[f"ci_high_{key}"] * sc
        ax.errorbar(est, i + off, xerr=[[est - lo], [hi - est]], fmt=mark, ms=4, color=col, elinewidth=1, capsize=0,
                    markeredgecolor="white", markeredgewidth=0.4, label=name if i == 0 else None)
    if r["difference_significant"]:
        ax.text(8.05, i, "*", va="center", ha="left", fontsize=9, color=INK)
ax.axvline(0, color=MUTED, lw=0.8)
ax.set_yticks(range(len(ROWS))); ax.set_yticklabels([r[2] for r in ROWS]); ax.invert_yaxis()
ax.set_xlim(-3.0, 8.0)
ax.set_xlabel("Paired persona effect \u0394 (95% CI)")
ax.xaxis.grid(True, color=GRID, lw=0.6); ax.set_axisbelow(True)
ax.legend(loc="lower left", bbox_to_anchor=(-0.02, 1.0), ncol=2, fontsize=6.8, handletextpad=0.2, columnspacing=0.8)
fig.savefig(HERE / "fig_family.pdf", bbox_inches="tight")
fig.savefig(HERE / "fig_family.png", bbox_inches="tight", dpi=200)
print("written")
