"""Figures for the ICAART paper. Reads the frozen result tables; writes PDFs next to this file."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
RES = Path("persona_study/analysis/results")
EXP23 = HERE / "exp23_results"
MODELS = ["gemini", "claude", "gpt", "llama3instruct", "biomedllama", "medgemma"]
LABEL = {"gemini": "Gemini 2.5 Flash-Lite", "claude": "Claude Haiku 4.5", "gpt": "GPT-4o mini", "llama3instruct": "Llama-3 8B Instruct", "biomedllama": "Bio-Medical Llama-3 8B", "medgemma": "MedGemma 4B"}
COLOR = {"gemini": "#2a78d6", "claude": "#eb6834", "gpt": "#1baf7a", "llama3instruct": "#4a3aa7", "biomedllama": "#eda100", "medgemma": "#e87ba4"}
MARK = {"gemini": "o", "claude": "s", "gpt": "^", "llama3instruct": "P", "biomedllama": "D", "medgemma": "v"}
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({"font.family": "serif", "font.size": 8, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False,
                     "legend.frameon": False, "pdf.fonttype": 42})


def style(ax, chance, ylabel):
    ax.axhline(chance, color=MUTED, lw=0.8, ls=(0, (3, 2)), zorder=0)
    ax.text(ax.get_xlim()[1], chance + 0.01, "chance", ha="right", va="bottom", color=MUTED, fontsize=7)
    ax.set_ylim(0, 1.02); ax.set_ylabel(ylabel)
    ax.yaxis.grid(True, color=GRID, lw=0.6); ax.set_axisbelow(True)


# Figure 2: per-condition recall (B1), with position panels
rec = pd.concat([pd.read_csv(RES / m / "b_recall.csv").assign(model=m) for m in MODELS])
rec = rec[rec["variant"] == "B1"]
conds = ["P0", "P1", "P2", "P3", "P4", "P5"]
fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.3), sharey=True)
for ax, scope in zip(axes, ["Early", "Middle", "Late"]):
    for k, m in enumerate(MODELS):
        r = rec[(rec.model == m) & (rec.scope == scope)].set_index("condition").loc[conds]
        x = [i + (k - 2.5) * 0.13 for i in range(6)]
        ax.errorbar(x, r.recall, yerr=[r.recall - r.ci_low, r.ci_high - r.recall], fmt=MARK[m], ms=3.6,
                    color=COLOR[m], ecolor=COLOR[m], elinewidth=1, capsize=0, label=LABEL[m],
                    markeredgecolor="white", markeredgewidth=0.5)
    ax.set_xticks(range(6)); ax.set_xticklabels(conds); ax.set_xlim(-0.5, 5.5)
    style(ax, 1 / 6, "Recall" if scope == "Early" else "")
    ax.set_title(scope, fontsize=8, color=INK)
fig.tight_layout(rect=(0, 0, 1, 0.88))
h, l = axes[0].get_legend_handles_labels(); fig.legend(h, l, loc="upper center", ncol=6, fontsize=6.5); fig.savefig(HERE / "fig_recall.pdf", bbox_inches="tight"); plt.close(fig)

# Figure 3: (a) accuracy by position (Exp 1), (b) recall by rollout turn (Exp 2)
acc = pd.concat([pd.read_csv(RES / m / "b_accuracy.csv").assign(model=m) for m in MODELS])
acc = acc[acc.variant == "B1"]
roll = pd.concat([pd.read_csv(EXP23 / "roll_recall.csv").query("model != 'gpt'"), pd.read_csv(HERE / "exp23_results_gpt4o" / "roll_recall.csv"), pd.read_csv(HERE / "exp23_results_med" / "roll_recall.csv"),
                  pd.read_csv(HERE / "exp23_results_biomed" / "roll_recall.csv"), pd.read_csv(HERE / "exp23_results_llama3q4" / "roll_recall.csv")])
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.0, 2.2), sharey=True)
pos = ["Early", "Middle", "Late"]
for m in MODELS:
    r = acc[acc.model == m].set_index("scope").loc[pos]
    a1.errorbar(range(3), r.accuracy, yerr=[r.accuracy - r.ci_low, r.ci_high - r.accuracy], color=COLOR[m],
                marker=MARK[m], ms=4.5, lw=1.6, elinewidth=1, label=LABEL[m], markeredgecolor="white", markeredgewidth=0.5)
    q = roll[(roll.model == m) & (roll.condition == "all")].sort_values("turn")
    a2.errorbar(q.turn, q.recall, yerr=[q.recall - q.ci_low, q.ci_high - q.recall], color=COLOR[m],
                marker=MARK[m], ms=4.5, lw=1.6, elinewidth=1, markeredgecolor="white", markeredgewidth=0.5)
a1.set_xticks(range(3)); a1.set_xticklabels(pos); a1.set_xlim(-0.3, 2.3)
a2.set_xticks([1, 2, 3, 4]); a2.set_xlim(0.7, 4.3); a2.set_xlabel("Clinician turn in rollout")
a1.set_xlabel("Position of target (Experiment 1)")
style(a1, 1 / 6, "Accuracy"); style(a2, 1 / 6, "")
a1.set_title("(a) Single turn, by position", fontsize=8, color=INK, loc="left")
a2.set_title("(b) Multi-turn rollouts, by turn", fontsize=8, color=INK, loc="left")
fig.tight_layout(rect=(0, 0, 1, 0.86))
h, l = a1.get_legend_handles_labels(); fig.legend(h, l, loc="upper center", ncol=6, fontsize=6.5); fig.savefig(HERE / "fig_position_turns.pdf", bbox_inches="tight"); plt.close(fig)
print("figures written")
