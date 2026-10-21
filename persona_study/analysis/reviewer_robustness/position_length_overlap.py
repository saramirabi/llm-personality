"""Position effects within a common range of context length (overlap-restricted analysis).

Specified on 2026-10-19, after all results were known. Reanalysis of existing result files only.
For each pair of positions, the window is the range of context lengths covered by both positions
(from the larger minimum to the smaller maximum). Within the window, the later position is compared
with the earlier one on classifier correctness (B1 out-of-fold predictions) and on two persona effects
(P4-P0 psychosocial rate, P5-P0 share of turns with a question). Differences are later minus earlier,
with 95% intervals from 2,000 cluster-bootstrap resamples of dialogues (seed from the analysis plan).
The full-sample difference is reported alongside.
"""
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
MODELS = ["gemini", "claude", "gpt", "llama3instruct", "biomedllama", "medgemma"]
PAIRS = [("Early", "Late"), ("Early", "Middle"), ("Middle", "Late")]
SEED, B = 20261002, 2000


def paired(f, marker, left):
    w = f.pivot(index="context_id", columns="condition", values=marker)
    return (w[left] - w["P0"]).rename("value")


def diff_ci(frame):
    """frame: context-level rows with value, dialogue_id, later (bool). Returns later mean - earlier mean, CI."""
    frame = frame.dropna(subset=["value"])
    est = frame.loc[frame.later, "value"].mean() - frame.loc[~frame.later, "value"].mean()
    groups = frame.dialogue_id.to_numpy()
    uniq = np.unique(groups)
    idx = {g: np.flatnonzero(groups == g) for g in uniq}
    v, later = frame.value.to_numpy(), frame.later.to_numpy()
    rng = np.random.default_rng(SEED)
    s = []
    for _ in range(B):
        take = np.concatenate([idx[g] for g in rng.choice(uniq, len(uniq))])
        lv, lt = v[take], later[take]
        if lt.any() and (~lt).any():
            s.append(lv[lt].mean() - lv[~lt].mean())
    lo, hi = np.percentile(s, [2.5, 97.5])
    return est, lo, hi


def main() -> None:
    rows = []
    for m in MODELS:
        f = pd.read_csv(PROJECT / f"analysis/features_{m}.csv")
        ctx = f[f.condition == "P0"].set_index("context_id")[["dialogue_id", "position", "context_word_count"]]
        oof = pd.read_csv(PROJECT / f"analysis/results/{m}/oof_predictions.csv")
        oof = oof[oof.variant == "B1"]
        acc = (oof.y_pred == oof.y_true).groupby(oof.context_id).mean().rename("value")
        measures = {"accuracy": acc, "P4-P0 psychosocial": paired(f, "psychosocial_per_100", "P4"),
                    "P5-P0 has question": paired(f, "has_question", "P5")}
        for a, b in PAIRS:
            la, lb = ctx[ctx.position == a].context_word_count, ctx[ctx.position == b].context_word_count
            lo, hi = max(la.min(), lb.min()), min(la.max(), lb.max())
            for name, series in measures.items():
                d = ctx.join(series, how="inner")
                d = d[d.position.isin([a, b])].assign(later=lambda x: x.position == b)
                win = d[(d.context_word_count >= lo) & (d.context_word_count <= hi)]
                fe, fl, fh = diff_ci(d)
                we, wl, wh = diff_ci(win)
                rows.append({"model": m, "earlier": a, "later": b, "window_low": lo, "window_high": hi,
                             "n_earlier_in_window": int((~win.later).sum()), "n_later_in_window": int(win.later.sum()),
                             "measure": name, "full_diff": fe, "full_ci_low": fl, "full_ci_high": fh,
                             "window_diff": we, "window_ci_low": wl, "window_ci_high": wh})
    out = pd.DataFrame(rows)
    out.to_csv(HERE / "position_length_overlap.csv", index=False)
    show = out.assign(full=out.full_diff.round(3).astype(str) + " [" + out.full_ci_low.round(3).astype(str) + "," + out.full_ci_high.round(3).astype(str) + "]",
                      window=out.window_diff.round(3).astype(str) + " [" + out.window_ci_low.round(3).astype(str) + "," + out.window_ci_high.round(3).astype(str) + "]")
    print(show[["model", "earlier", "later", "n_earlier_in_window", "n_later_in_window", "measure", "full", "window"]].to_string(index=False))


if __name__ == "__main__":
    main()
