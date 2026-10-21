#!/usr/bin/env python3
"""Sample and freeze the persona-study contexts. No model calls."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import numpy as np

MAIN_FIELDS = [
    "context_id",
    "dialogue_id",
    "specialty",
    "target_turn_index",
    "position",
    "normalized_target_position",
    "completed_exchanges_before_target",
    "context",
    "latest_patient_turn",
    "context_word_count",
    "in_subset",
]
PILOT_FIELDS = [field for field in MAIN_FIELDS if field != "in_subset"]
POSITIONS = ("Early", "Middle", "Late")
POSITION_RANK = {name: index for index, name in enumerate(POSITIONS)}
EXPECTED_BEFORE_EXCLUSION = {"Early": 2349, "Middle": 2646, "Late": 2242}
MIN_DIALOGUES = 260
SPECIALTY_ORDER = (
    "Cardiovascular",
    "Dermatological",
    "Gastrointestinal",
    "General",
    "Musculoskeletal",
    "Respiratory",
)


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


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"{path} has no header.")
        return list(reader.fieldnames), list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row[name] for name in fieldnames})


def frozen_key(row: dict[str, str]) -> tuple[str, int]:
    dialogue_id, marker, index = row["target_turn_id"].rpartition("_turn_")
    if not marker or dialogue_id != row["dialogue_id"]:
        raise SystemExit(
            f"Unparseable target_turn_id {row['target_turn_id']!r} for {row['dialogue_id']!r}."
        )
    return dialogue_id, int(index)


def pool_key(row: dict[str, object]) -> tuple[str, int]:
    return str(row["dialogue_id"]), int(row["target_turn_index"])


def passes_target_filter(text: str, question_re: re.Pattern[str], exclusion_re: re.Pattern[str], max_words: int) -> bool:
    stripped = text.strip()
    if question_re.search(stripped) is None:
        return False
    if len(stripped.split()) > max_words:
        return False
    if exclusion_re.search(stripped) is not None:
        return False
    return True


def position_counts(rows: list[dict[str, object]]) -> Counter[str]:
    return Counter(str(row["position"]) for row in rows)


def spacing_ok(ordinals: list[int], min_spacing: int) -> bool:
    for index, left in enumerate(ordinals):
        for right in ordinals[index + 1 :]:
            if abs(left - right) < min_spacing:
                return False
    return True


def any_valid_trio(
    early: list[dict[str, object]],
    middle: list[dict[str, object]],
    late: list[dict[str, object]],
    min_spacing: int,
) -> bool:
    for early_row in early:
        for middle_row in middle:
            early_ord = int(early_row["clinician_ordinal"])
            middle_ord = int(middle_row["clinician_ordinal"])
            if abs(early_ord - middle_ord) < min_spacing:
                continue
            for late_row in late:
                ordinals = [early_ord, middle_ord, int(late_row["clinician_ordinal"])]
                if spacing_ok(ordinals, min_spacing):
                    return True
    return False


def draw_index(rng: np.random.Generator, size: int) -> int:
    if size <= 0:
        raise SystemExit("Cannot draw from an empty target list.")
    return int(rng.integers(0, size))


def select_dialogue(
    dialogue_id: str,
    groups: dict[str, list[dict[str, object]]],
    rng: np.random.Generator,
    min_spacing: int,
) -> list[dict[str, object]]:
    early = groups["Early"]
    middle = groups["Middle"]
    late = groups["Late"]
    if not any_valid_trio(early, middle, late, min_spacing):
        raise SystemExit(
            f"{dialogue_id} has no Early/Middle/Late trio with clinician-turn distance >= {min_spacing}."
        )
    attempts = 0
    while True:
        attempts += 1
        if attempts > 100000:
            raise SystemExit(f"{dialogue_id} did not satisfy MIN_SPACING after {attempts - 1} draws.")
        chosen = [
            early[draw_index(rng, len(early))],
            middle[draw_index(rng, len(middle))],
            late[draw_index(rng, len(late))],
        ]
        ordinals = [int(row["clinician_ordinal"]) for row in chosen]
        if spacing_ok(ordinals, min_spacing):
            return [dict(row) for row in chosen]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def git_commit(project_dir: Path) -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=project_dir,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    commit = result.stdout.strip()
    return commit or None


def median_number(values: list[int]) -> float:
    return float(statistics.median(values))


def format_stat(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return f"{value:g}"


def sort_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return sorted(
        rows,
        key=lambda row: (
            str(row["dialogue_id"]),
            POSITION_RANK[str(row["position"])],
            int(row["target_turn_index"]),
        ),
    )


def non_context_leak(row: dict[str, object], human_text: str, fields: list[str]) -> str | None:
    stripped = human_text.strip()
    if not stripped:
        return "empty human target"
    for field in fields:
        if field == "context":
            continue
        if stripped in str(row[field]):
            return field
    return None


def keys_of(rows: list[dict[str, object]]) -> set[tuple[str, int]]:
    return {pool_key(row) for row in rows}


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    config_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else project_dir / "config.yaml"
    config = load_config(config_path)
    project_dir = config_path.parent

    if int(require(config, "min_gap")) != 1:
        raise SystemExit(f"MIN_GAP must be 1, found {config['min_gap']!r}.")
    pool_name = str(require(config, "sample_pool_filename"))
    if pool_name != "eligible_pool_gap1.csv":
        raise SystemExit(f"Sample pool must be eligible_pool_gap1.csv, found {pool_name}.")
    seed = int(require(config, "seed"))
    min_spacing = int(require(config, "min_spacing"))
    max_words = int(require(config, "max_target_words"))
    pilot_n = int(require(config, "pilot_dialogues"))
    subset_n = int(require(config, "subset_dialogues"))
    question_pattern = str(require(config, "target_question_regex"))
    exclusion_pattern = str(require(config, "target_exclusion_regex"))
    question_re = re.compile(question_pattern)
    exclusion_re = re.compile(exclusion_pattern, re.IGNORECASE)

    pool_path = project_dir / str(require(config, "pool_dir")) / pool_name
    human_path = project_dir / str(require(config, "pool_dir")) / str(require(config, "human_reference_filename"))
    truly_path = Path(str(require(config, "paper1_frozen_csv")))
    earlier_path = Path(str(require(config, "paper1_prereplacement_frozen_csv")))
    characteristics_path = Path(str(require(config, "paper1_characteristics_csv")))
    frozen_dir = project_dir / str(require(config, "frozen_dir"))
    report_path = project_dir / str(require(config, "report_dir")) / str(require(config, "freeze_report_filename"))
    main_path = frozen_dir / str(require(config, "main_frozen_filename"))
    pilot_path = frozen_dir / str(require(config, "pilot_frozen_filename"))
    manifest_path = frozen_dir / str(require(config, "manifest_filename"))

    for path in (pool_path, human_path, truly_path, earlier_path, characteristics_path):
        if not path.is_file():
            raise SystemExit(f"Missing input file: {path}")
    if main_path.exists() or pilot_path.exists() or manifest_path.exists():
        raise SystemExit(f"Freeze outputs already exist in {frozen_dir}. Refusing to overwrite.")

    _pool_fields, pool_rows = read_csv(pool_path)
    _human_fields, human_rows = read_csv(human_path)
    _truly_fields, truly_rows = read_csv(truly_path)
    _earlier_fields, earlier_rows = read_csv(earlier_path)
    _char_fields, characteristic_rows = read_csv(characteristics_path)

    human_by_id = {row["context_id"]: row["human_clinician_target"] for row in human_rows}
    missing_human = [row["context_id"] for row in pool_rows if row["context_id"] not in human_by_id]
    if missing_human:
        raise SystemExit(f"{len(missing_human)} pool rows have no human reference. Sample: {missing_human[:5]}")

    truly_keys = {frozen_key(row) for row in truly_rows}
    earlier_keys = {frozen_key(row) for row in earlier_rows}
    if len(truly_keys) != len(truly_rows) or len(earlier_keys) != len(earlier_rows):
        raise SystemExit("A paper 1 freeze has duplicate (dialogue_id, turn index) keys.")
    rejected_keys = earlier_keys - truly_keys
    either_keys = truly_keys | earlier_keys

    characteristics = {
        (row["dialogue_id"], int(row["turn_index"])): row for row in characteristic_rows
    }
    if len(characteristics) != len(characteristic_rows):
        raise SystemExit("Paper 1 characteristics have duplicate turn keys.")

    strict_rows: list[dict[str, object]] = []
    for row in pool_rows:
        human_text = human_by_id[row["context_id"]]
        if not passes_target_filter(human_text, question_re, exclusion_re, max_words):
            continue
        key = (row["dialogue_id"], int(row["target_turn_index"]))
        if key not in characteristics:
            raise SystemExit(f"No paper 1 characteristics row for {key}.")
        source = characteristics[key]
        if source["context"] != row["context"]:
            raise SystemExit(f"Context mismatch for {key}.")
        if int(source["completed_exchanges_before_target"]) != int(row["n_prior_exchanges"]):
            raise SystemExit(f"Exchange-count mismatch for {key}.")
        if source["position_category"].lower() != row["position"].lower():
            raise SystemExit(f"Position mismatch for {key}.")
        if source["specialty"] != row["specialty"]:
            raise SystemExit(f"Specialty mismatch for {key}.")
        strict_rows.append(
            {
                "context_id": row["context_id"],
                "dialogue_id": row["dialogue_id"],
                "specialty": row["specialty"],
                "target_turn_index": int(row["target_turn_index"]),
                "position": row["position"],
                "normalized_target_position": source["normalized_target_position"],
                "completed_exchanges_before_target": int(source["completed_exchanges_before_target"]),
                "context": row["context"],
                "latest_patient_turn": source["latest_patient_turn"],
                "context_word_count": int(source["context_word_count"]),
                "clinician_ordinal": int(source["doctor_turn_number"]),
                "human_target_for_filter_only": human_text,
            }
        )

    strict_counts = position_counts(strict_rows)
    if len(strict_rows) != sum(EXPECTED_BEFORE_EXCLUSION.values()) or any(
        strict_counts[position] != EXPECTED_BEFORE_EXCLUSION[position] for position in POSITIONS
    ):
        raise SystemExit(
            "Task 2 count before extra exclusion differs from the expected result. "
            f"got total={len(strict_rows)} counts={dict(strict_counts)} "
            f"expected={EXPECTED_BEFORE_EXCLUSION}"
        )

    gap1_removed = [row for row in pool_rows if (row["dialogue_id"], int(row["target_turn_index"])) in either_keys]
    filtered_rows = [row for row in strict_rows if pool_key(row) not in either_keys]
    removed_from_strict = len(strict_rows) - len(filtered_rows)

    by_dialogue: dict[str, dict[str, list[dict[str, object]]]] = defaultdict(
        lambda: {position: [] for position in POSITIONS}
    )
    for row in filtered_rows:
        by_dialogue[str(row["dialogue_id"])][str(row["position"])].append(row)
    for groups in by_dialogue.values():
        for position in POSITIONS:
            groups[position].sort(key=lambda row: int(row["target_turn_index"]))

    all_dialogue_ids = sorted({str(row["dialogue_id"]) for row in pool_rows})
    dropped: list[tuple[str, dict[str, int]]] = []
    kept_dialogue_ids: list[str] = []
    for dialogue_id in all_dialogue_ids:
        counts = {position: len(by_dialogue[dialogue_id][position]) for position in POSITIONS}
        if min(counts.values()) == 0:
            dropped.append((dialogue_id, counts))
        else:
            kept_dialogue_ids.append(dialogue_id)
    if len(kept_dialogue_ids) < MIN_DIALOGUES:
        detail = ", ".join(
            f"{dialogue_id} {counts}" for dialogue_id, counts in dropped
        )
        raise SystemExit(
            f"Only {len(kept_dialogue_ids)} dialogues remain after coverage (minimum {MIN_DIALOGUES}). "
            f"Dropped: {detail}"
        )

    rng = np.random.default_rng(seed)
    main_rows: list[dict[str, object]] = []
    for dialogue_id in kept_dialogue_ids:
        main_rows.extend(select_dialogue(dialogue_id, by_dialogue[dialogue_id], rng, min_spacing))

    if subset_n > len(kept_dialogue_ids):
        raise SystemExit(f"SUBSET_DIALOGUES={subset_n} exceeds kept dialogues {len(kept_dialogue_ids)}.")
    subset_ids = {
        str(dialogue_id)
        for dialogue_id in rng.choice(np.array(kept_dialogue_ids), size=subset_n, replace=False).tolist()
    }
    for row in main_rows:
        row["in_subset"] = 1 if row["dialogue_id"] in subset_ids else 0

    main_keys = keys_of(main_rows)
    main_ordinals: dict[str, list[int]] = defaultdict(list)
    for row in main_rows:
        main_ordinals[str(row["dialogue_id"])].append(int(row["clinician_ordinal"]))

    pilot_groups: dict[str, dict[str, list[dict[str, object]]]] = {}
    for dialogue_id in kept_dialogue_ids:
        groups = {position: [] for position in POSITIONS}
        for position in POSITIONS:
            for row in by_dialogue[dialogue_id][position]:
                if pool_key(row) in main_keys:
                    continue
                ordinal = int(row["clinician_ordinal"])
                if any(abs(ordinal - other) < min_spacing for other in main_ordinals[dialogue_id]):
                    continue
                groups[position].append(row)
        if all(groups[position] for position in POSITIONS):
            pilot_groups[dialogue_id] = groups
    pilot_dialogue_ids = sorted(pilot_groups)
    if len(pilot_dialogue_ids) < pilot_n:
        raise SystemExit(
            f"Only {len(pilot_dialogue_ids)} dialogues can supply a spaced pilot trio "
            f"(need {pilot_n})."
        )
    chosen_pilot = {
        str(dialogue_id)
        for dialogue_id in rng.choice(np.array(pilot_dialogue_ids), size=pilot_n, replace=False).tolist()
    }
    pilot_rows: list[dict[str, object]] = []
    for dialogue_id in sorted(chosen_pilot):
        groups = pilot_groups[dialogue_id]
        for position in POSITIONS:
            options = groups[position]
            pilot_rows.append(dict(options[draw_index(rng, len(options))]))

    main_rows = sort_rows(main_rows)
    pilot_rows = sort_rows(pilot_rows)

    checks: list[tuple[str, bool, str]] = []

    def add_check(name: str, passed: bool, detail: str) -> None:
        checks.append((name, passed, detail))
        if not passed:
            rendered = "\n".join(
                f"{'PASS' if ok else 'FAIL'} {label}: {text}" for label, ok, text in checks
            )
            raise SystemExit(rendered)

    shared_truly = keys_of(main_rows + pilot_rows) & truly_keys
    shared_earlier = keys_of(main_rows + pilot_rows) & earlier_keys
    add_check(
        "shared with final_1500_TRULY_FROZEN.csv",
        len(shared_truly) == 0,
        f"shared={len(shared_truly)}",
    )
    add_check(
        "shared with final_1500_FROZEN.csv",
        len(shared_earlier) == 0,
        f"shared={len(shared_earlier)}",
    )

    per_dialogue = Counter(str(row["dialogue_id"]) for row in main_rows)
    per_dialogue_position = Counter((str(row["dialogue_id"]), str(row["position"])) for row in main_rows)
    add_check(
        "main sample shape",
        len(main_rows) == 3 * len(kept_dialogue_ids)
        and set(per_dialogue.values()) == {3}
        and all(per_dialogue_position[(dialogue_id, position)] == 1 for dialogue_id in kept_dialogue_ids for position in POSITIONS)
        and len(main_keys) == len(main_rows)
        and len({row["context_id"] for row in main_rows}) == len(main_rows),
        f"rows={len(main_rows)} dialogues={len(kept_dialogue_ids)} unique_targets={len(main_keys)}",
    )
    add_check(
        "pilot and main share no targets",
        len(keys_of(pilot_rows) & main_keys) == 0,
        f"shared={len(keys_of(pilot_rows) & main_keys)} pilot_rows={len(pilot_rows)}",
    )
    subset_row_count = sum(int(row["in_subset"]) for row in main_rows)
    subset_dialogues = {str(row["dialogue_id"]) for row in main_rows if int(row["in_subset"]) == 1}
    add_check(
        "subset size",
        subset_row_count == 3 * subset_n and len(subset_dialogues) == subset_n,
        f"rows={subset_row_count} dialogues={len(subset_dialogues)}",
    )

    leaks: list[str] = []
    for label, rows, fields in (
        ("main", main_rows, MAIN_FIELDS),
        ("pilot", pilot_rows, PILOT_FIELDS),
    ):
        for row in rows:
            hit = non_context_leak(row, str(row["human_target_for_filter_only"]), fields)
            if hit is not None:
                leaks.append(f"{label} {row['context_id']} in {hit}")
    add_check("human target absent outside context", not leaks, "none" if not leaks else "; ".join(leaks[:8]))

    for row in main_rows + pilot_rows:
        ordinals = [int(item["clinician_ordinal"]) for item in main_rows if item["dialogue_id"] == row["dialogue_id"]]
        if row in main_rows:
            if not spacing_ok(ordinals, min_spacing):
                raise SystemExit(f"Main spacing failed for {row['dialogue_id']}.")
        else:
            if any(abs(int(row["clinician_ordinal"]) - other) < min_spacing for other in ordinals):
                raise SystemExit(f"Pilot spacing failed for {row['context_id']}.")

    frozen_dir.mkdir(parents=True, exist_ok=True)
    write_csv(main_path, MAIN_FIELDS, main_rows)
    write_csv(pilot_path, PILOT_FIELDS, pilot_rows)

    main_text = main_path.read_text(encoding="utf-8")
    pilot_text = pilot_path.read_text(encoding="utf-8")
    if "human_clinician_target" in main_text.splitlines()[0] or "human_clinician_target" in pilot_text.splitlines()[0]:
        main_path.unlink()
        pilot_path.unlink()
        raise SystemExit("Human target column was written.")
    disk_leaks = []
    for label, text, rows in (("main", main_text, main_rows), ("pilot", pilot_text, pilot_rows)):
        for row in rows:
            target = str(row["human_target_for_filter_only"]).strip()
            without_context = text
            # The context column is allowed to contain an earlier identical question.
            # Rebuild the non-context record and require the target to be absent there.
            record = {field: row[field] for field in (MAIN_FIELDS if label == "main" else PILOT_FIELDS) if field != "context"}
            blob = "\n".join(str(value) for value in record.values())
            if target and target in blob:
                disk_leaks.append(f"{label} {row['context_id']}")
    if disk_leaks:
        main_path.unlink()
        pilot_path.unlink()
        raise SystemExit("Human target text leaked outside context: " + ", ".join(disk_leaks[:8]))

    created_at = datetime.now().astimezone().isoformat(timespec="seconds")
    manifest = {
        "created_at": created_at,
        "git_commit": git_commit(project_dir),
        "numpy_version": np.__version__,
        "seed": seed,
        "parameters": {
            "min_gap": 1,
            "sample_pool": pool_name,
            "min_spacing": min_spacing,
            "max_target_words": max_words,
            "pilot_dialogues": pilot_n,
            "subset_dialogues": subset_n,
            "kept_dialogues": len(kept_dialogue_ids),
            "dropped_dialogues": [dialogue_id for dialogue_id, _counts in dropped],
        },
        "filter_regexes": {
            "target_question_regex": question_pattern,
            "target_exclusion_regex": exclusion_pattern,
            "target_exclusion_flags": "IGNORECASE",
            "max_target_words": "whitespace-separated words after strip",
        },
        "row_counts": {
            "gap1_pool": len(pool_rows),
            "strict_filter_before_exclusion": len(strict_rows),
            "gap1_rows_in_either_paper1_freeze": len(gap1_removed),
            "strict_rows_removed_by_either_freeze": removed_from_strict,
            "filtered_after_exclusion": len(filtered_rows),
            "main_sample": len(main_rows),
            "pilot": len(pilot_rows),
            "subset_rows": subset_row_count,
            "subset_dialogues": len(subset_dialogues),
        },
        "sha256": {
            main_path.name: sha256(main_path),
            pilot_path.name: sha256(pilot_path),
        },
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    main_position = position_counts(main_rows)
    specialty_table: dict[str, Counter[str]] = defaultdict(Counter)
    for row in main_rows:
        specialty_table[str(row["specialty"])][str(row["position"])] += 1
    specialties = [name for name in SPECIALTY_ORDER if name in specialty_table]
    specialties.extend(sorted(set(specialty_table) - set(specialties)))

    lines = [
        "# Persona study freeze report",
        "",
        "No model output was generated.",
        "",
        "## Task 1. Extra exclusion",
        "",
        f"- Earlier freeze: `{earlier_path}`",
        f"- Truly frozen file: `{truly_path}`",
        f"- Rows in `final_1500_FROZEN.csv` but not in `final_1500_TRULY_FROZEN.csv`: **{len(rejected_keys)}**.",
        f"- Estimated error rate of the original eligibility rule: **{len(rejected_keys)} / 1500 = {len(rejected_keys) / 1500:.4f}**.",
        f"- Gap-1 pool rows that appear in either frozen file: **{len(gap1_removed)}** removed from the gap-1 pool.",
        f"- Of the {len(strict_rows)} targets that pass the strict filter, **{removed_from_strict}** are in either frozen file and are removed.",
        "",
        "## Task 2. Strict target filter",
        "",
        "The human target is used only to decide eligibility. It is not written to the frozen files.",
        "",
        f"- Gap-1 pool before the strict filter: **{len(pool_rows)}**.",
        "- Before removing either paper 1 freeze, targets kept: "
        f"**{len(strict_rows)}** "
        f"(Early {strict_counts['Early']}, Middle {strict_counts['Middle']}, Late {strict_counts['Late']}). "
        "This matches the expected 7237 (Early 2349, Middle 2646, Late 2242).",
        f"- After removing targets that appear in either freeze: **{len(filtered_rows)}** "
        f"(Early {position_counts(filtered_rows)['Early']}, "
        f"Middle {position_counts(filtered_rows)['Middle']}, "
        f"Late {position_counts(filtered_rows)['Late']}).",
        "",
        "A kept target ends with `?` (trailing whitespace or quotes allowed), has at most "
        f"{max_words} whitespace-separated words, and does not match the closing/exclusion regex.",
        "",
        "## Task 3. Coverage",
        "",
        f"- Dialogues dropped because a position was empty: **{len(dropped)}**.",
        f"- Dialogues kept: **{len(kept_dialogue_ids)}**.",
        "",
    ]
    if dropped:
        lines.append("| Dialogue | Early | Middle | Late |")
        lines.append("| --- | ---: | ---: | ---: |")
        for dialogue_id, counts in dropped:
            lines.append(
                f"| {dialogue_id} | {counts['Early']} | {counts['Middle']} | {counts['Late']} |"
            )
        lines.append("")
    lines.extend(
        [
            f"- Final main-sample N: **{len(main_rows)}** ({len(kept_dialogue_ids)} dialogues x 3).",
            f"- Counts per position: Early {main_position['Early']}, Middle {main_position['Middle']}, Late {main_position['Late']}.",
            "",
            "## Position by specialty",
            "",
            "| Specialty | Early | Middle | Late | Total |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for specialty in specialties:
        counts = specialty_table[specialty]
        total = sum(counts[position] for position in POSITIONS)
        lines.append(
            f"| {specialty} | {counts['Early']} | {counts['Middle']} | {counts['Late']} | {total} |"
        )
    lines.extend(
        [
            "",
            "## Distributions by position",
            "",
            "`context_word_count` is the paper 1 token count joined from the characteristics file. "
            "`completed_exchanges_before_target` is the patient-turn count before the target.",
            "",
            "| Measure | Position | Min | Median | Max |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
    )
    for measure in ("context_word_count", "completed_exchanges_before_target"):
        for position in POSITIONS:
            values = [int(row[measure]) for row in main_rows if row["position"] == position]
            lines.append(
                f"| {measure} | {position} | {min(values)} | {format_stat(median_number(values))} | {max(values)} |"
            )
    lines.extend(
        [
            "",
            "## Checks",
            "",
        ]
    )
    for name, _passed, detail in checks:
        lines.append(f"- PASS: {name} ({detail}).")
    lines.append(
        "- PASS: human target text is not a frozen column and does not appear in any output field other than `context`."
    )
    lines.extend(
        [
            "",
            "Clinician-turn distance is the absolute difference of paper 1 `doctor_turn_number` values, "
            f"the 1-based ordinal of every clinician turn. Selected targets in a dialogue must be at least {min_spacing} apart. "
            "Pilot targets are also at least that far from the main-sample targets in the same dialogue.",
            "",
            f"Pilot rows: **{len(pilot_rows)}** from {pilot_n} dialogues. "
            f"Subset rows: **{subset_row_count}** from {subset_n} dialogues.",
            "",
            "## Manifest",
            "",
            "```json",
            json.dumps(manifest, indent=2),
            "```",
            "",
        ]
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")

    os.chmod(main_path, 0o444)
    os.chmod(pilot_path, 0o444)
    print(f"Main sample: {len(main_rows)} rows, {len(kept_dialogue_ids)} dialogues")
    print(f"Subset: {subset_row_count} rows")
    print(f"Pilot: {len(pilot_rows)} rows")
    print(f"Wrote {main_path}")
    print(f"Wrote {pilot_path}")
    print(f"Wrote {manifest_path}")
    print(f"Wrote {report_path}")


if __name__ == "__main__":
    main()
