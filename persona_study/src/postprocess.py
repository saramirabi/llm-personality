#!/usr/bin/env python3
"""Clean generation JSONL into a table. This script never writes the JSONL."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

LEADING_DOCTOR = re.compile(r"^\s*Doctor:\s*")
PATIENT_TURN = "Patient:"
DOCTOR_TURN = "Doctor:"
AI_META = re.compile(
    r"("
    r"\bas an ai\b|"
    r"\bi am an ai\b|"
    r"\bi'm an ai\b|"
    r"\bi’m an ai\b|"
    r"\blanguage model\b|"
    r"\bas an artificial intelligence\b|"
    r"\bi(?:'m| am) (?:just )?an? (?:ai|artificial intelligence|language model)\b|"
    r"\bi (?:cannot|can't) (?:role[- ]?play|pretend|assist with that|provide medical)\b"
    r")",
    re.IGNORECASE,
)


def successful_records(path: Path) -> list[dict[str, object]]:
    chosen: dict[tuple[str, str, str], dict[str, object]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("error") is not None:
                continue
            key = (record["context_id"], record["model_id"], record["condition"])
            previous = chosen.get(key)
            if previous is None or int(record.get("attempt_count") or 0) >= int(previous.get("attempt_count") or 0):
                chosen[key] = record
    return list(chosen.values())


def clean_text(raw: str | None) -> str:
    text = "" if raw is None else str(raw)
    text = LEADING_DOCTOR.sub("", text, count=1)
    return text.strip()


def analysis_text(raw: str | None) -> str:
    """Text before the first Patient: label. That prefix is the first doctor turn."""
    text = "" if raw is None else str(raw)
    index = text.find(PATIENT_TURN)
    if index == -1:
        return text
    return text[:index]


def word_count(text: str) -> int:
    return len(text.split())


def exact_repeat_flags(records: list[dict[str, object]]) -> dict[tuple[str, str, int], int]:
    """1 when a doctor turn matches the previous doctor turn after trimming whitespace."""
    grouped: dict[tuple[str, str], list[dict[str, object]]] = {}
    for record in records:
        if record.get("role") != "doctor" or record.get("error") is not None:
            continue
        key = (str(record["context_id"]), str(record["condition"]))
        grouped.setdefault(key, []).append(record)
    flags_out: dict[tuple[str, str, int], int] = {}
    for key, turns in grouped.items():
        ordered = sorted(turns, key=lambda item: int(item["turn"]))
        previous = None
        for record in ordered:
            text = str(record.get("analysis_text") or "").strip()
            turn = int(record["turn"])
            flags_out[(key[0], key[1], turn)] = int(previous is not None and text == previous)
            previous = text
    return flags_out


def flags(raw: str | None, cleaned: str, finish_reason: str | None) -> dict[str, int]:
    raw_text = "" if raw is None else str(raw)
    remaining_doctor = DOCTOR_TURN in LEADING_DOCTOR.sub("", raw_text, count=1)
    return {
        "flag_empty": int(cleaned == ""),
        "flag_truncated": int(finish_reason in {"MAX_TOKENS", "max_tokens", "length"}),
        "flag_patient_turn": int(PATIENT_TURN in raw_text or PATIENT_TURN in cleaned),
        "flag_multiple_doctor_turns": int(remaining_doctor),
        "flag_refusal_or_ai_meta": int(AI_META.search(raw_text) is not None or AI_META.search(cleaned) is not None),
    }


def write_rollout_cleaned(jsonl_path: Path, csv_path: Path) -> int:
    """Cleaned rollout table. Does not rewrite the JSONL or any Experiment 1 file."""
    if jsonl_path.resolve() == csv_path.resolve():
        raise SystemExit("Refusing to write the cleaned table over the raw JSONL.")
    records: list[dict[str, object]] = []
    with jsonl_path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    chosen: dict[tuple[str, str, int, str], dict[str, object]] = {}
    for record in records:
        if record.get("error") is not None:
            continue
        key = (str(record["context_id"]), str(record["condition"]), int(record["turn"]), str(record["role"]))
        chosen[key] = record
    repeats = exact_repeat_flags(list(chosen.values()))
    fieldnames = [
        "context_id",
        "dialogue_id",
        "position",
        "condition",
        "doctor_model_id",
        "turn",
        "role",
        "model_id",
        "model_version",
        "finish_reason",
        "analysis_text",
        "analysis_word_count",
        "closing_detected",
        "exact_repeat",
        "reused_from_experiment1",
        "prompt_file_hash",
    ]
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(chosen.values(), key=lambda item: (str(item["context_id"]), str(item["condition"]), int(item["turn"]), str(item["role"])))
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for record in rows:
            turn = int(record["turn"])
            role = str(record["role"])
            analysed = str(record.get("analysis_text") or "")
            repeat = ""
            if role == "doctor":
                repeat = repeats[(str(record["context_id"]), str(record["condition"]), turn)]
            writer.writerow(
                {
                    "context_id": record["context_id"],
                    "dialogue_id": record["dialogue_id"],
                    "position": record["position"],
                    "condition": record["condition"],
                    "doctor_model_id": record.get("doctor_model_id") or "",
                    "turn": turn,
                    "role": role,
                    "model_id": record.get("model_id") or "",
                    "model_version": record.get("model_version") or "",
                    "finish_reason": record.get("finish_reason") or "",
                    "analysis_text": analysed,
                    "analysis_word_count": word_count(analysed),
                    "closing_detected": int(bool(record.get("closing_detected"))),
                    "exact_repeat": repeat,
                    "reused_from_experiment1": int(bool(record.get("reused_from_experiment1"))),
                    "prompt_file_hash": record.get("prompt_file_hash") or "",
                }
            )
    return len(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        raise SystemExit("Refusing to write the cleaned table over the raw JSONL.")
    if "human_reference" in args.input.name or "human_reference" in args.output.name:
        raise SystemExit("Refusing to read or write a human reference file.")
    records = successful_records(args.input)
    fieldnames = [
        "context_id",
        "dialogue_id",
        "position",
        "condition",
        "model_id",
        "model_version",
        "finish_reason",
        "response_text",
        "cleaned_text",
        "analysis_text",
        "word_count",
        "analysis_word_count",
        "flag_empty",
        "flag_truncated",
        "flag_patient_turn",
        "flag_multiple_doctor_turns",
        "flag_refusal_or_ai_meta",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for record in sorted(records, key=lambda item: (str(item["context_id"]), str(item["condition"]))):
            raw = None if record.get("response_text") is None else str(record.get("response_text"))
            cleaned = clean_text(raw)
            analysed = analysis_text(raw)
            row = {
                "context_id": record["context_id"],
                "dialogue_id": record["dialogue_id"],
                "position": record["position"],
                "condition": record["condition"],
                "model_id": record["model_id"],
                "model_version": record.get("model_version") or "",
                "finish_reason": record.get("finish_reason") or "",
                "response_text": "" if raw is None else raw,
                "cleaned_text": cleaned,
                "analysis_text": analysed,
                "word_count": word_count(cleaned),
                "analysis_word_count": word_count(analysed),
            }
            row.update(flags(raw, cleaned, row["finish_reason"]))
            writer.writerow(row)
    print(f"Wrote {len(records)} cleaned rows to {args.output}")


if __name__ == "__main__":
    main()
