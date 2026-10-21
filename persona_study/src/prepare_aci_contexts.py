#!/usr/bin/env python3
"""Build ACI-Bench next-turn contexts for the existing persona scenario.

Uses the five published challenge splits. Clinical notes are never written.
Position uses the same one-third rule as the OSCE pool. One Early, Middle,
and Late target is drawn per dialogue with seed 20261002 and clinician-turn
spacing of at least 2. The OSCE question-mark filter is not applied: these
transcripts are ASR text, and that filter leaves most visits without a trio.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

import numpy as np

SEED = 20261002
MIN_COMPLETED_EXCHANGES = 2
MIN_SPACING = 2
TAG = re.compile(r"\[(doctor|patient)\]", re.IGNORECASE)
SPLITS = (
    ("train", "train.csv"),
    ("valid", "valid.csv"),
    ("test1", "clinicalnlp_taskB_test1.csv"),
    ("test2", "clinicalnlp_taskC_test2.csv"),
    ("test3", "clef_taskC_test3.csv"),
)


def parse_dialogue(text: str) -> list[tuple[str, str]]:
    matches = list(TAG.finditer(text))
    turns: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        utterance = text[start:end].strip()
        if utterance:
            turns.append((match.group(1).lower(), utterance))
    return turns


def position_third(normalized: float) -> str:
    if normalized <= 1 / 3:
        return "Early"
    if normalized <= 2 / 3:
        return "Middle"
    return "Late"


def spacing_ok(ordinals: list[int]) -> bool:
    for index, left in enumerate(ordinals):
        for right in ordinals[index + 1 :]:
            if abs(left - right) < MIN_SPACING:
                return False
    return True


def format_context(turns: list[tuple[str, str]]) -> str:
    blocks = []
    for speaker, text in turns:
        label = "Doctor" if speaker == "doctor" else "Patient"
        blocks.append(f"{label}: {text}")
    return "\n\n".join(blocks)


def candidates_for(turns: list[tuple[str, str]]) -> list[dict[str, object]]:
    doctor_ordinal = 0
    doctor_ordinal_by_index: dict[int, int] = {}
    for index, (speaker, _text) in enumerate(turns):
        if speaker == "doctor":
            doctor_ordinal += 1
            doctor_ordinal_by_index[index] = doctor_ordinal
    candidate_indices = [
        index
        for index, (speaker, _text) in enumerate(turns)
        if speaker == "doctor" and index > 0 and turns[index - 1][0] == "patient"
    ]
    rows: list[dict[str, object]] = []
    count = len(candidate_indices)
    for number, index in enumerate(candidate_indices, start=1):
        prior_patient = sum(1 for speaker, _text in turns[:index] if speaker == "patient")
        if prior_patient < MIN_COMPLETED_EXCHANGES:
            continue
        rows.append(
            {
                "position": position_third(number / count),
                "target_turn_index": index + 1,
                "clinician_ordinal": doctor_ordinal_by_index[index],
                "context": format_context(turns[:index]),
                "context_word_count": len(format_context(turns[:index]).split()),
            }
        )
    return rows


def draw_index(rng: np.random.Generator, size: int) -> int:
    return int(rng.integers(0, size))


def select_trio(dialogue_id: str, rows: list[dict[str, object]], rng: np.random.Generator) -> list[dict[str, object]] | None:
    groups = {position: [row for row in rows if row["position"] == position] for position in ("Early", "Middle", "Late")}
    if any(not groups[position] for position in groups):
        return None
    for _attempt in range(100000):
        chosen = [groups[position][draw_index(rng, len(groups[position]))] for position in ("Early", "Middle", "Late")]
        ordinals = [int(row["clinician_ordinal"]) for row in chosen]
        if spacing_ok(ordinals):
            return [dict(row) for row in chosen]
    raise SystemExit(f"{dialogue_id} did not satisfy spacing.")


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    source = project / "data" / "aci_bench" / "challenge_data"
    output = project / "data" / "aci_bench" / "aci_contexts.csv"
    manifest_path = project / "data" / "aci_bench" / "aci_context_manifest.json"
    rng = np.random.default_rng(SEED)
    selected: list[dict[str, object]] = []
    dropped: list[dict[str, str]] = []
    for split, filename in SPLITS:
        with (source / filename).open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                if "note" in row:
                    row = {key: value for key, value in row.items() if key != "note"}
                encounter = row["encounter_id"]
                turns = parse_dialogue(row["dialogue"])
                trio = select_trio(encounter, candidates_for(turns), rng)
                if trio is None:
                    dropped.append({"dataset": split, "encounter_id": encounter})
                    continue
                for item in trio:
                    item["dataset"] = split
                    item["dialogue_id"] = encounter
                    item["context_id"] = f"ACI_{split}_{encounter}_{item['position']}"
                    selected.append(item)
    fieldnames = [
        "context_id",
        "dialogue_id",
        "dataset",
        "position",
        "target_turn_index",
        "clinician_ordinal",
        "context",
        "context_word_count",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in selected:
            writer.writerow({key: row[key] for key in fieldnames})
    counts = Counter((row["dataset"], row["position"]) for row in selected)
    words = [int(row["context_word_count"]) for row in selected]
    words.sort()
    manifest = {
        "source": "https://github.com/wyim/aci-bench/tree/main/data/challenge_data",
        "splits": [name for name, _filename in SPLITS],
        "seed": SEED,
        "min_completed_exchanges": MIN_COMPLETED_EXCHANGES,
        "min_spacing": MIN_SPACING,
        "contexts": len(selected),
        "dialogues": len({row["dialogue_id"] for row in selected}),
        "dropped": dropped,
        "counts": {f"{dataset}:{position}": count for (dataset, position), count in sorted(counts.items())},
        "context_words_min": words[0] if words else None,
        "context_words_median": words[len(words) // 2] if words else None,
        "context_words_max": words[-1] if words else None,
        "notes_included": False,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: manifest[key] for key in ("contexts", "dialogues", "dropped", "context_words_min", "context_words_median", "context_words_max")}, indent=2))


if __name__ == "__main__":
    main()
