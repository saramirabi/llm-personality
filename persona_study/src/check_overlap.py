#!/usr/bin/env python3
"""Assert persona-study pools share no target turns with the paper 1 frozen set."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

TURN_ID_RE_TEMPLATE = r"^(?P<dialogue_id>.+)_turn_(?P<index>\d+)$"


def load_config(path: Path) -> dict[str, object]:
    data: dict[str, object] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = []
            for item in value[1:-1].split(","):
                item = item.strip().strip("'\"")
                if not item:
                    continue
                items.append(int(item) if item.isdigit() else item)
            data[key] = items
        elif value.isdigit():
            data[key] = int(value)
        else:
            data[key] = value.strip("'\"")
    return data


def require(config: dict[str, object], key: str) -> object:
    if key not in config:
        raise SystemExit(f"Missing config key: {key}")
    return config[key]


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"{path} has no header.")
        return list(reader.fieldnames), list(reader)


def paper1_pairs(path: Path) -> set[tuple[str, int]]:
    import re

    pattern = re.compile(TURN_ID_RE_TEMPLATE)
    fieldnames, rows = read_rows(path)
    for column in ("dialogue_id", "target_turn_id"):
        if column not in fieldnames:
            raise SystemExit(f"{path.name} is missing column {column}. Found: {fieldnames}")
    pairs: set[tuple[str, int]] = set()
    for row in rows:
        match = pattern.match(row["target_turn_id"])
        if match is None or match.group("dialogue_id") != row["dialogue_id"]:
            raise SystemExit(
                f"Unparseable paper 1 target id {row['target_turn_id']!r} "
                f"for dialogue {row['dialogue_id']!r}."
            )
        pairs.add((row["dialogue_id"], int(match.group("index"))))
    if len(pairs) != len(rows):
        raise SystemExit(
            f"{path.name} has {len(rows)} rows but {len(pairs)} unique targets."
        )
    return pairs


def pool_pairs(path: Path) -> set[tuple[str, int]]:
    fieldnames, rows = read_rows(path)
    for column in ("dialogue_id", "target_turn_index"):
        if column not in fieldnames:
            raise SystemExit(f"{path.name} is missing column {column}. Found: {fieldnames}")
    if "human_clinician_target" in fieldnames:
        raise SystemExit(f"{path.name} contains the human target column.")
    pairs: set[tuple[str, int]] = set()
    for row in rows:
        pairs.add((row["dialogue_id"], int(row["target_turn_index"])))
    if len(pairs) != len(rows):
        raise SystemExit(f"{path.name} has duplicate (dialogue_id, target_turn_index) rows.")
    return pairs


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    config_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else project_dir / "config.yaml"
    config = load_config(config_path)
    project_dir = config_path.parent

    frozen_path = Path(str(require(config, "paper1_frozen_csv")))
    pool_dir = project_dir / str(require(config, "pool_dir"))
    pool_names = require(config, "pool_filenames")
    if not isinstance(pool_names, list) or not pool_names:
        raise SystemExit("pool_filenames must be a non-empty list.")

    paper_pairs = paper1_pairs(frozen_path)
    print(f"Paper 1 frozen targets: {len(paper_pairs)} from {frozen_path.name}")

    failed = False
    for name in pool_names:
        path = pool_dir / str(name)
        pairs = pool_pairs(path)
        shared = pairs & paper_pairs
        print(
            f"{name}: pool={len(pairs)} shared_with_paper1={len(shared)}"
        )
        if shared:
            failed = True
            sample = sorted(shared)[:10]
            print(f"  OVERLAP EXAMPLES: {sample}")

    if failed:
        raise SystemExit("OVERLAP CHECK FAILED: shared (dialogue_id, target_turn_index) pairs are not 0.")
    print("OVERLAP CHECK PASSED: shared pairs = 0 for every pool.")


if __name__ == "__main__":
    main()
