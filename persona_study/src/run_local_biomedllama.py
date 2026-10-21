#!/usr/bin/env python3
"""E1 and E2 doctor turns for local bio-medical Llama 3.

Does not read the human reference file and does not write Gemini, Claude, or GPT outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from generate import is_retryable, load_config, read_contexts  # noqa: E402
from postprocess import analysis_text, clean_text  # noqa: E402
from prompting import CONDITIONS, assemble_system, assemble_user, load_prompt_file  # noqa: E402
from providers.base import GenerationRequest  # noqa: E402
from providers.biomedllama import (  # noqa: E402
    CONTEXT_LENGTH,
    MODEL_ID,
    REASONING_SETTING,
    TOKENIZER_ID,
    BioMedLlamaProvider,
    count_prompt_tokens,
    output_limit,
)

PROJECT = SRC_DIR.parent
EXPECTED_SHA = {
    "prompts/p2_prompts_v1.yaml": "5d91f7d1e52d4b6b3ec38d6b05ab9eef8d184113eb9597f52cd52de88bae7999",
    "prompts/p2_patient_v2.yaml": "f23b9c276788ac78fba6cdf889e2eb669c9bd82695e1d9ad663b0970802c5cf6",
    "data/frozen/p2_contexts_FROZEN.csv": "4ed0b5b043ed0bf4446fce7cba3332bcc8a2f2d63c7908ad24877486e3d6b36d",
}
PROTECTED = {
    PROJECT / "outputs" / "main_gemini.jsonl",
    PROJECT / "outputs" / "main_claude.jsonl",
    PROJECT / "outputs" / "main_gpt.jsonl",
    PROJECT / "outputs" / "aci_gemini.jsonl",
    PROJECT / "outputs" / "aci_claude.jsonl",
    PROJECT / "outputs" / "aci_gpt.jsonl",
    PROJECT / "outputs" / "pilot_gemini.jsonl",
}
TRUNCATED = {"MAX_TOKENS", "max_tokens", "length"}


def text_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def verify_study_hashes() -> str:
    prompt_sha = ""
    for relative, expected in EXPECTED_SHA.items():
        path = PROJECT / relative
        actual = text_sha256(path)
        if actual != expected:
            raise SystemExit(
                f"SHA-256 mismatch for {relative}. expected={expected} actual={actual}. "
                "The file was not edited."
            )
        print(f"SHA-256 ok {relative}", flush=True)
        if relative.endswith("p2_prompts_v1.yaml"):
            prompt_sha = actual
    return prompt_sha


def load_tokenizer():
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained(TOKENIZER_ID)


def user_ends_with_doctor(user_text: str, context_id: str, condition: str) -> None:
    last_line = user_text.rstrip("\n").split("\n")[-1]
    if last_line != "Doctor:" or not user_text.endswith("Doctor:\n"):
        raise SystemExit(f"{context_id} {condition} user message does not end with Doctor:.")


def completed_successes(path: Path) -> set[tuple[str, str]]:
    done: set[tuple[str, str]] = set()
    if not path.exists():
        return done
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("error") is None and str(record.get("response_text") or "").strip():
                done.add((str(record["context_id"]), str(record["condition"])))
    return done


def attempt_counts(path: Path) -> dict[tuple[str, str], int]:
    counts: dict[tuple[str, str], int] = {}
    if not path.exists():
        return counts
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            key = (str(record["context_id"]), str(record["condition"]))
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


def is_oom(exc: Exception) -> bool:
    text = str(exc).lower()
    markers = ("out of memory", "outofmemory", "cuda", "failed to allocate", "insufficient memory", "kv cache")
    return any(marker in text for marker in markers)


def has_text(value: str | None) -> bool:
    return bool(value and str(value).strip())


def is_bad_outcome(outcome: dict[str, object]) -> bool:
    return bool(
        outcome.get("status") == "error"
        or outcome.get("empty")
        or outcome.get("truncated")
        or outcome.get("patient_turn")
    )


def final_outcomes(path: Path) -> list[dict[str, object]]:
    """One outcome per key, in first-seen order, using that key's last stored attempt."""
    order: list[tuple[str, str]] = []
    last: dict[tuple[str, str], dict[str, object]] = {}
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            key = (str(record["context_id"]), str(record["condition"]))
            if key not in last:
                order.append(key)
            text = str(record.get("response_text") or "")
            finish = "" if record.get("finish_reason") is None else str(record.get("finish_reason"))
            failed = record.get("error") is not None or not text.strip()
            last[key] = {
                "status": "error" if failed else "ok",
                "empty": clean_text(text) == "",
                "truncated": finish in TRUNCATED,
                "patient_turn": "Patient:" in text,
            }
    return [last[key] for key in order]


def assert_early_stop_history(path: Path) -> None:
    outcomes = final_outcomes(path)
    if len(outcomes) < 30:
        return
    bad = sum(1 for item in outcomes[:30] if is_bad_outcome(item))
    print(f"Early-stop check after 30 requests: {bad} empty, truncated, errors, or Patient: turns.", flush=True)
    if bad > 3:
        raise SystemExit(
            f"Halted after 30 requests: {bad} were empty, truncated, errors, or contained a Patient: turn."
        )


def build_items(rows: list[dict[str, str]], prompts: dict[str, object]) -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    for row in sorted(rows, key=lambda item: (item["context_id"], item["dialogue_id"])):
        for condition in CONDITIONS:
            system_text = assemble_system(prompts, condition)
            user_text = assemble_user(prompts, row["context"])
            user_ends_with_doctor(user_text, row["context_id"], condition)
            item = {
                "context_id": row["context_id"],
                "dialogue_id": row["dialogue_id"],
                "position": row["position"],
                "condition": condition,
                "system_instruction": system_text,
                "user_text": user_text,
            }
            if row.get("dataset"):
                item["dataset"] = row["dataset"]
            items.append(item)
    return items


def base_record(
    item: dict[str, object],
    prompt_sha: str,
    attempt_count: int,
    timestamp: str,
    latency: float,
) -> dict[str, object]:
    record = {
        "context_id": item["context_id"],
        "dialogue_id": item["dialogue_id"],
        "position": item["position"],
        "condition": item["condition"],
        "model_id": MODEL_ID,
        "model_version": None,
        "prompt_sha256": prompt_sha,
        "request_parameters": {"model": MODEL_ID},
        "response_text": None,
        "finish_reason": None,
        "token_usage": {},
        "reasoning_setting": REASONING_SETTING,
        "reasoning_token_count": None,
        "timestamp": timestamp,
        "latency_seconds": round(latency, 3),
        "attempt_count": attempt_count,
        "error": None,
    }
    if item.get("dataset"):
        record["dataset"] = item["dataset"]
    return record


def run_item(
    item: dict[str, object],
    provider: BioMedLlamaProvider,
    tokenizer,
    tokenizer_lock: threading.Lock,
    prompt_sha: str,
    prior_attempts: int,
    output_path: Path,
    lock: threading.Lock,
    stop: threading.Event,
    max_attempts: int,
    retry_initial: float,
    retry_multiplier: float,
) -> dict[str, object]:
    if stop.is_set():
        return {"status": "skipped"}
    key = (str(item["context_id"]), str(item["condition"]))
    with tokenizer_lock:
        prompt_tokens = count_prompt_tokens(tokenizer, str(item["system_instruction"]), str(item["user_text"]))
    try:
        limit = output_limit(prompt_tokens)
    except RuntimeError as exc:
        stop.set()
        raise SystemExit(str(exc)) from exc
    request = GenerationRequest(
        model_id=MODEL_ID,
        system_instruction=str(item["system_instruction"]),
        user_text=str(item["user_text"]),
        max_output_tokens=limit,
    )
    content_tries = 0
    transport_tries = 0
    while content_tries < 2:
        if stop.is_set():
            return {"status": "skipped"}
        last_error = ""
        result = None
        for transport_index in range(1, max_attempts + 1):
            if stop.is_set():
                return {"status": "skipped"}
            transport_tries += 1
            started = time.perf_counter()
            timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
            try:
                result = provider.generate(request)
                latency = time.perf_counter() - started
                break
            except Exception as exc:  # noqa: BLE001
                latency = time.perf_counter() - started
                last_error = f"{type(exc).__name__}: {exc}"
                if is_oom(exc):
                    stop.set()
                    record = base_record(item, prompt_sha, prior_attempts + transport_tries, timestamp, latency)
                    record["error"] = last_error
                    record["prompt_tokens_local"] = prompt_tokens
                    append_record(output_path, record, lock)
                    raise SystemExit(f"GPU memory error. Stopped {MODEL_ID}. {last_error}") from exc
                if transport_index == max_attempts or not is_retryable(exc):
                    record = base_record(item, prompt_sha, prior_attempts + transport_tries, timestamp, latency)
                    record["error"] = last_error
                    record["prompt_tokens_local"] = prompt_tokens
                    append_record(output_path, record, lock)
                    print(f"FAILED {key[0]} {key[1]}: {last_error}", file=sys.stderr, flush=True)
                    return {"status": "error", "empty": True, "truncated": False, "patient_turn": False}
                delay = retry_initial * (retry_multiplier ** (transport_index - 1))
                print(f"RETRY {key[0]} {key[1]} in {delay:.1f}s: {last_error}", file=sys.stderr, flush=True)
                time.sleep(delay)
        if result is None:
            return {"status": "error", "empty": True, "truncated": False, "patient_turn": False}
        content_tries += 1
        text = result.response_text or ""
        finish = "" if result.finish_reason is None else str(result.finish_reason)
        record = base_record(item, prompt_sha, prior_attempts + transport_tries, timestamp, latency)
        record["model_version"] = result.model_version
        record["request_parameters"] = result.request_parameters
        record["response_text"] = text
        record["finish_reason"] = result.finish_reason
        record["token_usage"] = result.token_usage
        record["reasoning_token_count"] = 0
        record["prompt_tokens_local"] = prompt_tokens
        if has_text(text):
            record["error"] = None
            append_record(output_path, record, lock)
            print(f"ok {key[0]} {key[1]}", flush=True)
            return {
                "status": "ok",
                "empty": clean_text(text) == "",
                "truncated": finish in TRUNCATED,
                "patient_turn": "Patient:" in text,
                "server_prompt_tokens": result.token_usage.get("input_tokens"),
                "local_prompt_tokens": prompt_tokens,
            }
        record["error"] = "no text"
        append_record(output_path, record, lock)
        print(f"NO TEXT {key[0]} {key[1]} content try {content_tries}", file=sys.stderr, flush=True)
    return {"status": "error", "empty": True, "truncated": False, "patient_turn": False}


def assert_smoke(path: Path) -> None:
    chosen: dict[str, dict[str, object]] = {}
    if path.exists():
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                record = json.loads(line)
                if record.get("error") is None and has_text(record.get("response_text")):
                    chosen[str(record["condition"])] = record
    missing = [condition for condition in CONDITIONS if condition not in chosen]
    if missing:
        raise SystemExit(f"Smoke is missing non-empty turns for {missing}. The 4,824 was not started.")
    print("\n===== SMOKE DOCTOR TURNS =====", flush=True)
    for condition in CONDITIONS:
        record = chosen[condition]
        print(f"\n##### {condition} context={record['context_id']} #####", flush=True)
        print(analysis_text(record.get("response_text")), flush=True)


def summarise(path: Path) -> dict[str, int]:
    attempts = 0
    successes: set[tuple[str, str]] = set()
    failed: set[tuple[str, str]] = set()
    empty_analysis = 0
    input_tokens = 0
    output_tokens = 0
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            attempts += 1
            key = (str(record["context_id"]), str(record["condition"]))
            usage = record.get("token_usage") or {}
            input_tokens += int(usage.get("input_tokens") or 0)
            output_tokens += int(usage.get("output_tokens") or 0)
            if record.get("error") is None and has_text(record.get("response_text")):
                successes.add(key)
                failed.discard(key)
                if analysis_text(record.get("response_text")).strip() == "":
                    empty_analysis += 1
            elif key not in successes:
                failed.add(key)
    return {
        "attempts": attempts,
        "successes": len(successes),
        "failures": len(failed),
        "empty_analyses": empty_analysis,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
    }


def write_run_report(path: Path, study: str, output_path: Path, stats: dict[str, int]) -> None:
    lines = [
        f"# bio-medical Llama 3 {study} run",
        "",
        f"- model_id: `{MODEL_ID}`",
        "- source: mradermacher/Bio-Medical-MultiModal-Llama-3-8B-V1-i1-GGUF, Q4_K_S, base model ContactDoctor/Bio-Medical-MultiModal-Llama-3-8B-V1",
        "- server: `http://localhost:1234/v1`",
        "- endpoint: `POST /v1/chat/completions`",
        "- chat template: Llama 3 chat template. The system role is a real system header.",
        f"- context_length: {CONTEXT_LENGTH} (max_position_embeddings)",
        "- max_new_tokens: the tokens remaining inside that context. generation_config.json states no separate max_new_tokens.",
        "- stop: `<|eot_id|>` and `<|end_of_text|>`",
        f"- reasoning: {REASONING_SETTING}",
        f"- tokenizer: `{TOKENIZER_ID}`",
        "- sampling: temperature, top_p, and top_k omitted",
        f"- output: `{output_path.relative_to(PROJECT).as_posix()}`",
        "",
        f"- requests recorded: {stats['attempts']}",
        f"- successes: {stats['successes']}",
        f"- failures: {stats['failures']}",
        f"- empty analyses: {stats['empty_analyses']}",
        f"- input tokens: {stats['input_tokens']}",
        f"- output tokens: {stats['output_tokens']}",
        "- doctor API cost: 0",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"report {path}", flush=True)


def clean_table(jsonl_path: Path, csv_path: Path) -> None:
    import subprocess

    subprocess.check_call(
        [sys.executable, str(SRC_DIR / "postprocess.py"), "--input", str(jsonl_path), "--output", str(csv_path)],
    )


def contexts_for(phase: str, config: dict[str, object]) -> tuple[list[dict[str, str]], Path, Path, str]:
    if phase == "smoke":
        frozen = PROJECT / str(config["frozen_dir"]) / "p2_contexts_FROZEN.csv"
        rows = read_contexts(frozen)
        rows = sorted(rows, key=lambda item: item["context_id"])[:1]
        output = PROJECT / "outputs" / "smoke_not_data_biomedllama" / "smoke.jsonl"
        report = PROJECT / "reports" / "run_report_biomedllama_smoke.md"
        return rows, output, report, "smoke"
    if phase == "e1":
        frozen = PROJECT / str(config["frozen_dir"]) / "p2_contexts_FROZEN.csv"
        rows = read_contexts(frozen)
        if len(rows) != 804:
            raise SystemExit(f"Expected 804 frozen contexts, found {len(rows)}.")
        output = PROJECT / "outputs" / "main_biomedllama.jsonl"
        report = PROJECT / "reports" / "run_report_biomedllama_e1.md"
        return rows, output, report, "E1"
    if phase == "e2":
        path = PROJECT / "data" / "aci_bench" / "aci_contexts.csv"
        rows = read_contexts(path)
        if len(rows) != 612:
            raise SystemExit(f"Expected 612 ACI contexts, found {len(rows)}.")
        output = PROJECT / "outputs" / "aci_biomedllama.jsonl"
        report = PROJECT / "reports" / "run_report_biomedllama_e2.md"
        return rows, output, report, "E2"
    raise SystemExit(f"Unknown phase {phase}.")


def note_progress(outcome: dict[str, object], consecutive_errors: list[int], stop: threading.Event, phase: str) -> None:
    if outcome.get("status") == "skipped":
        return
    if outcome.get("status") == "error":
        consecutive_errors[0] += 1
        if consecutive_errors[0] >= 20:
            stop.set()
            raise SystemExit("Halted: 20 consecutive requests failed.")
        return
    consecutive_errors[0] = 0
    server_tokens = outcome.get("server_prompt_tokens")
    local_tokens = outcome.get("local_prompt_tokens")
    if (
        phase == "smoke"
        and isinstance(server_tokens, int)
        and isinstance(local_tokens, int)
        and abs(server_tokens - local_tokens) > 2
    ):
        stop.set()
        raise SystemExit(
            f"Tokenizer check failed: local {local_tokens} server {server_tokens}. The main run was not started."
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("smoke", "e1", "e2"), required=True)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    if args.workers < 1:
        raise SystemExit("--workers must be at least 1.")
    prompt_sha = verify_study_hashes()
    config = load_config(PROJECT / "config.yaml")
    rows, output_path, report_path, study = contexts_for(args.phase, config)
    if output_path.resolve() in {path.resolve() for path in PROTECTED}:
        raise SystemExit(f"Refusing to write onto an existing study output: {output_path}")
    if args.phase == "e1":
        assert_smoke(PROJECT / "outputs" / "smoke_not_data_biomedllama" / "smoke.jsonl")
        assert_early_stop_history(output_path)
    prompts = load_prompt_file(PROJECT / str(config["prompt_file"]))
    if text_sha256(PROJECT / str(config["prompt_file"])) != prompt_sha:
        raise SystemExit("Prompt file changed after the hash check.")
    items = build_items(rows, prompts)
    expected = len(rows) * 6
    if len(items) != expected:
        raise SystemExit(f"Expected {expected} requests, assembled {len(items)}.")
    print(f"model_id: {MODEL_ID}", flush=True)
    print(f"reasoning_setting: {REASONING_SETTING}", flush=True)
    print("sampling: temperature, top_p, and top_k omitted", flush=True)
    print("template: Llama 3 chat template on POST /v1/chat/completions", flush=True)
    print(f"requests: {len(items)} output: {output_path}", flush=True)
    done = completed_successes(output_path)
    prior = attempt_counts(output_path)
    pending = [item for item in items if (str(item["context_id"]), str(item["condition"])) not in done]
    print(f"Completed already: {len(done)}. Pending: {len(pending)}.", flush=True)
    if pending:
        tokenizer = load_tokenizer()
        provider = BioMedLlamaProvider()
        lock = threading.Lock()
        tokenizer_lock = threading.Lock()
        stop = threading.Event()
        max_attempts = int(config["max_attempts"])
        retry_initial = float(config["retry_initial_seconds"])
        retry_multiplier = float(config["retry_multiplier"])
        consecutive_errors = [0]
        first_gate = args.phase == "e1" and len(final_outcomes(output_path)) < 30
        head = pending[: max(0, 30 - len(final_outcomes(output_path)))] if first_gate else []
        tail = pending[len(head) :]

        def one(item: dict[str, object]) -> dict[str, object]:
            return run_item(
                item,
                provider,
                tokenizer,
                tokenizer_lock,
                prompt_sha,
                prior.get((str(item["context_id"]), str(item["condition"])), 0),
                output_path,
                lock,
                stop,
                max_attempts,
                retry_initial,
                retry_multiplier,
            )

        for item in head:
            if stop.is_set():
                break
            note_progress(one(item), consecutive_errors, stop, args.phase)
        if first_gate:
            assert_early_stop_history(output_path)
        if tail and not stop.is_set():
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                futures = [pool.submit(one, item) for item in tail]
                completed = 0
                for future in as_completed(futures):
                    outcome = future.result()
                    if outcome.get("status") == "skipped":
                        continue
                    note_progress(outcome, consecutive_errors, stop, args.phase)
                    completed += 1
                    if completed % 25 == 0:
                        print(f"progress {completed}/{len(tail)}", flush=True)
    if args.phase == "smoke":
        assert_smoke(output_path)
    else:
        stats = summarise(output_path)
        write_run_report(report_path, study, output_path, stats)
        csv_path = output_path.with_name(output_path.stem + "_cleaned.csv")
        clean_table(output_path, csv_path)
        print(
            f"{study} requests={stats['attempts']} successes={stats['successes']} "
            f"failures={stats['failures']} empty_analyses={stats['empty_analyses']} "
            f"input_tokens={stats['input_tokens']} output_tokens={stats['output_tokens']}",
            flush=True,
        )
        if stats["failures"]:
            raise SystemExit(f"{study} left {stats['failures']} keys failed.")


if __name__ == "__main__":
    main()
