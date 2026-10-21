#!/usr/bin/env python3
"""Build persona-study pools that do not reuse paper 1 target turns.

Eligibility and position rules are copied from the paper 1 scripts:
parse_candidate_turns.py, analyze_candidate_turns_v3.py, and
sample_final_1500_v2.eligible_rows. This file does not import that project.
"""

from __future__ import annotations

import csv
import re
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import turn_rules_v3 as rules  # noqa: E402

SPEAKER_LINE = re.compile(
    r"^(?P<speaker>DL|[DP])[\s;:.\u201c\"\u201d\u2018\u2019-]*\s*(?P<text>.*)$",
    re.IGNORECASE,
)
TURN_ID_RE = re.compile(r"^(?P<dialogue_id>.+)_turn_(?P<index>\d+)$")

SPECIALTY_BY_PREFIX = {
    "CAR": "Cardiovascular",
    "DER": "Dermatological",
    "GAS": "Gastrointestinal",
    "GEN": "General",
    "MSK": "Musculoskeletal",
    "RES": "Respiratory",
}

POOL_FIELDS = [
    "context_id",
    "dialogue_id",
    "target_turn_index",
    "position",
    "n_prior_exchanges",
    "specialty",
    "context",
]
HUMAN_FIELDS = [
    "context_id",
    "dialogue_id",
    "target_turn_index",
    "human_clinician_target",
]
POSITION_DISPLAY = {"early": "Early", "middle": "Middle", "late": "Late"}


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


def read_transcript(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16"), "utf-16-bom"
    if b"\x00" in raw[:100]:
        for encoding in ("utf-16-le", "utf-16-be"):
            try:
                return raw.decode(encoding), encoding
            except UnicodeDecodeError:
                continue
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("unknown", b"", 0, 1, f"Could not decode {path.name}")


def normalize_speaker(raw_speaker: str) -> str:
    speaker = raw_speaker.upper()
    if speaker == "DL":
        return "D"
    return speaker


def parse_transcript(text: str) -> tuple[list[tuple[str, str, int]], Counter[str]]:
    """Return (speaker, text, source_line) turns and parse counters.

    Turn assembly matches parse_candidate_turns.py: a non-speaker line is
    appended to the previous turn. DL is stored as D.
    """
    turns: list[tuple[str, str, int]] = []
    stats: Counter[str] = Counter()
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            stats["blank_lines"] += 1
            continue
        match = SPEAKER_LINE.match(stripped)
        if match:
            raw_speaker = match.group("speaker").upper()
            stats[f"prefix_{raw_speaker}"] += 1
            speaker = normalize_speaker(raw_speaker)
            utterance = match.group("text").strip()
            turns.append((speaker, utterance, line_number))
            continue
        stats["continuation_lines"] += 1
        if not turns:
            stats["orphan_continuation_lines"] += 1
            continue
        speaker, previous, source_line = turns[-1]
        turns[-1] = (speaker, f"{previous} {stripped}".strip(), source_line)
    return turns, stats


def format_context(turns: list[tuple[str, str, int]]) -> str:
    blocks = []
    for speaker, text, _source_line in turns:
        label = "Doctor" if speaker == "D" else "Patient"
        blocks.append(f"{label}: {text}")
    return "\n\n".join(blocks)


def position_third(normalized_position: float) -> str:
    """Paper 1 boundary: <= 1/3 early, <= 2/3 middle, else late."""
    if normalized_position <= 1 / 3:
        return "early"
    if normalized_position <= 2 / 3:
        return "middle"
    return "late"


def specialty_for_dialogue(dialogue_id: str) -> str:
    prefix = re.match(r"^[A-Z]+", dialogue_id)
    if not prefix:
        return "Unknown"
    return SPECIALTY_BY_PREFIX.get(prefix.group(0), "Unknown")


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


def paper1_targets(rows: list[dict[str, str]]) -> list[tuple[str, int]]:
    parsed: list[tuple[str, int]] = []
    for row in rows:
        match = TURN_ID_RE.match(row["target_turn_id"])
        if match is None or match.group("dialogue_id") != row["dialogue_id"]:
            raise SystemExit(
                "Paper 1 target_turn_id does not encode dialogue_id plus turn index: "
                f"{row['dialogue_id']} / {row['target_turn_id']}"
            )
        parsed.append((row["dialogue_id"], int(match.group("index"))))
    if len(parsed) != len(set(parsed)):
        raise SystemExit("Paper 1 frozen file has duplicate (dialogue_id, target_turn_index) pairs.")
    return parsed


def is_eligible(primary_function: str, n_prior_exchanges: int, minimum: int) -> bool:
    return (
        primary_function == "history_information_seeking"
        and n_prior_exchanges >= minimum
    )


def near_paper1(
    dialogue_id: str,
    doctor_ordinal: int,
    paper_ordinals: dict[str, set[int]],
    gap: int,
) -> bool:
    return any(
        abs(doctor_ordinal - other) <= gap
        for other in paper_ordinals.get(dialogue_id, ())
    )


def load_dialogues(transcript_dir: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    files = sorted(transcript_dir.glob("*.txt"))
    if not files:
        raise SystemExit(f"No .txt dialogues in {transcript_dir}")

    candidates: list[dict[str, object]] = []
    turn_counts: list[int] = []
    encodings: Counter[str] = Counter()
    parse_stats: Counter[str] = Counter()
    unknown_specialties: list[str] = []
    dialogue_ids: list[str] = []
    doctor_ordinal_by_turn: dict[tuple[str, int], int] = {}

    for file_index, path in enumerate(files, start=1):
        dialogue_id = path.stem
        dialogue_ids.append(dialogue_id)
        specialty = specialty_for_dialogue(dialogue_id)
        if specialty == "Unknown":
            unknown_specialties.append(dialogue_id)
        text, encoding = read_transcript(path)
        encodings[encoding] += 1
        turns, file_stats = parse_transcript(text)
        parse_stats.update(file_stats)
        turn_counts.append(len(turns))

        doctor_ordinal = 0
        for index, (speaker, _text, _line) in enumerate(turns):
            if speaker == "D":
                doctor_ordinal += 1
                doctor_ordinal_by_turn[(dialogue_id, index + 1)] = doctor_ordinal

        doctor_turn_indices = [index for index, turn in enumerate(turns) if turn[0] == "D"]
        candidate_indices = [
            index
            for index in doctor_turn_indices
            if index > 0 and turns[index - 1][0] == "P"
        ]
        candidate_count = len(candidate_indices)
        for candidate_number, turn_index in enumerate(candidate_indices, start=1):
            normalized = candidate_number / candidate_count
            third = position_third(normalized)
            context_turns = turns[:turn_index]
            n_prior_exchanges = sum(1 for turn in context_turns if turn[0] == "P")
            target_speaker, target_text, source_line = turns[turn_index]
            if target_speaker != "D":
                raise SystemExit(f"{dialogue_id} target at {turn_index + 1} is not a clinician turn.")
            primary_function, _reason, _summary = rules.classify_primary_turn_function(target_text)
            candidates.append(
                {
                    "dialogue_id": dialogue_id,
                    "specialty": specialty,
                    "target_turn_index": turn_index + 1,
                    "source_line": source_line,
                    "context": format_context(context_turns),
                    "human_clinician_target": target_text,
                    "n_prior_exchanges": n_prior_exchanges,
                    "position_code": third,
                    "position": POSITION_DISPLAY[third],
                    "normalized_position": round(normalized, 6),
                    "primary_turn_function": primary_function,
                    "doctor_ordinal": doctor_ordinal_by_turn[(dialogue_id, turn_index + 1)],
                    "candidate_number": candidate_number,
                    "candidate_count": candidate_count,
                }
            )
        if file_index % 40 == 0 or file_index == len(files):
            print(f"Parsed {file_index}/{len(files)} dialogues, {len(candidates)} candidate turns.")

    summary = {
        "dialogue_ids": dialogue_ids,
        "turn_counts": turn_counts,
        "encodings": encodings,
        "parse_stats": parse_stats,
        "unknown_specialties": unknown_specialties,
        "doctor_ordinal_by_turn": doctor_ordinal_by_turn,
        "file_count": len(files),
    }
    return candidates, summary


def verify_against_paper1_characteristics(
    candidates: list[dict[str, object]], characteristics_path: Path
) -> None:
    _fields, rows = read_csv(characteristics_path)
    by_key = {
        (row["dialogue_id"], int(row["turn_index"])): row
        for row in rows
    }
    if len(by_key) != len(rows):
        raise SystemExit("Paper 1 characteristics file has duplicate turn keys.")
    ours = {(row["dialogue_id"], int(row["target_turn_index"])): row for row in candidates}
    missing = sorted(set(by_key) - set(ours))
    extra = sorted(set(ours) - set(by_key))
    if missing or extra or len(candidates) != len(rows):
        raise SystemExit(
            "Candidate-turn set does not match paper 1 characteristics. "
            f"ours={len(candidates)} paper1={len(rows)} missing={len(missing)} extra={len(extra)} "
            f"missing_sample={missing[:5]} extra_sample={extra[:5]}"
        )
    mismatches: list[str] = []
    for key, paper_row in by_key.items():
        ours_row = ours[key]
        checks = {
            "primary_turn_function": (
                str(ours_row["primary_turn_function"]),
                paper_row["primary_turn_function"],
            ),
            "n_prior_exchanges": (
                str(ours_row["n_prior_exchanges"]),
                paper_row["completed_exchanges_before_target"],
            ),
            "position_code": (
                str(ours_row["position_code"]),
                paper_row["position_category"],
            ),
            "specialty": (str(ours_row["specialty"]), paper_row["specialty"]),
            "normalized_position": (
                f"{float(ours_row['normalized_position']):.6f}",
                f"{float(paper_row['target_position']):.6f}",
            ),
            "context": (str(ours_row["context"]), paper_row["context"]),
            "human_clinician_target": (
                str(ours_row["human_clinician_target"]),
                paper_row["human_doctor_target"],
            ),
        }
        for field, (left, right) in checks.items():
            if left != right:
                mismatches.append(f"{key} {field}: ours={left!r} paper1={right!r}")
                if len(mismatches) >= 8:
                    break
        if len(mismatches) >= 8:
            break
    if mismatches:
        detail = "\n".join(mismatches)
        raise SystemExit(
            "Reimplemented rules do not match candidate_characteristics_v3.csv:\n" + detail
        )
    print(f"Rule copy matches paper 1 characteristics on all {len(candidates)} candidate turns.")


def assign_ids(rows: list[dict[str, object]], prefix: str) -> None:
    ordered = sorted(rows, key=lambda row: (str(row["dialogue_id"]), int(row["target_turn_index"])))
    if ordered is not rows:
        rows[:] = ordered
    width = max(6, len(str(len(rows))))
    for index, row in enumerate(rows, start=1):
        row["context_id"] = f"{prefix}{index:0{width}d}"


def at_least_counts(rows: list[dict[str, object]], dialogue_ids: list[str]) -> dict[int, int]:
    per_dialogue = Counter(str(row["dialogue_id"]) for row in rows)
    return {
        threshold: sum(1 for dialogue_id in dialogue_ids if per_dialogue[dialogue_id] >= threshold)
        for threshold in (1, 2, 3, 4)
    }


def position_per_dialogue(
    rows: list[dict[str, object]], dialogue_ids: list[str]
) -> dict[str, tuple[float, float, float]]:
    counts: dict[str, Counter[str]] = {dialogue_id: Counter() for dialogue_id in dialogue_ids}
    for row in rows:
        counts[str(row["dialogue_id"])][str(row["position"])] += 1
    summary: dict[str, tuple[float, float, float]] = {}
    for position in ("Early", "Middle", "Late"):
        values = [counts[dialogue_id][position] for dialogue_id in dialogue_ids]
        summary[position] = (min(values), statistics.median(values), max(values))
    return summary


def histogram(values: list[int], start: int, width: int) -> list[tuple[str, int]]:
    if not values:
        return []
    end = max(values)
    bins: list[tuple[str, int]] = []
    low = start
    while low <= end:
        high = low + width - 1
        count = sum(1 for value in values if low <= value <= high)
        bins.append((f"{low}-{high}", count))
        low += width
    return bins


def write_report(
    path: Path,
    inspection: dict[str, object],
    frozen_fieldnames: list[str],
    frozen_position_counts: Counter[str],
    frozen_row_count: int,
    eligible_count: int,
    pools: dict[int, list[dict[str, object]]],
    dialogue_ids: list[str],
    checker_output: str,
    characteristics_matched: int,
) -> None:
    turn_counts = inspection["turn_counts"]
    assert isinstance(turn_counts, list)
    encodings = inspection["encodings"]
    parse_stats = inspection["parse_stats"]
    assert isinstance(encodings, Counter)
    assert isinstance(parse_stats, Counter)
    bins = histogram(turn_counts, start=40, width=10)

    lines = [
        "# Persona study eligible-pool audit",
        "",
        "This step builds the pool of eligible clinician target turns and removes paper 1 targets.",
        "It does not sample or freeze a dataset.",
        "",
        "## Task 1. Inspection",
        "",
        "### Dialogues",
        "",
        f"- Path: `{inspection['transcript_dir']}`",
        "- Format: one plain-text file per dialogue. A turn is a line whose first token is a speaker prefix. Non-empty lines that do not start with a speaker prefix are continuations and are merged into the previous turn.",
        f"- Dialogue files: **{inspection['file_count']}** `.txt` files.",
        f"- Encodings: {', '.join(f'{name}={count}' for name, count in sorted(encodings.items()))}.",
        "- Speaker prefixes, before normalisation: "
        + ", ".join(
            f"`{name.removeprefix('prefix_')}`={parse_stats[name]}"
            for name in sorted(parse_stats)
            if name.startswith("prefix_")
        )
        + ".",
        "- `DL` is normalised to the clinician, matching paper 1. Stored speaker labels in the context text are `Doctor` and `Patient`.",
        f"- Parsed turns: **{sum(turn_counts)}**. Clinician turns (`D`, including `DL`): **{parse_stats['prefix_D'] + parse_stats['prefix_DL']}**. Patient turns: **{parse_stats['prefix_P']}**.",
        f"- Continuation lines merged into the previous turn: **{parse_stats['continuation_lines']}**. Continuations before any speaker: **{parse_stats['orphan_continuation_lines']}**.",
        "",
        "Turns per dialogue:",
        "",
        f"- Min / median / mean / max: **{min(turn_counts)} / {statistics.median(turn_counts)} / {statistics.mean(turn_counts):.2f} / {max(turn_counts)}**.",
        "",
        "| Turns per dialogue | Dialogues |",
        "| --- | ---: |",
    ]
    for label, count in bins:
        lines.append(f"| {label} | {count} |")

    lines.extend(
        [
            "",
            "### Paper 1 frozen file",
            "",
            f"- Path: `{inspection['frozen_csv']}`",
            f"- Rows: **{frozen_row_count}**.",
            "- Columns: " + ", ".join(f"`{name}`" for name in frozen_fieldnames) + ".",
            "- There is no column named `target_turn_index`. The turn is identified by `dialogue_id` plus `target_turn_id`.",
            "- `target_turn_id` has the form `{dialogue_id}_turn_{index}` where `index` is the 1-based index of the target in the parsed turn list (all speakers). Example: `CAR0001_turn_0019` is dialogue `CAR0001`, turn 19.",
            "- Position is the column `position_category`, stored in lowercase: "
            + ", ".join(f"`{name}`={count}" for name, count in sorted(frozen_position_counts.items()))
            + ".",
            "",
            "### How paper 1 defined eligibility and position",
            "",
            "The frozen file was written by `finalize_truly_frozen_sample.py`. That script keeps the sample produced by `sample_final_1500_v2.py` and replaces manually reviewed non-history targets. The eligible-turn rule itself is `sample_final_1500_v2.eligible_rows`, applied to rows built by `parse_candidate_turns.py` and classified by `analyze_candidate_turns_v3.py`.",
            "",
            "An eligible target turn must satisfy both of the following:",
            "",
            "1. It is a candidate clinician turn. The parsed turn speaker is the clinician (`D`, or `DL` normalised to `D`), the turn is not the first turn of the dialogue, and the immediately previous turn is the patient (`P`).",
            "2. `primary_turn_function == history_information_seeking` and `completed_exchanges_before_target >= 2`.",
            "",
            "`completed_exchanges_before_target` is the number of patient turns in the context, which is every turn before the target. It is not a separate pairing rule beyond that count.",
            "",
            "`history_information_seeking` is the dominant sentence class from `analyze_candidate_turns_v3.py`, not the broader information-seeking flag from v2. The target is split into sentences. Each sentence is classified in this order: acknowledgement, incidental closing question, administrative, examination, diagnosis, treatment, conversational transition, closing, greeting, history-information-seeking, otherwise other. Brief acknowledgements are dropped, and the remaining sentence with the highest precedence wins. Precedence is examination, diagnosis, treatment, administrative, closing, transition, greeting, history-information-seeking, other. A history sentence is one that is not an incidental closing question or a clinician recap, and that matches a medication-history pattern, a social-history pattern, the v2 information-seeking regular expressions, or the v2 spaCy information-seeking rules.",
            "",
            "Position is assigned before the eligibility filter, across candidate clinician turns in that dialogue (clinician turns immediately preceded by a patient turn). `normalized = candidate_number / candidate_count`, with `candidate_number` starting at 1. Early if `normalized <= 1/3`, Middle if `normalized <= 2/3`, otherwise Late. A value exactly on 1/3 is Early, and a value exactly on 2/3 is Middle. Paper 1 stores these as `early`, `middle`, and `late`.",
            "",
            f"The copied rules were checked against `{inspection['characteristics_csv']}`. All **{characteristics_matched}** candidate turns matched on function, exchange count, position, specialty, normalized position, context text, and human target text.",
            "",
            "## Task 2. Eligible pool",
            "",
            f"- Candidate clinician turns: **{inspection['candidate_count']}**.",
            f"- Eligible before removing paper 1 targets: **{eligible_count}**.",
            "- `MIN_GAP = k` removes every remaining eligible target whose clinician-turn distance to any paper 1 target in the same dialogue is `<= k`. Distance is the absolute difference of 1-based clinician-turn ordinals. Those ordinals count every clinician turn, including turns that are not eligible. `MIN_GAP = 0` removes only the paper 1 targets themselves.",
            "- Pool position labels are `Early`, `Middle`, and `Late`.",
            "- `specialty` is the dialogue prefix used by paper 1 (`CAR`, `DER`, `GAS`, `GEN`, `MSK`, `RES`). The transcripts have no separate case-category field.",
            "- `context` is every turn before the target, labeled `Doctor` or `Patient`, separated by a blank line. The human target utterance is only in `human_reference_not_for_analysis.csv`.",
            "- `context_id` values are assigned on the `MIN_GAP = 0` pool, sorted by dialogue id and turn index, and reused in the other pools.",
            "",
            "### Pool size by position",
            "",
            "| MIN_GAP | Early | Middle | Late | Total |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for gap, rows in pools.items():
        counts = Counter(str(row["position"]) for row in rows)
        lines.append(
            f"| {gap} | {counts['Early']} | {counts['Middle']} | {counts['Late']} | {len(rows)} |"
        )

    lines.extend(
        [
            "",
            "### Dialogues that still have at least this many eligible targets",
            "",
            "Denominator is all parsed dialogues.",
            "",
            "| MIN_GAP | >= 1 | >= 2 | >= 3 | >= 4 |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for gap, rows in pools.items():
        counts = at_least_counts(rows, dialogue_ids)
        lines.append(
            f"| {gap} | {counts[1]} | {counts[2]} | {counts[3]} | {counts[4]} |"
        )

    lines.extend(
        [
            "",
            "### Eligible targets per position per dialogue",
            "",
            "Min, median, and max are taken over every parsed dialogue. A dialogue with no remaining target in that position contributes 0.",
            "",
            "| MIN_GAP | Position | Min | Median | Max |",
            "| ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for gap, rows in pools.items():
        summary = position_per_dialogue(rows, dialogue_ids)
        for position in ("Early", "Middle", "Late"):
            low, middle, high = summary[position]
            lines.append(f"| {gap} | {position} | {low:g} | {middle:g} | {high:g} |")

    lines.extend(
        [
            "",
            "## Task 3. Overlap check",
            "",
            "```",
            checker_output.rstrip(),
            "```",
            "",
            "## Assumptions and problems",
            "",
            "- Paper 1 has no `target_turn_index` column. The index is the integer in `target_turn_id`, and the same 1-based parsed-turn index is stored in the new pools.",
            "- The copy of the frozen file in this project folder, `final_1500_FROZEN.csv`, is the earlier freeze from before manual replacement. Exclusion uses `final_1500_TRULY_FROZEN.csv`, which is the file paper 1 generation used. The 272 transcript files in this folder are byte-identical to the transcript files that paper 1 parsed.",
            "- Clinician-turn distance counts every clinician turn. A paper 1 target that is the 10th clinician turn excludes the 9th and 11th clinician turns when `MIN_GAP = 1`, whether or not those neighbours are themselves history-information-seeking.",
            "- Manually excluded paper 1 rows that were replaced are not in `final_1500_TRULY_FROZEN.csv`. If they still pass the automatic eligibility rule, they remain in this pool. Their replacements are in the frozen file and are removed.",
            "- No separate case category is stored in the transcripts. `specialty` is included because paper 1 derived it from the dialogue-id prefix.",
            "- The linguistic classifier is a local copy in `turn_rules_v2.py` and `turn_rules_v3.py`, including the spaCy `en_core_web_sm` checks. It was not imported from the paper 1 folder.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    config_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else project_dir / "config.yaml"
    config = load_config(config_path)
    project_dir = config_path.parent

    transcript_dir = Path(str(require(config, "osce_dialogues_path")))
    frozen_path = Path(str(require(config, "paper1_frozen_csv")))
    characteristics_path = Path(str(require(config, "paper1_characteristics_csv")))
    minimum = int(require(config, "min_completed_exchanges"))
    gaps = require(config, "min_gaps")
    if not isinstance(gaps, list) or [int(gap) for gap in gaps] != [0, 1, 2]:
        raise SystemExit(f"This step expects min_gaps [0, 1, 2], found {gaps!r}.")
    prefix = str(require(config, "context_id_prefix"))
    pool_dir = project_dir / str(require(config, "pool_dir"))
    report_dir = project_dir / str(require(config, "report_dir"))
    pool_names = require(config, "pool_filenames")
    if not isinstance(pool_names, list) or len(pool_names) != 3:
        raise SystemExit("pool_filenames must list the three gap files.")
    pool_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    print("Loading dialogues and classifying candidate turns.")
    candidates, summary = load_dialogues(transcript_dir)
    summary["transcript_dir"] = str(transcript_dir)
    summary["frozen_csv"] = str(frozen_path)
    summary["characteristics_csv"] = str(characteristics_path)
    summary["candidate_count"] = len(candidates)
    verify_against_paper1_characteristics(candidates, characteristics_path)

    eligible = [
        row
        for row in candidates
        if is_eligible(str(row["primary_turn_function"]), int(row["n_prior_exchanges"]), minimum)
    ]
    print(f"Eligible targets before paper 1 removal: {len(eligible)}")

    frozen_fields, frozen_rows = read_csv(frozen_path)
    frozen_keys = set(paper1_targets(frozen_rows))
    eligible_keys = {(str(row["dialogue_id"]), int(row["target_turn_index"])) for row in eligible}
    missing_frozen = sorted(frozen_keys - eligible_keys)
    if missing_frozen:
        raise SystemExit(
            "Some paper 1 frozen targets are not eligible under the copied rules. "
            f"count={len(missing_frozen)} sample={missing_frozen[:8]}"
        )

    paper_ordinals: dict[str, set[int]] = defaultdict(set)
    ordinal_lookup = summary["doctor_ordinal_by_turn"]
    assert isinstance(ordinal_lookup, dict)
    for dialogue_id, turn_index in frozen_keys:
        key = (dialogue_id, turn_index)
        if key not in ordinal_lookup:
            raise SystemExit(f"Paper 1 target {dialogue_id} turn {turn_index} is not a clinician turn.")
        paper_ordinals[dialogue_id].add(int(ordinal_lookup[key]))

    dialogue_ids = summary["dialogue_ids"]
    assert isinstance(dialogue_ids, list)
    pools: dict[int, list[dict[str, object]]] = {}
    for gap in (0, 1, 2):
        kept = [
            row
            for row in eligible
            if not near_paper1(str(row["dialogue_id"]), int(row["doctor_ordinal"]), paper_ordinals, gap)
        ]
        pools[gap] = kept
        print(f"MIN_GAP={gap}: {len(kept)} targets")

    assign_ids(pools[0], prefix)
    ids_by_turn = {
        (str(row["dialogue_id"]), int(row["target_turn_index"])): str(row["context_id"])
        for row in pools[0]
    }
    for gap in (1, 2):
        for row in pools[gap]:
            row["context_id"] = ids_by_turn[(str(row["dialogue_id"]), int(row["target_turn_index"]))]
        pools[gap].sort(key=lambda row: str(row["context_id"]))

    gap0_ids = {str(row["context_id"]) for row in pools[0]}
    for gap in (1, 2):
        if not {str(row["context_id"]) for row in pools[gap]} <= gap0_ids:
            raise SystemExit(f"MIN_GAP={gap} is not a subset of MIN_GAP=0.")

    for gap, filename in zip((0, 1, 2), pool_names):
        destination = pool_dir / str(filename)
        write_csv(destination, POOL_FIELDS, pools[gap])
        print(f"Wrote {destination}")

    human_rows = [
        {
            "context_id": row["context_id"],
            "dialogue_id": row["dialogue_id"],
            "target_turn_index": row["target_turn_index"],
            "human_clinician_target": row["human_clinician_target"],
        }
        for row in pools[0]
    ]
    human_path = pool_dir / str(require(config, "human_reference_filename"))
    write_csv(human_path, HUMAN_FIELDS, human_rows)
    print(f"Wrote {human_path}")

    checker = subprocess.run(
        [sys.executable, str(SRC_DIR / "check_overlap.py"), str(config_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    checker_output = (checker.stdout or "") + (checker.stderr or "")
    print(checker_output, end="" if checker_output.endswith("\n") or not checker_output else "\n")

    report_path = report_dir / str(require(config, "report_filename"))
    write_report(
        report_path,
        summary,
        frozen_fields,
        Counter(row["position_category"] for row in frozen_rows),
        len(frozen_rows),
        len(eligible),
        pools,
        [str(dialogue_id) for dialogue_id in dialogue_ids],
        checker_output,
        len(candidates),
    )
    print(f"Wrote {report_path}")
    if checker.returncode != 0:
        raise SystemExit(checker.returncode)


if __name__ == "__main__":
    main()
