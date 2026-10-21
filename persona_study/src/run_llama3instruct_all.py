"""Run Meta Llama 3 8B Instruct E1, its measurement, E2, then E3. Does not analyse E3."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
PY = sys.executable


def run(args: list[str]) -> int:
    print("START", " ".join(args), flush=True)
    completed = subprocess.run(args, cwd=PROJECT)
    print("EXIT", completed.returncode, " ".join(args), flush=True)
    return completed.returncode


def main() -> None:
    e1 = run([PY, "src/run_local_llama3instruct.py", "--phase", "e1", "--workers", "1"])
    cleaned = PROJECT / "outputs" / "main_llama3instruct_cleaned.csv"
    if not cleaned.exists():
        raise SystemExit(f"E1 did not write a cleaned table. exit={e1}")
    measured = run(
        [PY, "src/run_measurement.py", "--config", "config_llama3instruct_measurement.yaml", "--skip-combined"]
    )
    e2 = run([PY, "src/run_local_llama3instruct.py", "--phase", "e2", "--workers", "1"])
    e3 = run([PY, "src/rollout.py", "--run", "--doctor", "llama3instruct"])
    raise SystemExit(e3 or e2 or measured or e1)


if __name__ == "__main__":
    main()
