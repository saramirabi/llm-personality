"""Figure 1: overview of the study design (shared design and the three experiments)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

HERE = Path(__file__).resolve().parent
INK, MUTED, RULE = "#14232b", "#56676e", "#c9d4d6"
ACC, ACC_SOFT = "#0d6a70", "#dcecec"
DOC, PAT = "#2a78d6", "#eb6834"
plt.rcParams.update({"font.family": "serif", "font.size": 7.5, "pdf.fonttype": 42})

fig = plt.figure(figsize=(7.2, 2.75))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 38); ax.axis("off")


def box(x, y, w, h, fc="white", ec=RULE, lw=0.8, r=0.8):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw))


def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=7, color=MUTED, lw=0.8))


# ---------------- Left: shared design ----------------
ax.text(1, 36.2, "Shared design", fontsize=9, fontweight="bold", color=INK, va="center")
# transcript as alternating turns
ax.text(1, 32.6, "Real clinician–patient transcript", fontsize=7, color=MUTED)
x0, y0, n = 1, 28.6, 22
for i in range(n):
    ax.add_patch(Rectangle((x0 + i * 2.05, y0), 1.75, 2.4, fc=DOC if i % 2 == 0 else PAT, ec="none", alpha=0.85))
for lbl, i in [("Early", 6), ("Middle", 12), ("Late", 18)]:
    xc = x0 + i * 2.05 - 0.15
    ax.plot([xc, xc], [y0 - 0.6, y0 + 3.0], color=INK, lw=1.0)
    ax.text(xc, y0 - 1.8, lbl, ha="center", fontsize=6.8, color=INK)
ax.text(1, 24.2, "Cut before a clinician turn at three positions;\nthe original turn is never shown.", fontsize=6.6, color=MUTED, va="top")

# context -> conditions x models -> next turn
box(1, 4.5, 13, 13, fc=ACC_SOFT, ec=ACC)
ax.text(7.5, 14.6, "Identical\ndialogue\nhistory", ha="center", va="top", fontsize=7.2, color=INK)
ax.text(7.5, 7.0, "804 OSCE\n612 ACI-Bench", ha="center", va="center", fontsize=6.4, color=MUTED)
arrow(14.3, 11, 17.2, 11)
box(17.5, 4.5, 15.5, 13)
ax.text(25.25, 15.9, "6 conditions", ha="center", fontsize=7.2, color=INK, fontweight="bold")
ax.text(25.25, 13.9, "P0 baseline\nP1–P4 content scale\nP5 directive", ha="center", va="top", fontsize=6.4, color=MUTED, linespacing=1.3)
ax.text(25.25, 7.2, "×  6 LLMs", ha="center", fontsize=7.2, color=INK, fontweight="bold")
ax.text(25.25, 5.4, "4 general, 2 medical", ha="center", fontsize=6.2, color=MUTED)
arrow(33.3, 11, 36.2, 11)
box(36.5, 4.5, 10.5, 13)
ax.text(41.75, 15.9, "Next\nclinician\nturn", ha="center", va="top", fontsize=7.2, color=INK)
ax.text(41.75, 7.6, "classifier\n+ markers", ha="center", va="center", fontsize=6.4, color=MUTED)

ax.plot([49.5, 49.5], [2, 36.5], color=RULE, lw=0.8)

# ---------------- Right: three experiments ----------------
ax.text(51.5, 36.2, "Three experiments", fontsize=9, fontweight="bold", color=INK, va="center")
rows = [
    ("Experiment 1", "Single next turn, OSCE", "804 contexts · 268 per position · 28,944 outputs", "D"),
    ("Experiment 2", "Four-turn rollouts with a simulated patient", "150 contexts · 3,600 clinician turns per model", "DPDPDPD"),
    ("Experiment 3", "Single next turn, whole visits (ACI-Bench)", "612 contexts · 22,032 outputs", "D"),
]
for k, (name, what, size, seq) in enumerate(rows):
    y = 25.2 - k * 10.6
    box(51.5, y, 47, 8.8)
    ax.text(53, y + 6.6, name, fontsize=7.4, color=ACC, fontweight="bold", va="center")
    ax.text(53, y + 4.3, what, fontsize=7.2, color=INK, va="center")
    ax.text(53, y + 2.0, size, fontsize=6.4, color=MUTED, va="center")
    for j, s in enumerate(seq):
        ax.add_patch(Rectangle((84.5 + j * 1.9, y + 5.6), 1.6, 2.1, fc=DOC if s == "D" else PAT, ec="none", alpha=0.85))

ax.add_patch(Rectangle((51.5, 0.6), 1.6, 1.6, fc=DOC, ec="none", alpha=0.85))
ax.text(53.6, 1.4, "clinician turn", fontsize=6.4, color=MUTED, va="center")
ax.add_patch(Rectangle((66, 0.6), 1.6, 1.6, fc=PAT, ec="none", alpha=0.85))
ax.text(68.1, 1.4, "patient turn", fontsize=6.4, color=MUTED, va="center")

fig.savefig(HERE / "fig_experiments.pdf", bbox_inches="tight")
fig.savefig(HERE / "fig_experiments.png", bbox_inches="tight", dpi=200)
print("written")
