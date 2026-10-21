#!/usr/bin/env python3
"""Generate doctor turns for frozen contexts.

The human reference file is never opened. Live runs append JSONL records and
do not overwrite earlier lines. A completed request is never sent again.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import threading
import time
from concurrent.futures import CancelledError, ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from postprocess import clean_text  # noqa: E402
from prompting import CONDITIONS, assemble_system, assemble_user, load_prompt_file  # noqa: E402
from providers.base import GenerationRequest  # noqa: E402

CHARS_PER_TOKEN_ESTIMATE = 4


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
        elif value == "":
            data[key] = ""
        elif value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            data[key] = int(value)
        elif _is_float(value):
            data[key] = float(value)
        else:
            data[key] = value.strip("'\"")
    return data


def _is_float(value: str) -> bool:
    if value.count(".") != 1:
        return False
    left, right = value.split(".")
    return bool(left) and left.replace("-", "").isdigit() and right.isdigit()


def require(config: dict[str, object], key: str) -> object:
    if key not in config:
        raise SystemExit(f"Missing config key: {key}")
    return config[key]


def optional_number(config: dict[str, object], key: str) -> int | float | None:
    if key not in config or config[key] in ("", None):
        return None
    value = config[key]
    if isinstance(value, (int, float)):
        return value
    raise SystemExit(f"{key} must be a number when set, found {value!r}.")


def sha256(path: Path) -> str:
    # Git checks these files out with CRLF on Windows. The recorded digests are
    # the LF bytes the study loads. Normalize only for the digest; do not rewrite the file.
    digest = hashlib.sha256()
    digest.update(path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n"))
    return digest.hexdigest()


def verify_frozen_hashes(project_dir: Path, config: dict[str, object], filenames: tuple[str, ...]) -> None:
    frozen_dir = project_dir / str(require(config, "frozen_dir"))
    manifest_path = frozen_dir / str(require(config, "manifest_filename"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected = manifest.get("sha256")
    if not isinstance(expected, dict):
        raise SystemExit("frozen_manifest.json has no sha256 object.")
    for filename in filenames:
        path = frozen_dir / filename
        if "human_reference" in path.name:
            raise SystemExit("Refusing to read a human reference file.")
        actual = sha256(path)
        recorded = expected.get(filename)
        if actual != recorded:
            raise SystemExit(
                f"SHA-256 mismatch for {filename}. recorded={recorded} actual={actual}. Aborting."
            )
        print(f"SHA-256 ok {filename}")


def read_contexts(path: Path) -> list[dict[str, str]]:
    if "human_reference" in path.name:
        raise SystemExit("Refusing to read a human reference file.")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"context_id", "dialogue_id", "position", "context"}
    missing = required - set(rows[0].keys() if rows else [])
    if missing:
        raise SystemExit(f"{path.name} is missing columns: {sorted(missing)}")
    if "human_clinician_target" in rows[0]:
        raise SystemExit(f"{path.name} contains the human target column.")
    return rows


def estimate_tokens(text: str) -> int:
    return max(1, -(-len(text) // CHARS_PER_TOKEN_ESTIMATE))


def build_requests(
    rows: list[dict[str, str]],
    prompts: dict[str, object],
    model_id: str,
    conditions: list[str],
) -> list[dict[str, object]]:
    requests: list[dict[str, object]] = []
    for row in sorted(rows, key=lambda item: (item["context_id"], item["dialogue_id"])):
        for condition in conditions:
            system_text = assemble_system(prompts, condition)
            user_text = assemble_user(prompts, row["context"])
            item = {
                "context_id": row["context_id"],
                "dialogue_id": row["dialogue_id"],
                "position": row["position"],
                "condition": condition,
                "model_id": model_id,
                "system_instruction": system_text,
                "user_text": user_text,
            }
            if row.get("dataset"):
                item["dataset"] = row["dataset"]
            requests.append(item)
    return requests


def shuffle_requests(requests: list[dict[str, object]], seed: int) -> list[dict[str, object]]:
    rng = np.random.default_rng(seed)
    order = rng.permutation(len(requests))
    return [requests[int(index)] for index in order]


def completed_keys(path: Path) -> set[tuple[str, str, str]]:
    done: set[tuple[str, str, str]] = set()
    if not path.exists():
        return done
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("error") is None:
                done.add((record["context_id"], record["model_id"], record["condition"]))
            else:
                _ = line_number
    return done


def attempt_counts(path: Path) -> dict[tuple[str, str, str], int]:
    counts: dict[tuple[str, str, str], int] = {}
    if not path.exists():
        return counts
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            key = (record["context_id"], record["model_id"], record["condition"])
            counts[key] = counts.get(key, 0) + 1
    return counts


def append_record(path: Path, record: dict[str, object], lock: threading.Lock) -> None:
    payload = json.dumps(record, ensure_ascii=False)
    if "human_clinician_target" in payload:
        raise SystemExit("Refusing to write a record that contains the human target field.")
    with lock:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(payload + "\n")
            handle.flush()


def is_retryable(exc: Exception) -> bool:
    code = getattr(exc, "code", None) or getattr(exc, "status_code", None)
    if code in (408, 429, 500, 502, 503, 504):
        return True
    text = str(exc).lower()
    markers = ("resource_exhausted", "unavailable", "deadline exceeded", "timed out", "timeout", "503", "429", "529", "overloaded", "connection")
    return any(marker in text for marker in markers)


def reasoning_setting_label(thinking_level: str | None, thinking_budget: int | None) -> str:
    parts: list[str] = []
    if thinking_level is not None:
        parts.append(f"thinking_level={thinking_level}")
    if thinking_budget is not None:
        parts.append(f"thinking_budget={thinking_budget}")
    if not parts:
        raise SystemExit("A live run requires an explicit reasoning setting.")
    return ",".join(parts)


def reasoning_token_count(usage: dict[str, object] | None, thinking_budget: int | None) -> int | None:
    if usage and "thoughts_token_count" in usage and usage["thoughts_token_count"] is not None:
        return int(usage["thoughts_token_count"])
    if usage and usage.get("reasoning_tokens") is not None:
        return int(usage["reasoning_tokens"])
    # Gemini omits thoughts_token_count when thinking is disabled. The probe
    # call with thinking_budget 0 had prompt + candidates = total.
    if thinking_budget == 0:
        return 0
    return None


def run_one(
    item: dict[str, object],
    provider,
    prompt_sha: str,
    max_output_tokens: int,
    temperature: float | None,
    top_p: float | None,
    top_k: int | None,
    thinking_level: str | None,
    thinking_budget: int | None,
    reasoning_effort: str | None,
    reasoning_setting: str,
    max_attempts: int,
    retry_initial_seconds: float,
    retry_multiplier: float,
    prior_attempts: int,
    output_path: Path,
    lock: threading.Lock,
    stop: threading.Event | None = None,
) -> dict[str, object]:
    if stop is not None and stop.is_set():
        return {"status": "skipped", "empty": False, "truncated": False, "patient_turn": False}
    key = (str(item["context_id"]), str(item["model_id"]), str(item["condition"]))
    request = GenerationRequest(
        model_id=str(item["model_id"]),
        system_instruction=str(item["system_instruction"]),
        user_text=str(item["user_text"]),
        max_output_tokens=max_output_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        thinking_level=thinking_level,
        thinking_budget=thinking_budget,
        reasoning_effort=reasoning_effort,
    )
    for attempt_index in range(1, max_attempts + 1):
        if stop is not None and stop.is_set():
            return {"status": "skipped", "empty": False, "truncated": False, "patient_turn": False}
        attempt_count = prior_attempts + attempt_index
        started = time.perf_counter()
        timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
        try:
            result = provider.generate(request)
            latency = time.perf_counter() - started
            append_record(
                output_path,
                {
                    "context_id": key[0],
                    "dialogue_id": item["dialogue_id"],
                    "position": item["position"],
                    "condition": key[2],
                    "model_id": key[1],
                    "model_version": result.model_version,
                    "prompt_sha256": prompt_sha,
                    "request_parameters": result.request_parameters,
                    "response_text": result.response_text,
                    "finish_reason": result.finish_reason,
                    "token_usage": result.token_usage,
                    "reasoning_setting": reasoning_setting,
                    "reasoning_token_count": reasoning_token_count(result.token_usage, thinking_budget),
                    "timestamp": timestamp,
                    "latency_seconds": round(latency, 3),
                    "attempt_count": attempt_count,
                    "error": None,
                    **({"dataset": item["dataset"]} if item.get("dataset") else {}),
                },
                lock,
            )
            print(f"ok {key[0]} {key[2]}", flush=True)
            finish = "" if result.finish_reason is None else str(result.finish_reason)
            return {
                "status": "ok",
                "empty": clean_text(result.response_text) == "",
                "truncated": finish in {"MAX_TOKENS", "max_tokens", "length"},
                "patient_turn": "Patient:" in (result.response_text or ""),
            }
        except Exception as exc:  # noqa: BLE001
            latency = time.perf_counter() - started
            message = provider.redact(f"{type(exc).__name__}: {exc}") if hasattr(provider, "redact") else f"{type(exc).__name__}"
            retry = is_retryable(exc) and attempt_index < max_attempts
            if not retry:
                append_record(
                    output_path,
                    {
                        "context_id": key[0],
                        "dialogue_id": item["dialogue_id"],
                        "position": item["position"],
                        "condition": key[2],
                        "model_id": key[1],
                        "model_version": None,
                        "prompt_sha256": prompt_sha,
                        "request_parameters": {
                            "model": request.model_id,
                            "max_output_tokens": request.max_output_tokens,
                            "contents": request.user_text,
                            "config": {
                                "system_instruction": request.system_instruction,
                                "max_output_tokens": request.max_output_tokens,
                            },
                        },
                        "response_text": None,
                        "finish_reason": None,
                        "token_usage": {},
                        "reasoning_setting": reasoning_setting,
                        "reasoning_token_count": None,
                        "timestamp": timestamp,
                        "latency_seconds": round(latency, 3),
                        "attempt_count": attempt_count,
                        "error": message,
                        **({"dataset": item["dataset"]} if item.get("dataset") else {}),
                    },
                    lock,
                )
                print(f"FAILED {key[0]} {key[2]} attempt {attempt_count}: {message}", file=sys.stderr)
                return {"status": "error", "empty": False, "truncated": False, "patient_turn": False}
            delay = retry_initial_seconds * (retry_multiplier ** (attempt_index - 1))
            print(
                f"RETRY {key[0]} {key[2]} attempt {attempt_count} in {delay:.1f}s: {message}",
                file=sys.stderr,
            )
            time.sleep(delay)


def print_dry_run(requests: list[dict[str, object]], prompt_sha: str) -> None:
    print(f"Prompt SHA-256: {prompt_sha}")
    print(f"Requests: {len(requests)}")
    total_chars = 0
    for item in requests:
        total_chars += len(str(item["system_instruction"])) + len(str(item["user_text"]))
    estimated = -(-total_chars // CHARS_PER_TOKEN_ESTIMATE)
    print(
        "Estimated input tokens: "
        f"{estimated} (characters/4 = {total_chars}/{CHARS_PER_TOKEN_ESTIMATE}; not a Gemini countTokens call)"
    )
    by_condition: dict[str, list[dict[str, object]]] = {condition: [] for condition in CONDITIONS}
    for item in requests:
        by_condition[str(item["condition"])].append(item)
    for condition in CONDITIONS:
        examples = by_condition[condition][:2]
        if len(examples) < 2:
            raise SystemExit(f"Need two contexts to preview {condition}.")
        for index, item in enumerate(examples, start=1):
            print("\n" + "=" * 72)
            print(f"DRY RUN {condition} example {index} context_id={item['context_id']} position={item['position']}")
            print("- system -")
            print(item["system_instruction"], end="" if str(item["system_instruction"]).endswith("\n") else "\n")
            print("- user -")
            print(item["user_text"], end="" if str(item["user_text"]).endswith("\n") else "\n")


def prompt_sha_from_output(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Cannot read the pilot prompt SHA from {path}.")
    with path.open(encoding="utf-8") as handle:
        line = handle.readline()
    if not line.strip():
        raise SystemExit(f"{path} has no records to supply the pilot prompt SHA.")
    record = json.loads(line)
    sha = record.get("prompt_sha256")
    if not isinstance(sha, str) or len(sha) != 64:
        raise SystemExit("Pilot output has no prompt_sha256.")
    return sha


def assert_external_requests(requests: list[dict[str, object]]) -> None:
    if not requests:
        raise SystemExit("No prompts were assembled.")
    if len(requests) % 6 != 0:
        raise SystemExit(f"Expected a multiple of 6 prompts, found {len(requests)}.")
    counts = {condition: 0 for condition in CONDITIONS}
    for item in requests:
        condition = str(item["condition"])
        if condition not in counts:
            raise SystemExit(f"Unexpected condition {condition}.")
        counts[condition] += 1
        user_text = str(item["user_text"])
        last_line = user_text.rstrip("\n").split("\n")[-1]
        if last_line != "Doctor:" or not user_text.endswith(("Doctor:", "Doctor:\n")):
            raise SystemExit(
                f"{item['context_id']} {condition} user message does not end with Doctor:."
            )
    expected = len(requests) // 6
    for condition, count in counts.items():
        if count != expected:
            raise SystemExit(f"{condition} has {count} prompts, expected {expected}.")
    print(
        f"Assembled {len(requests)} prompts: {expected} per condition. "
        "Every user message ends with Doctor:."
    )


def assert_main_requests(requests: list[dict[str, object]]) -> None:
    if len(requests) != 4824:
        raise SystemExit(f"Expected 4824 assembled prompts, found {len(requests)}.")
    counts = {condition: 0 for condition in CONDITIONS}
    contexts: set[str] = set()
    for item in requests:
        condition = str(item["condition"])
        if condition not in counts:
            raise SystemExit(f"Unexpected condition {condition}.")
        counts[condition] += 1
        contexts.add(str(item["context_id"]))
        user_text = str(item["user_text"])
        last_line = user_text.rstrip("\n").split("\n")[-1]
        if last_line != "Doctor:" or not user_text.endswith(("Doctor:", "Doctor:\n")):
            raise SystemExit(
                f"{item['context_id']} {condition} user message does not end with Doctor:."
            )
    for condition, count in counts.items():
        if count != 804:
            raise SystemExit(f"{condition} has {count} prompts, expected 804.")
    if len(contexts) != 804:
        raise SystemExit(f"Expected 804 contexts, found {len(contexts)}.")
    print("Assembled 4824 prompts: 804 per condition. Every user message ends with Doctor:.")


def note_main_outcome(
    outcome: dict[str, object],
    first: list[dict[str, object]],
    consecutive_errors: list[int],
    stop: threading.Event,
) -> str | None:
    if outcome.get("status") == "skipped":
        return None
    if len(first) < 30:
        first.append(outcome)
        if len(first) == 30:
            bad = sum(
                1
                for item in first
                if item.get("status") == "error"
                or item.get("empty")
                or item.get("truncated")
                or item.get("patient_turn")
            )
            print(
                "Early-stop check after 30 requests: "
                f"{bad} empty, truncated, errors, or Patient: turns.",
                flush=True,
            )
            if bad > 3:
                stop.set()
                return (
                    f"Halted after 30 requests: {bad} were empty, truncated, errors, or contained a Patient: turn."
                )
    if outcome.get("status") == "error":
        consecutive_errors[0] += 1
        if consecutive_errors[0] >= 20:
            stop.set()
            return "Halted: 20 consecutive requests failed."
    else:
        consecutive_errors[0] = 0
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path)
    parser.add_argument("--split", choices=("pilot", "main"), required=True)
    parser.add_argument("--provider", choices=("gemini", "claude", "gpt"), default="gemini")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--contexts", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    project_dir = Path(__file__).resolve().parents[1]
    config_path = args.config.resolve() if args.config else project_dir / "config.yaml"
    config = load_config(config_path)
    project_dir = config_path.parent
    reasoning_effort = None
    if args.provider == "claude":
        model_id = str(require(config, "claude_model_id"))
        thinking_level = None
        thinking_budget = None
        setting = "thinking_omitted_default_off"
        system_delivery = "Messages API top-level system parameter"
        sampling = "temperature omitted (API default 1.0); top_p omitted; top_k omitted"
        output_name_key = "claude_main_output_jsonl"
        max_output_tokens = int(require(config, "claude_max_output_tokens"))
    elif args.provider == "gpt":
        model_id = str(require(config, "gpt_model_id"))
        thinking_level = None
        thinking_budget = None
        raw_effort = config.get("gpt_reasoning_effort")
        if raw_effort in (None, "", "omitted", "none"):
            reasoning_effort = None
            setting = "reasoning omitted; this model has no reasoning step"
        else:
            reasoning_effort = str(raw_effort)
            setting = f"reasoning_effort={reasoning_effort}"
        system_delivery = "Chat Completions system role"
        sampling = "temperature omitted; top_p omitted; top_k is not a Chat Completions parameter; service_tier omitted"
        output_name_key = "gpt_main_output_jsonl"
        max_output_tokens = int(require(config, "gpt_max_output_tokens"))
    else:
        model_id = str(require(config, "model_id"))
        thinking_level = config.get("thinking_level")
        thinking_level = None if thinking_level in (None, "") else str(thinking_level)
        thinking_budget_raw = optional_number(config, "thinking_budget")
        thinking_budget = None if thinking_budget_raw is None else int(thinking_budget_raw)
        if thinking_level is not None and thinking_budget is not None:
            raise SystemExit("Set only one of thinking_level or thinking_budget.")
        setting = reasoning_setting_label(thinking_level, thinking_budget)
        system_delivery = "Gemini system_instruction"
        sampling = "temperature, top_p, and top_k omitted"
        output_name_key = "pilot_output_jsonl" if args.split == "pilot" else "main_output_jsonl"
        max_output_tokens = int(require(config, "max_output_tokens"))
    print(f"model_id: {model_id}", flush=True)
    print(f"reasoning_setting: {setting}", flush=True)
    print(f"system_prompt_delivery: {system_delivery}", flush=True)
    print(f"sampling: {sampling}", flush=True)

    if args.contexts is None:
        if args.split == "main":
            frozen_names = (str(require(config, "main_frozen_filename")),)
        else:
            frozen_names = (
                str(require(config, "main_frozen_filename")),
                str(require(config, "pilot_frozen_filename")),
            )
        verify_frozen_hashes(project_dir, config, frozen_names)

        frozen_dir = project_dir / str(require(config, "frozen_dir"))
        filename = str(require(config, "pilot_frozen_filename" if args.split == "pilot" else "main_frozen_filename"))
        if args.split == "main" and filename != "p2_contexts_FROZEN.csv":
            raise SystemExit(f"Main split must read p2_contexts_FROZEN.csv, found {filename}.")
        if "pilot" in filename and args.split == "main":
            raise SystemExit("Refusing to read the pilot contexts for the main run.")
        rows = read_contexts(frozen_dir / filename)
    else:
        context_path = args.contexts if args.contexts.is_absolute() else project_dir / args.contexts
        if "human_reference" in context_path.name or "note" in context_path.name:
            raise SystemExit("Refusing to read a note or human-reference file as model context.")
        rows = read_contexts(context_path)
        print(f"External contexts: {len(rows)} from {context_path}")
    prompt_path = project_dir / str(require(config, "prompt_file"))
    prompts = load_prompt_file(prompt_path)
    prompt_sha = sha256(prompt_path)
    if args.split == "main":
        pilot_output = project_dir / str(require(config, "pilot_output_jsonl"))
        pilot_sha = prompt_sha_from_output(pilot_output)
        if prompt_sha != pilot_sha:
            raise SystemExit(
                f"Prompt SHA-256 {prompt_sha} does not equal the pilot SHA {pilot_sha}."
            )
        print(f"Prompt SHA-256 matches the pilot: {prompt_sha}")
    conditions = [str(item) for item in require(config, "conditions")]
    if conditions != list(CONDITIONS):
        raise SystemExit(f"conditions must be {list(CONDITIONS)}, found {conditions}.")
    ordered = build_requests(rows, prompts, model_id, conditions)
    requests = shuffle_requests(ordered, int(require(config, "request_shuffle_seed")))
    if args.contexts is None and args.split == "main":
        assert_main_requests(requests)
    elif args.contexts is not None:
        assert_external_requests(requests)

    if args.dry_run:
        print_dry_run(ordered, prompt_sha)
        print("\nShuffled request order, first 12 keys:")
        for item in requests[:12]:
            print(f"  {item['context_id']} {item['condition']}")
        return

    if not model_id:
        raise SystemExit("Set model_id in config.yaml before a live run. Do not guess it in code.")
    if args.output is not None:
        output_path = args.output if args.output.is_absolute() else project_dir / args.output
    else:
        output_path = project_dir / str(require(config, output_name_key))
    pilot_output_path = project_dir / str(require(config, "pilot_output_jsonl"))
    gemini_output_path = project_dir / str(require(config, "main_output_jsonl"))
    gpt_output_path = (project_dir / str(require(config, "gpt_main_output_jsonl"))).resolve()
    protected = {
        pilot_output_path.resolve(),
        gemini_output_path.resolve(),
        (project_dir / str(require(config, "claude_main_output_jsonl"))).resolve(),
    }
    if output_path.resolve() in protected:
        raise SystemExit(f"Refusing to write onto an existing study output: {output_path}")
    if output_path.resolve() == gpt_output_path and output_path.exists():
        existing_models = {key[1] for key in completed_keys(output_path)}
        if existing_models and existing_models != {model_id}:
            raise SystemExit(
                f"Refusing to append {model_id} onto {output_path.name}, which already holds {sorted(existing_models)}."
            )
    done = completed_keys(output_path)
    prior = attempt_counts(output_path)
    pending = [
        item
        for item in requests
        if (str(item["context_id"]), str(item["model_id"]), str(item["condition"])) not in done
    ]
    print(f"Completed already: {len(done)}. Pending: {len(pending)}. Output: {output_path}")
    if not pending:
        return

    if args.provider == "claude":
        from providers.claude import ClaudeProvider

        provider = ClaudeProvider(str(require(config, "anthropic_api_key_env")))
    elif args.provider == "gpt":
        from providers.gpt import GPTProvider

        provider = GPTProvider(str(require(config, "openai_api_key_env")))
    else:
        from providers.gemini import GeminiProvider

        provider = GeminiProvider(str(require(config, "gemini_api_key_env")))
    lock = threading.Lock()
    temperature = optional_number(config, "temperature")
    top_p = optional_number(config, "top_p")
    top_k_raw = optional_number(config, "top_k")
    top_k = None if top_k_raw is None else int(top_k_raw)
    workers = int(require(config, "concurrency"))
    max_attempts = int(require(config, "max_attempts"))
    retry_initial = float(require(config, "retry_initial_seconds"))
    retry_multiplier = float(require(config, "retry_multiplier"))
    stop = threading.Event()
    first_outcomes: list[dict[str, object]] = []
    consecutive_errors = [0]
    halt_reason: str | None = None

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [
            pool.submit(
                run_one,
                item,
                provider,
                prompt_sha,
                max_output_tokens,
                None if temperature is None else float(temperature),
                None if top_p is None else float(top_p),
                top_k,
                thinking_level,
                thinking_budget,
                reasoning_effort,
                setting,
                max_attempts,
                retry_initial,
                retry_multiplier,
                prior.get((str(item["context_id"]), str(item["model_id"]), str(item["condition"])), 0),
                output_path,
                lock,
                stop if args.split == "main" else None,
            )
            for item in pending
        ]
        completed = 0
        for future in as_completed(futures):
            try:
                outcome = future.result()
            except CancelledError:
                continue
            if outcome.get("status") == "skipped":
                continue
            completed += 1
            if args.split == "main" and halt_reason is None:
                reason = note_main_outcome(outcome, first_outcomes, consecutive_errors, stop)
                if reason is not None:
                    halt_reason = reason
                    stop.set()
                    for pending_future in futures:
                        pending_future.cancel()
            if completed % 100 == 0:
                print(f"progress {completed}", flush=True)
    if halt_reason is not None:
        raise SystemExit(halt_reason + " Completed requests were kept. Re-run resumes without regenerating them.")
    print(f"Finished. Records appended to {output_path}")


if __name__ == "__main__":
    main()
