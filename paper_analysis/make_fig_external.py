"""Figure: external validation of the style markers with Empath and ConvoKit (Experiment 1, OSCE, full text)."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = Path(__file__).resolve().parent
EV = Path("persona_study/analysis/external_validation")
MODELS = ["gemini", "claude", "gpt", "llama3instruct", "biomedllama", "medgemma"]
SHORT = {"gemini": "Gemini", "claude": "Claude", "gpt": "GPT-4o mini", "llama3instruct": "Llama-3", "biomedllama": "BioMed-Llama", "medgemma": "MedGemma"}
COLOR = {"gemini": "#2a78d6", "claude": "#eb6834", "gpt": "#1baf7a", "llama3instruct": "#4a3aa7", "biomedllama": "#eda100", "medgemma": "#e87ba4"}
MARK = {"gemini": "o", "claude": "s", "gpt": "^", "llama3instruct": "P", "biomedllama": "D", "medgemma": "v"}
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({"font.family": "serif", "font.size": 7.5, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": INK, "axes.spines.top": False, "axes.spines.right": False,
                     "legend.frameon": False, "pdf.fonttype": 42})
MINUS, UP, DOWN = "\u2212", "\u2191", "\u2193"
CHECK, DASH, CROSS = "\u2713", "\u2013", "\u00d7"

PAIRS = [  # (marker, external, label)
    ("psychosocial_per_100", "empath_psychosocial_per_100", "Psychosocial vs Empath psychosocial"),
    ("med_per_100", "empath_medical_per_100", "Medical terms vs Empath medical"),
    ("hedge_per_100", "ck_HASHEDGE_present", "Hedges vs ConvoKit HASHEDGE"),
    ("plan_statement_present", "ck_1st_person_start_present", "Plan statements vs 1st_person_start"),
    ("has_question", "ck_Direct_question_present", "Any question vs Direct_question"),
    ("instruction_per_100", "ck_2nd_person_start_per_100", "Instructions vs 2nd_person_start"),
]
PRED = [  # (contrast, external, label)
    ("P1 - P0", "empath_psychosocial_per_100", f"P1{MINUS}P0 psychosocial {DOWN}"),
    ("P2 - P1", "empath_psychosocial_per_100", f"P2{MINUS}P1 psychosocial {UP}"),
    ("P3 - P0", "empath_psychosocial_per_100", f"P3{MINUS}P0 psychosocial {UP}"),
    ("P4 - P0", "empath_psychosocial_per_100", f"P4{MINUS}P0 psychosocial {UP}"),
    ("P4 - P3", "empath_psychosocial_per_100", f"P4{MINUS}P3 psychosocial {UP}"),
    ("P1 - P0", "empath_medical_per_100", f"P1{MINUS}P0 medical {UP}"),
    ("P4 - P0", "empath_medical_per_100", f"P4{MINUS}P0 medical {DOWN}"),
    ("P4 - P3", "empath_medical_per_100", f"P4{MINUS}P3 medical {DOWN}"),
    ("P5 - P0", "ck_1st_person_start_present", f"P5{MINUS}P0 plan / 1st_pers._start {UP}"),
    ("P5 - P0", "ck_2nd_person_start_present", f"P5{MINUS}P0 instruct. / 2nd_pers._start {UP}"),
    ("P5 - P0", "ck_Direct_question_present", f"P5{MINUS}P0 question / Direct_quest. {DOWN}"),
]
SYM = {"confirmed": CHECK, "not confirmed": DASH, "opposite": CROSS}
FILL = {"agree_conf": "#2a78d6", "agree_other": "#e4e3df", "disagree": "#f2b8a0", "opposite": "#d95926"}

a = pd.concat([pd.read_csv(EV / "A_convergence_FULL.csv").query("model not in ['gpt', 'llama2chat']"), pd.read_csv(EV / "gpt4omini" / "A_convergence_FULL.csv"), pd.read_csv(EV / "biomedllama" / "A_convergence_FULL.csv"), pd.read_csv(EV / "llama3instruct_q4" / "A_convergence_FULL.csv")])
b = pd.concat([pd.read_csv(EV / "B_replication_FULL.csv").query("model not in ['gpt', 'llama2chat']"), pd.read_csv(EV / "gpt4omini" / "B_replication_FULL.csv"), pd.read_csv(EV / "biomedllama" / "B_replication_FULL.csv"), pd.read_csv(EV / "llama3instruct_q4" / "B_replication_FULL.csv")])
b = b[b["status"] == "prediction"]

fig = plt.figure(figsize=(7.2, 3.3))
ax1 = fig.add_axes([0.235, 0.24, 0.20, 0.62])
ax2 = fig.add_axes([0.70, 0.24, 0.295, 0.62])

# (a) convergence
for k, m in enumerate(MODELS):
    ys, xs, lo, hi = [], [], [], []
    for i, (marker, ext, _) in enumerate(PAIRS):
        r = a[(a.model == m) & (a.marker == marker) & (a.external == ext)].iloc[0]
        ys.append(i + (k - 2.5) * 0.12); xs.append(r.spearman)
        lo.append(r.spearman - r.ci_low); hi.append(r.ci_high - r.spearman)
    ax1.errorbar(xs, ys, xerr=[lo, hi], fmt=MARK[m], ms=3.6, color=COLOR[m], elinewidth=1, capsize=0,
                 markeredgecolor="white", markeredgewidth=0.4, label=SHORT[m])
ax1.axvline(0, color=MUTED, lw=0.8)
ax1.set_yticks(range(len(PAIRS))); ax1.set_yticklabels([p[2] for p in PAIRS]); ax1.invert_yaxis()
ax1.set_xlim(-0.2, 0.65); ax1.set_xlabel("Spearman correlation (95% CI)")
ax1.xaxis.grid(True, color=GRID, lw=0.6); ax1.set_axisbelow(True)
fig.text(0.005, 1.03, "(a) Convergence with the existing markers", fontsize=8, color=INK)

# (b) verdict agreement grid
for i, (contrast, ext, _) in enumerate(PRED):
    for j, m in enumerate(MODELS):
        r = b[(b.model == m) & (b.contrast == contrast) & (b.external == ext)].iloc[0]
        orig, new = r.marker_verdict_original_full_text, r.external_verdict
        if new == "opposite":
            key = "opposite"
        elif orig == new:
            key = "agree_conf" if orig == "confirmed" else "agree_other"
        else:
            key = "disagree"
        ax2.add_patch(plt.Rectangle((j + 0.04, i + 0.06), 0.92, 0.88, color=FILL[key], lw=0))
        ink = "white" if key in ("agree_conf", "opposite") else INK
        ax2.text(j + 0.5, i + 0.5, f"{SYM[orig]} {SYM[new]}", ha="center", va="center", fontsize=7.5,
                 color=ink, fontfamily="DejaVu Sans")
ax2.set_xlim(0, len(MODELS)); ax2.set_ylim(len(PRED), 0)
ax2.set_xticks([j + 0.5 for j in range(len(MODELS))])
ax2.set_xticklabels([SHORT[m] for m in MODELS], rotation=35, ha="left")
ax2.xaxis.tick_top(); ax2.tick_params(length=0)
ax2.set_yticks([i + 0.5 for i in range(len(PRED))]); ax2.set_yticklabels([p[2] for p in PRED])
for s in ax2.spines.values():
    s.set_visible(False)
fig.text(0.44, 1.03, "(b) Verdicts: existing marker, then external measure", fontsize=8, color=INK)

# legends
h1, l1 = ax1.get_legend_handles_labels()
fig.legend(h1, l1, loc="lower left", bbox_to_anchor=(0.0, 0.0), ncol=6, fontsize=6.5, columnspacing=0.6, handletextpad=0.2)
handles = [Patch(color=FILL["agree_conf"], label="both confirmed"), Patch(color=FILL["agree_other"], label="both not confirmed"),
           Patch(color=FILL["disagree"], label="disagree"), Patch(color=FILL["opposite"], label="external opposite")]
fig.legend(handles=handles, loc="lower right", bbox_to_anchor=(1.0, -0.01), ncol=2, fontsize=7, columnspacing=0.8)
fig.text(0.99, 0.125, f"{CHECK} confirmed   {DASH} not confirmed   {CROSS} opposite", ha="right", fontsize=7,
         fontfamily="DejaVu Sans", color=INK)
fig.savefig(HERE / "fig_external_validation.pdf", bbox_inches="tight")
fig.savefig(HERE / "fig_external_validation.png", bbox_inches="tight", dpi=200)
print("written")
