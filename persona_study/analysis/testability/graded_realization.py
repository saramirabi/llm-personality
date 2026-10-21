"""Graded realization: share of pre-specified predictions against P0 that are confirmed (R) and the
directional score R* = (confirmed - opposite) / predictions. Descriptive summary of the strict verdicts
in testability_predictions.csv (read unchanged from c_predictions.csv and aci_predictions.csv)."""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
d = pd.read_csv(HERE / "testability_predictions.csv")
d = d[(d.in_realised_rule == 1) & d.contrast.str.endswith("P0")]
d["persona"] = d.contrast.str[:2]
g = d.groupby(["corpus", "model", "persona"]).agg(n=("verdict", "size"), confirmed=("verdict", lambda v: (v == "confirmed").sum()),
                                                 opposite=("verdict", lambda v: (v == "opposite").sum())).reset_index()
g["R"] = g.confirmed / g.n
g["R_star"] = (g.confirmed - g.opposite) / g.n
g["complete"] = (g.confirmed == g.n).astype(int)
g.to_csv(HERE / "graded_realization.csv", index=False)
g["cell"] = g.confirmed.astype(str) + "/" + g.n.astype(str) + g.opposite.map(lambda o: f" ({o} opp)" if o else "")
print(g.pivot_table(index=["corpus", "persona"], columns="model", values="cell", aggfunc="first").to_string())
print(g.groupby(["corpus", "persona"])[["R", "R_star"]].agg(["min", "max"]).round(2).to_string())
