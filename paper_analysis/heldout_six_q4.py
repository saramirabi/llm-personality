"""Held-out-model classifier over all six models (Llama-3 Q4_K_S), using run_measurement.cross_model_generalise unchanged."""
import sys, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
PROJECT = Path("persona_study")
sys.path.insert(0, str(PROJECT / "src"))
import pandas as pd
import run_measurement as rm
OUT = Path(__file__).resolve().parent / "exp23_results_med"
OUT.mkdir(exist_ok=True)
plan = rm.load_plan(rm.PLAN_PATH); seed = int(plan["seed"])
frames = []
for m in ["gemini", "claude", "gpt", "llama3instruct", "biomedllama", "medgemma"]:
    d = pd.read_csv(PROJECT / f"outputs/main_{m}_cleaned.csv")
    d = d[d["analysis_text"].fillna("").str.strip() != ""].copy(); d["model"] = m
    frames.append(d)
acc, rec, conf = rm.cross_model_generalise(frames, plan, seed)
acc.to_csv(OUT / "heldout6q4_accuracy.csv", index=False); rec.to_csv(OUT / "heldout6q4_recall.csv", index=False); conf.to_csv(OUT / "heldout6q4_confusion.csv", index=False)
print(acc[acc.scope == "overall"][["held_out_model", "accuracy", "ci_low", "ci_high"]].round(3).to_string(index=False))
r = rec[rec.scope == "overall"].pivot(index="held_out_model", columns="condition", values="recall").round(2); print(r)
