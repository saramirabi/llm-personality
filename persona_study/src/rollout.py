"""Experiment 2 multi-turn rollouts.

Dry run prints one doctor turn-2 request and one patient request and does not call a model API.
Live generation is --run. A response with no text is retried once; the blocked attempt stays in the JSONL.
"""

from __future__ import annotations

import argparse
import csv
import json
import queue
import random
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

SRC = Path(__file__).resolve().parent
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from build_pool import format_context, parse_transcript, read_transcript  # noqa: E402
from generate import is_retryable, load_config, sha256  # noqa: E402
from postprocess import analysis_text, write_rollout_cleaned  # noqa: E402
from prompting import _read_block, assemble_system, assemble_user, load_prompt_file  # noqa: E402
from providers.base import GenerationRequest  # noqa: E402
from turn_rules_v2 import CLOSING_RE, normalize_for_rules, split_sentences  # noqa: E402
from turn_rules_v3 import CLOSING_STATEMENT_RE, INCIDENTAL_CLOSING_Q_RE  # noqa: E402

DOCTOR_PROMPT_SHA = "5d91f7d1e52d4b6b3ec38d6b05ab9eef8d184113eb9597f52cd52de88bae7999"
CONDITIONS = ("P0", "P1", "P2", "P3", "P4", "P5")
PLACEHOLDER_D1 = "[PLACEHOLDER D1]"
PLACEHOLDER_PATIENT = "[PLACEHOLDER PATIENT REPLY]"

# Official context windows. Prompt tokens plus the output limit must fit.
# Gemini 2.5 Flash-Lite: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite
# Claude Haiku 4.5: https://platform.claude.com/docs/en/docs/about-claude/models/overview
# GPT-4o mini: https://developers.openai.com/api/docs/models/gpt-4o-mini
CONTEXT_WINDOWS = {
    "gemini-2.5-flash-lite": 1_048_576,
    "gemini-2.5-flash": 1_048_576,
    "claude-haiku-4-5-20251001": 200_000,
    "gpt-4o-mini-2024-07-18": 128_000,
    "gpt-5-nano-2025-08-07": 400_000,
    "med-llama3-8b": 8192,
    "llama-2-13b-chat@q8_0": 4096,
    "medgemma-4b-it": 131072,
    "bio-medical-multimodal-llama-3-8b-v1-i1": 8192,
    "bartowski/meta-llama-3-8b-instruct": 8192,
}
PATIENT_PROMPT_SHA = "f23b9c276788ac78fba6cdf889e2eb669c9bd82695e1d9ad663b0970802c5cf6"
# Experiment 1 returned no text for this subset cell, including its one retry.
SKIPPED_MISSING_EXPERIMENT1 = {("P2_003101", "P4")}


def doctor_specs(config: dict[str, object]) -> list[dict[str, object]]:
    return [
        {
            "slug": "gemini",
            "model_id": str(config["model_id"]),
            "max_output_tokens": int(config["max_output_tokens"]),
            "thinking_level": None,
            "thinking_budget": int(config["thinking_budget"]),
            "reasoning_effort": None,
            "reasoning_setting": f"thinking_budget={int(config['thinking_budget'])}",
            "system_delivery": "Gemini system_instruction",
            "sampling": "temperature, top_p, and top_k omitted",
            "cleaned_csv": "outputs/main_gemini_cleaned.csv",
        },
        {
            "slug": "claude",
            "model_id": str(config["claude_model_id"]),
            "max_output_tokens": int(config["claude_max_output_tokens"]),
            "thinking_level": None,
            "thinking_budget": None,
            "reasoning_effort": None,
            "reasoning_setting": "thinking_omitted_default_off",
            "system_delivery": "Messages API top-level system parameter",
            "sampling": "temperature omitted (API default 1.0); top_p omitted; top_k omitted",
            "cleaned_csv": "outputs/main_claude_cleaned.csv",
        },
        {
            "slug": "gpt",
            "model_id": str(config["gpt_model_id"]),
            "max_output_tokens": int(config["gpt_max_output_tokens"]),
            "thinking_level": None,
            "thinking_budget": None,
            "reasoning_effort": None if config.get("gpt_reasoning_effort") in (None, "", "omitted", "none") else str(config.get("gpt_reasoning_effort")),
            "reasoning_setting": "reasoning omitted; this model has no reasoning step" if config.get("gpt_reasoning_effort") in (None, "", "omitted", "none") else f"reasoning_effort={config.get('gpt_reasoning_effort')}",
            "system_delivery": "Chat Completions system role",
            "sampling": "temperature omitted; top_p omitted; top_k is not a Chat Completions parameter; service_tier omitted",
            "cleaned_csv": "outputs/main_gpt_cleaned.csv",
        },
        {
            "slug": "medllama",
            "model_id": "med-llama3-8b",
            "max_output_tokens": 512,
            "thinking_level": None,
            "thinking_budget": None,
            "reasoning_effort": None,
            "reasoning_setting": "no reasoning control on the model card; no thinking prompt added",
            "system_delivery": "chat_completions_system_role",
            "sampling": "temperature, top_p, and top_k omitted",
            "cleaned_csv": "outputs/main_medllama_cleaned.csv",
        },
        {
            "slug": "llama2chat",
            "model_id": "llama-2-13b-chat@q8_0",
            "max_output_tokens": 4096,
            "thinking_level": None,
            "thinking_budget": None,
            "reasoning_effort": None,
            "reasoning_setting": "no reasoning control on the model card; no thinking prompt added",
            "system_delivery": "llama2_chat_template_raw_completion",
            "sampling": "temperature, top_p, and top_k omitted",
            "cleaned_csv": "outputs/main_llama2chat_cleaned.csv",
        },
        {
            "slug": "medgemma",
            "model_id": "medgemma-4b-it",
            "max_output_tokens": 131072,
            "thinking_level": None,
            "thinking_budget": None,
            "reasoning_effort": None,
            "reasoning_setting": "no reasoning control on the model card; no thinking prompt added",
            "system_delivery": "gemma3_chat_template_system_role",
            "sampling": "temperature, top_p, and top_k omitted",
            "cleaned_csv": "outputs/main_medgemma_cleaned.csv",
        },
        {
            "slug": "biomedllama",
            "model_id": "bio-medical-multimodal-llama-3-8b-v1-i1",
            "max_output_tokens": 8192,
            "thinking_level": None,
            "thinking_budget": None,
            "reasoning_effort": None,
            "reasoning_setting": "no reasoning control on the model card; no thinking prompt added",
            "system_delivery": "llama3_chat_template_system_role",
            "sampling": "temperature, top_p, and top_k omitted",
            "cleaned_csv": "outputs/main_biomedllama_cleaned.csv",
        },
        {
            "slug": "llama3instruct",
            "model_id": "bartowski/meta-llama-3-8b-instruct",
            "max_output_tokens": 8192,
            "thinking_level": None,
            "thinking_budget": None,
            "reasoning_effort": None,
            "reasoning_setting": "no reasoning control on the model card; no thinking prompt added",
            "system_delivery": "llama3_instruct_chat_template_system_role",
            "sampling": "temperature, top_p, and top_k omitted",
            "cleaned_csv": "outputs/main_llama3instruct_cleaned.csv",
        },
    ]


def matching_sha256(path: Path, expected: str) -> str:
    """Return the study hash. A Windows checkout may store CRLF while the committed text is LF."""
    raw = sha256(path)
    if raw == expected:
        return raw
    import hashlib

    text = hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
    if text == expected:
        print(f"SHA-256 ok {path.name}", flush=True)
        return expected
    raise SystemExit(f"SHA-256 mismatch for {path.name}. expected={expected} raw={raw} text={text}")


def refuse_human_reference(path: Path) -> None:
    if "human_reference" in path.name or "human_reference" in path.as_posix():
        raise SystemExit(f"Generation code must not read {path}.")


def load_subset(path: Path) -> list[dict[str, str]]:
    refuse_human_reference(path)
    with path.open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row.get("in_subset") == "1"]
    dialogues = {row["dialogue_id"] for row in rows}
    positions: dict[str, int] = {}
    for row in rows:
        positions[row["position"]] = positions.get(row["position"], 0) + 1
    if len(rows) != 150 or len(dialogues) != 50 or positions != {"Early": 50, "Middle": 50, "Late": 50}:
        raise SystemExit(
            f"Subset check failed: rows={len(rows)} dialogues={len(dialogues)} positions={positions}."
        )
    return rows


def load_experiment1(path: Path, model_id: str, wanted: set[tuple[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    refuse_human_reference(path)
    csv.field_size_limit(min(sys.maxsize, 2_147_483_647))
    found: dict[tuple[str, str], dict[str, str]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            key = (row["context_id"], row["condition"])
            if key not in wanted or row.get("model_id") != model_id:
                continue
            if key in found:
                raise SystemExit(f"Duplicate Experiment 1 row for {key} in {path.name}.")
            found[key] = row
    missing = sorted(wanted - set(found))
    if missing:
        raise SystemExit(f"{path.name} is missing {len(missing)} subset rows. First: {missing[0]}.")
    empty = [key for key, row in found.items() if not (row.get("analysis_text") or "").strip()]
    if empty:
        raise SystemExit(f"{path.name} has an empty analysis_text for {empty[0]}.")
    return found


def case_record(dialogue_dir: Path, dialogue_id: str) -> str:
    path = dialogue_dir / f"{dialogue_id}.txt"
    refuse_human_reference(path)
    if not path.is_file():
        raise SystemExit(f"Missing transcript {path}.")
    text, _encoding = read_transcript(path)
    turns, _counts = parse_transcript(text)
    return format_context(turns)


def append_turn(history: str, label: str, text: str) -> str:
    block = f"{label}: {text.strip()}"
    if not history.strip():
        return block
    return history.rstrip("\n") + "\n\n" + block


def patient_history_text(raw: str | None) -> str:
    text = "" if raw is None else str(raw)
    if text.lstrip().startswith("Patient:"):
        text = text.lstrip()[len("Patient:") :]
    doctor_at = text.find("Doctor:")
    if doctor_at != -1:
        text = text[:doctor_at]
    return text.strip()


def closing_detected(text: str) -> bool:
    """Existing closing-phrase detectors. No new pattern."""
    normalized = normalize_for_rules(text or "")
    if CLOSING_RE.search(normalized) or CLOSING_STATEMENT_RE.search(normalized):
        return True
    for sentence in split_sentences(text or ""):
        if INCIDENTAL_CLOSING_Q_RE.match(normalize_for_rules(sentence)):
            return True
    return False


def load_patient_prompts(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    system = _read_block(lines, "patient_system")
    template = _read_block(lines, "patient_user_template")
    if "{case_record}" not in template or "{history}" not in template:
        raise SystemExit("Patient template is missing {case_record} or {history}.")
    return {"patient_system": system, "patient_user_template": template}


def assemble_patient(prompts: dict[str, str], case_record_text: str, history: str) -> str:
    return (
        prompts["patient_user_template"]
        .replace("{case_record}", case_record_text)
        .replace("{history}", history)
    )


_TOKENIZERS: dict[str, object] = {}


def count_tokens(model_id: str, system_text: str, user_text: str) -> tuple[int, str]:
    """Count with the model's own local tokenizer. No model API call."""
    if model_id in {"gemini-2.5-flash-lite", "gemini-2.5-flash"}:
        import warnings

        from google.genai.local_tokenizer import LocalTokenizer

        tokenizer = _TOKENIZERS.get(model_id)
        if tokenizer is None:
            tokenizer = LocalTokenizer(model_name=model_id)
            _TOKENIZERS[model_id] = tokenizer
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message=".*[Ll]ocal tokenizer.*")
            result = tokenizer.count_tokens(user_text, config={"system_instruction": system_text})
        return int(result.total_tokens), f"google.genai.local_tokenizer.LocalTokenizer for {model_id}"
    if model_id in {"gpt-4o-mini-2024-07-18", "gpt-5-nano-2025-08-07"}:
        import tiktoken

        try:
            encoding = tiktoken.encoding_for_model(model_id)
        except KeyError as exc:
            raise SystemExit(
                f"tiktoken.encoding_for_model({model_id!r}) has no official encoding. "
                "This step does not substitute another encoding."
            ) from exc
        count = len(encoding.encode(system_text)) + len(encoding.encode(user_text))
        return count, f"tiktoken.encoding_for_model({model_id}) name={encoding.name}; message-framing tokens are not in the cookbook for this model and were not added"
    if model_id == "med-llama3-8b":
        from transformers import AutoTokenizer

        from providers.medllama import SERVER_FRAMING_TOKENS, TOKENIZER_ID

        tokenizer = _TOKENIZERS.get(model_id)
        if tokenizer is None:
            tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_ID)
            _TOKENIZERS[model_id] = tokenizer
        count = len(tokenizer.encode(system_text)) + len(tokenizer.encode(user_text)) + SERVER_FRAMING_TOKENS
        return count, f"{TOKENIZER_ID} plus {SERVER_FRAMING_TOKENS} server framing tokens"
    if model_id == "llama-2-13b-chat@q8_0":
        from transformers import AutoTokenizer

        from providers.llama2chat import SERVER_BOS_TOKENS, TOKENIZER_ID, count_prompt_tokens

        tokenizer = _TOKENIZERS.get(model_id)
        if tokenizer is None:
            tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_ID)
            _TOKENIZERS[model_id] = tokenizer
        count = count_prompt_tokens(tokenizer, system_text, user_text)
        return count, f"{TOKENIZER_ID} Llama-2-Chat template plus {SERVER_BOS_TOKENS} server BOS token"
    if model_id == "medgemma-4b-it":
        from transformers import AutoTokenizer

        from providers.medgemma import TOKENIZER_ID, count_prompt_tokens

        tokenizer = _TOKENIZERS.get(model_id)
        if tokenizer is None:
            tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_ID)
            _TOKENIZERS[model_id] = tokenizer
        count = count_prompt_tokens(tokenizer, system_text, user_text)
        return count, f"{TOKENIZER_ID} Gemma 3 chat template"
    if model_id == "bio-medical-multimodal-llama-3-8b-v1-i1":
        from transformers import AutoTokenizer

        from providers.biomedllama import TOKENIZER_ID, count_prompt_tokens

        tokenizer = _TOKENIZERS.get(model_id)
        if tokenizer is None:
            tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_ID)
            _TOKENIZERS[model_id] = tokenizer
        count = count_prompt_tokens(tokenizer, system_text, user_text)
        return count, f"{TOKENIZER_ID} Llama 3 chat template"
    if model_id == "bartowski/meta-llama-3-8b-instruct":
        from transformers import AutoTokenizer

        from providers.llama3instruct import TOKENIZER_ID, count_prompt_tokens

        tokenizer = _TOKENIZERS.get(model_id)
        if tokenizer is None:
            tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_ID)
            _TOKENIZERS[model_id] = tokenizer
        count = count_prompt_tokens(tokenizer, system_text, user_text)
        return count, f"{TOKENIZER_ID} Llama 3 Instruct chat template"
    if model_id == "claude-haiku-4-5-20251001":
        raise SystemExit(
            "Claude Haiku 4.5 has no published local tokenizer. The official counter is "
            "POST /v1/messages/count_tokens, which is an API call. This step does not call it, "
            "so the Claude fit check was not run."
        )
    raise SystemExit(
        f"No official local tokenizer is configured for {model_id}. "
        "This step does not guess one, and it does not call a count API."
    )


def assert_fits(model_id: str, prompt_tokens: int, max_output_tokens: int) -> None:
    window = CONTEXT_WINDOWS.get(model_id)
    if window is None:
        raise SystemExit(f"No official context window is recorded for {model_id}.")
    if prompt_tokens + max_output_tokens > window:
        raise SystemExit(
            f"{model_id} does not fit: prompt tokens {prompt_tokens} + output limit "
            f"{max_output_tokens} = {prompt_tokens + max_output_tokens}, context window {window}. "
            "Nothing was truncated."
        )


def request_parameters(spec: dict[str, object]) -> dict[str, object]:
    return {
        "model_id": spec["model_id"],
        "max_output_tokens": spec["max_output_tokens"],
        "thinking_level": spec["thinking_level"],
        "thinking_budget": spec["thinking_budget"],
        "reasoning_effort": spec["reasoning_effort"],
        "temperature": None,
        "top_p": None,
        "top_k": None,
        "system_delivery": spec["system_delivery"],
        "sampling": spec["sampling"],
    }


def completed_turns(path: Path) -> set[tuple[str, str, int, str]]:
    done: set[tuple[str, str, int, str]] = set()
    if not path.exists():
        return done
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("error") is not None:
                continue
            if record.get("reused_from_experiment1") or record.get("raw_response") is not None:
                done.add((record["context_id"], record["condition"], int(record["turn"]), record["role"]))
    return done


def append_record(path: Path, record: dict[str, object], lock: threading.Lock) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, ensure_ascii=False) + "\n"
    with lock:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(line)


def make_provider(spec: dict[str, object], config: dict[str, object]):
    slug = spec["slug"]
    if slug == "gemini" or (slug == "patient" and str(spec["model_id"]).startswith("gemini")):
        from providers.gemini import GeminiProvider

        return GeminiProvider(str(config["gemini_api_key_env"]))
    if slug == "claude":
        from providers.claude import ClaudeProvider

        return ClaudeProvider(str(config["anthropic_api_key_env"]))
    if slug == "gpt":
        from providers.gpt import GPTProvider

        return GPTProvider(str(config["openai_api_key_env"]))
    if slug == "medllama":
        from providers.medllama import MedLlamaProvider

        return MedLlamaProvider()
    if slug == "llama2chat":
        from providers.llama2chat import Llama2ChatProvider

        return Llama2ChatProvider()
    if slug == "medgemma":
        from providers.medgemma import MedGemmaProvider

        return MedGemmaProvider()
    if slug == "biomedllama":
        from providers.biomedllama import BioMedLlamaProvider

        return BioMedLlamaProvider()
    if slug == "llama3instruct":
        from providers.llama3instruct import Llama3InstructProvider

        return Llama3InstructProvider()
    raise SystemExit(f"Unknown doctor model slug {slug}.")


def is_payment_or_quota(text: str) -> bool:
    """HTTP 402 or 429. These pause a run; they do not mark a rollout incomplete."""
    if text.startswith("402") or text.startswith("429") or text.startswith("HTTP 402") or text.startswith("HTTP 429"):
        return True
    markers = (
        "'code': 402",
        '"code": 402',
        "'code': 429",
        '"code": 429',
        "status_code=402",
        "status_code=429",
        "HTTP 402",
        "HTTP 429",
    )
    return any(marker in text for marker in markers)


def is_pause_exception(exc: Exception) -> bool:
    code = getattr(exc, "code", None) or getattr(exc, "status_code", None)
    if code in (402, 429):
        return True
    return is_payment_or_quota(str(exc))


def generate_once(provider, request: GenerationRequest, max_attempts: int, initial: float, multiplier: float):
    import time

    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            result = provider.generate(request)
        except Exception as exc:
            last_error = exc
            if is_pause_exception(exc):
                code = getattr(exc, "code", None) or getattr(exc, "status_code", None)
                prefix = f"HTTP {code} " if code in (402, 429) else ""
                return None, f"{prefix}{exc}", attempt
            if attempt == max_attempts or not is_retryable(exc):
                return None, str(exc), attempt
            time.sleep(initial * (multiplier ** (attempt - 1)))
            continue
        if result.error:
            return result, result.error, attempt
        if result.response_text is None or not str(result.response_text).strip():
            return result, "no output returned", attempt
        return result, None, attempt
    return None, str(last_error), max_attempts


# The two Gemini doctor turns that returned PROHIBITED_CONTENT with no text.
BLOCKED_GEMINI = {
    ("P2_001509", "P3"): (2, "doctor"),
    ("P2_004885", "P5"): (4, "doctor"),
}


def _records_for_turn(path: Path, context_id: str, condition: str, turn: int, role: str) -> list[dict[str, object]]:
    found: list[dict[str, object]] = []
    if not path.exists():
        return found
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if (
                record.get("context_id") == context_id
                and record.get("condition") == condition
                and int(record.get("turn", -1)) == turn
                and record.get("role") == role
            ):
                found.append(record)
    return found


TURN_SEQUENCE = [(1, "doctor"), (1, "patient"), (2, "doctor"), (2, "patient"), (3, "doctor"), (3, "patient"), (4, "doctor")]


def record_turn_state(record: dict[str, object]) -> str:
    raw = record.get("raw_response")
    has_text = raw is not None and str(raw).strip()
    if record.get("error") is None and (record.get("reused_from_experiment1") or has_text):
        return "ok"
    error = str(record.get("error") or "")
    if is_payment_or_quota(error):
        return "payment"
    if error == "no output returned" or (record.get("finish_reason") and not has_text):
        return "content"
    return "error"


def rollout_states(path: Path) -> dict[tuple[str, str], str]:
    """Latest state of each started rollout. Payment pauses are not incomplete."""
    turns: dict[tuple[str, str], dict[tuple[int, str], str]] = {}
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            key = (str(record["context_id"]), str(record["condition"]))
            slot = (int(record["turn"]), str(record["role"]))
            state = record_turn_state(record)
            current = turns.setdefault(key, {})
            if state == "ok" or current.get(slot) != "ok":
                current[slot] = state
    classes: dict[tuple[str, str], str] = {}
    for key, slots in turns.items():
        outcomes = [slots.get(step) for step in TURN_SEQUENCE]
        if all(item == "ok" for item in outcomes):
            classes[key] = "complete"
        elif any(item == "content" for item in outcomes):
            classes[key] = "incomplete"
        elif any(item == "error" for item in outcomes):
            classes[key] = "other_error"
        else:
            classes[key] = "paused"
    return classes


def returned_no_output_records(path: Path, context_id: str, condition: str, turn: int, role: str) -> list[dict[str, object]]:
    """Stored API responses that came back with no text. Transport errors are not included."""
    blocked: list[dict[str, object]] = []
    for record in _records_for_turn(path, context_id, condition, turn, role):
        raw = record.get("raw_response")
        if record.get("error") is None:
            continue
        if raw is not None and str(raw).strip():
            continue
        if record.get("error") != "no output returned" and not record.get("finish_reason"):
            continue
        blocked.append(record)
    return blocked


def request_mismatch(stored: dict[str, object], request: GenerationRequest) -> str | None:
    """None when the rebuilt request is the stored blocked request."""
    params = stored.get("request_parameters")
    if not isinstance(params, dict):
        return "The stored blocked request has no parameters, so the retry was not sent."
    if "contents" in params and isinstance(params.get("config"), dict):
        config = params["config"]
        thinking = config.get("thinking_config") if isinstance(config.get("thinking_config"), dict) else {}
        checks = {
            "model": params.get("model") == request.model_id,
            "contents": params.get("contents") == request.user_text,
            "system_instruction": config.get("system_instruction") == request.system_instruction,
            "max_output_tokens": config.get("max_output_tokens") == request.max_output_tokens,
            "thinking_budget": thinking.get("thinking_budget") == request.thinking_budget,
        }
    elif params.get("transport") == "messages.stream":
        messages = params.get("messages")
        content = messages[0].get("content") if isinstance(messages, list) and messages else None
        checks = {
            "model": params.get("model") == request.model_id,
            "system": params.get("system") == request.system_instruction,
            "user": content == request.user_text,
            "max_tokens": params.get("max_tokens") == request.max_output_tokens,
            "thinking": params.get("thinking") == "omitted" and request.thinking_budget is None and request.thinking_level is None,
        }
    elif params.get("system_delivery") == "chat_completions_system_role":
        messages = params.get("messages")
        system = messages[0].get("content") if isinstance(messages, list) and len(messages) > 0 else None
        user = messages[1].get("content") if isinstance(messages, list) and len(messages) > 1 else None
        checks = {
            "model": params.get("model") == request.model_id,
            "system": system == request.system_instruction,
            "user": user == request.user_text,
            "max_completion_tokens": (
                params.get("max_completion_tokens")
                if "max_completion_tokens" in params
                else params.get("max_tokens")
            ) == request.max_output_tokens,
            "reasoning_effort": params.get("reasoning_effort") == request.reasoning_effort,
        }
    elif params.get("system_delivery") == "llama2_chat_template_raw_completion":
        messages = params.get("messages")
        system = messages[0].get("content") if isinstance(messages, list) and len(messages) > 0 else None
        user = messages[1].get("content") if isinstance(messages, list) and len(messages) > 1 else None
        checks = {
            "model": params.get("model") == request.model_id,
            "system": system == request.system_instruction,
            "user": user == request.user_text,
            "max_tokens": params.get("max_tokens") == request.max_output_tokens,
            "stop": params.get("stop") == ["</s>"],
        }
    elif params.get("system_delivery") == "gemma3_chat_template_system_role":
        messages = params.get("messages")
        system = messages[0].get("content") if isinstance(messages, list) and len(messages) > 0 else None
        user = messages[1].get("content") if isinstance(messages, list) and len(messages) > 1 else None
        checks = {
            "model": params.get("model") == request.model_id,
            "system": system == request.system_instruction,
            "user": user == request.user_text,
            "max_tokens": params.get("max_tokens") == request.max_output_tokens,
            "stop": params.get("stop") == ["<end_of_turn>", "<eos>"],
        }
    elif params.get("system_delivery") == "llama3_chat_template_system_role":
        messages = params.get("messages")
        system = messages[0].get("content") if isinstance(messages, list) and len(messages) > 0 else None
        user = messages[1].get("content") if isinstance(messages, list) and len(messages) > 1 else None
        checks = {
            "model": params.get("model") == request.model_id,
            "system": system == request.system_instruction,
            "user": user == request.user_text,
            "max_tokens": params.get("max_tokens") == request.max_output_tokens,
            "stop": params.get("stop") == ["<|eot_id|>", "<|end_of_text|>"],
        }
    elif params.get("system_delivery") == "llama3_instruct_chat_template_system_role":
        messages = params.get("messages")
        system = messages[0].get("content") if isinstance(messages, list) and len(messages) > 0 else None
        user = messages[1].get("content") if isinstance(messages, list) and len(messages) > 1 else None
        checks = {
            "model": params.get("model") == request.model_id,
            "system": system == request.system_instruction,
            "user": user == request.user_text,
            "max_tokens": params.get("max_tokens") == request.max_output_tokens,
            "stop": params.get("stop") == ["<|eot_id|>", "<|end_of_text|>"],
        }
    else:
        return "The stored request shape is not recognised, so the retry was not sent."
    mismatched = [name for name, ok in checks.items() if not ok]
    if not mismatched:
        return None
    return (
        "The rebuilt request does not match the stored blocked request "
        f"({', '.join(mismatched)}). The retry was not sent."
    )


def dry_run(project_dir: Path, config: dict[str, object]) -> None:
    frozen = project_dir / str(config["frozen_dir"]) / str(config["main_frozen_filename"])
    subset = load_subset(frozen)
    wanted = {(row["context_id"], condition) for row in subset for condition in CONDITIONS}
    specs = doctor_specs(config)
    indexes = {}
    for spec in specs:
        indexes[spec["slug"]] = load_experiment1(project_dir / str(spec["cleaned_csv"]), str(spec["model_id"]), wanted)

    dialogue_dir = Path(str(config["osce_dialogues_path"]))
    cases: dict[str, str] = {}
    for dialogue_id in sorted({row["dialogue_id"] for row in subset}):
        cases[dialogue_id] = case_record(dialogue_dir, dialogue_id)
    mismatches = []
    for row in subset:
        full = cases[row["dialogue_id"]]
        context = row["context"].strip()
        if not full.startswith(context):
            mismatches.append(row["context_id"])
    if mismatches:
        raise SystemExit(
            f"{len(mismatches)} frozen contexts are not a prefix of the full transcript. First: {mismatches[0]}."
        )

    doctor_prompts = load_prompt_file(project_dir / str(config["prompt_file"]))
    doctor_sha = sha256(project_dir / str(config["prompt_file"]))
    if doctor_sha != DOCTOR_PROMPT_SHA:
        raise SystemExit(f"Doctor prompt SHA changed: {doctor_sha}")
    patient_path = project_dir / str(config["patient_prompt_file"])
    patient_prompts = load_patient_prompts(patient_path)
    patient_sha = sha256(patient_path)

    example = sorted(subset, key=lambda row: row["context_id"])[0]
    condition = "P0"
    spec = specs[0]
    d1 = indexes[spec["slug"]][(example["context_id"], condition)]["analysis_text"]
    history_after_d1 = append_turn(example["context"], "Doctor", PLACEHOLDER_D1)
    history_for_d2 = append_turn(history_after_d1, "Patient", PLACEHOLDER_PATIENT)
    system_text = assemble_system(doctor_prompts, condition)
    user_text = assemble_user(doctor_prompts, history_for_d2)
    patient_user = assemble_patient(patient_prompts, cases[example["dialogue_id"]], history_after_d1)

    print(f"rollouts_per_doctor_model: {len(subset) * len(CONDITIONS)}")
    print("turns_per_rollout: D1 reused, then patient, D2, patient, D3, patient, D4")
    print("generated_requests_per_rollout: 6")
    print(f"generated_requests_per_doctor_model: {len(subset) * len(CONDITIONS) * 6}")
    print(f"records_per_doctor_model_including_reused_D1: {len(subset) * len(CONDITIONS) * 7}")
    print(f"experiment1_D1_matches: " + ", ".join(f"{item['slug']}={len(indexes[item['slug']])}" for item in specs))
    print(f"doctor_prompt_sha256: {doctor_sha}")
    print(f"patient_prompt_sha256: {patient_sha}")
    print(
        "example_rollout: "
        f"context_id={example['context_id']} dialogue_id={example['dialogue_id']} "
        f"position={example['position']} condition={condition} doctor_model={spec['model_id']}"
    )
    print(f"placeholder_D1: {PLACEHOLDER_D1}")
    print(f"placeholder_patient_reply_used_only_so_turn_2_has_a_history: {PLACEHOLDER_PATIENT}")
    print(f"real_experiment1_D1_not_used_in_this_print: {d1}")
    print("local_models_configured: none")
    print()
    print("===== DOCTOR REQUEST TURN 2 =====")
    print(f"model_id: {spec['model_id']}")
    print(f"reasoning_setting: {spec['reasoning_setting']}")
    print(f"system_prompt_delivery: {spec['system_delivery']}")
    print(f"sampling: {spec['sampling']}")
    print(f"max_output_tokens: {spec['max_output_tokens']}")
    print("--- system ---")
    print(system_text, end="" if system_text.endswith("\n") else "\n")
    print("--- user ---")
    print(user_text, end="" if user_text.endswith("\n") else "\n")
    print()
    print("===== PATIENT REQUEST AFTER D1 =====")
    patient_model = config.get("patient_model_id")
    print(f"patient_model_id: {patient_model if patient_model else 'NOT SET'}")
    print(f"prompt_file_sha256: {patient_sha}")
    print("--- system ---")
    print(patient_prompts["patient_system"], end="" if str(patient_prompts["patient_system"]).endswith("\n") else "\n")
    print("--- user ---")
    print(patient_user, end="" if patient_user.endswith("\n") else "\n")
    print()

    print("===== CONTEXT WINDOW CHECK =====")
    gemini = specs[0]
    gpt = specs[2]
    worst: dict[str, tuple[int, str]] = {}
    for item in (gemini, gpt):
        model_id = str(item["model_id"])
        peak = 0
        peak_id = ""
        for row in subset:
            for cond in CONDITIONS:
                system = assemble_system(doctor_prompts, cond)
                user = assemble_user(doctor_prompts, row["context"])
                tokens, method = count_tokens(model_id, system, user)
                assert_fits(model_id, tokens, int(item["max_output_tokens"]))
                if tokens > peak:
                    peak = tokens
                    peak_id = row["context_id"] + " " + cond
        turn2_tokens, method = count_tokens(model_id, system_text, user_text)
        assert_fits(model_id, turn2_tokens, int(item["max_output_tokens"]))
        worst[model_id] = (peak, peak_id)
        window = CONTEXT_WINDOWS[model_id]
        print(
            f"{model_id}: tokenizer={method}; frozen-context doctor prompts checked="
            f"{len(subset) * len(CONDITIONS)}; largest_prompt_tokens={peak} at {peak_id}; "
            f"output_limit={item['max_output_tokens']}; context_window={window}; "
            f"largest_plus_output_limit={peak + int(item['max_output_tokens'])}; "
            f"printed_turn2_prompt_tokens={turn2_tokens}; fits=yes"
        )
    print(
        "claude-haiku-4-5-20251001: context_window=200000 output_limit=64000. "
        "No published local tokenizer. Official counter is POST /v1/messages/count_tokens. "
        "That is an API call, so it was not used. Claude fit was not asserted."
    )
    if not patient_model:
        print(
            "patient: patient_model_id is not in config.yaml. "
            "The patient request was not token-counted and its fit was not asserted."
        )
    print("truncation: none")


def _assert_blocked_gemini(path: Path) -> None:
    """Stop before any call unless the only incomplete Gemini rollouts are the two blocked doctor turns."""
    sequence = [(1, "doctor"), (1, "patient"), (2, "doctor"), (2, "patient"), (3, "doctor"), (3, "patient"), (4, "doctor")]
    present: dict[tuple[str, str, int, str], str] = {}
    error_count = 0
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            key = (str(record["context_id"]), str(record["condition"]), int(record["turn"]), str(record["role"]))
            if record.get("error") is None and (record.get("reused_from_experiment1") or record.get("raw_response") is not None):
                present[key] = "ok"
            elif record.get("error") is not None:
                error_count += 1
                present.setdefault(key, "error")
    started = {(context_id, condition) for context_id, condition, _turn, _role in present}
    incomplete = []
    for context_id, condition in started:
        if not all(present.get((context_id, condition, turn, role)) == "ok" for turn, role in sequence):
            incomplete.append((context_id, condition))
    if sorted(incomplete) != sorted(BLOCKED_GEMINI):
        raise SystemExit(
            f"Incomplete Gemini rollouts are {incomplete}. Expected only the two blocked requests. No retry was sent."
        )
    if error_count != 2:
        raise SystemExit(f"Expected 2 blocked Gemini records, found {error_count}. No retry was sent.")
    for (context_id, condition), (turn, role) in BLOCKED_GEMINI.items():
        blocked = returned_no_output_records(path, context_id, condition, turn, role)
        if len(blocked) != 1:
            raise SystemExit(f"{context_id} {condition} does not have exactly one no-output record. No retry was sent.")
        record = blocked[0]
        if record.get("finish_reason") != "PROHIBITED_CONTENT" or int(record.get("attempt_count") or 0) != 1:
            raise SystemExit(f"{context_id} {condition} turn {turn} is not the stored PROHIBITED_CONTENT attempt. No retry was sent.")
        if present.get((context_id, condition, turn, role)) != "error":
            raise SystemExit(f"{context_id} {condition} turn {turn} is not the failed turn. No retry was sent.")
        failed_at = sequence.index((turn, role))
        for later_turn, later_role in sequence[failed_at + 1 :]:
            if present.get((context_id, condition, later_turn, later_role)) is not None:
                raise SystemExit(f"{context_id} {condition} already has a later turn. No retry was sent.")


def probe_patient_billing(config: dict[str, object]) -> None:
    """One short patient-model call. No rollout file is written."""
    from providers.gemini import GeminiProvider

    provider = GeminiProvider(str(config["gemini_api_key_env"]))
    request = GenerationRequest(
        model_id=str(config["patient_model_id"]),
        system_instruction="Reply with one word.",
        user_text="Reply with ok.",
        max_output_tokens=32,
        thinking_budget=int(config["patient_thinking_budget"]),
    )
    try:
        result = provider.generate(request)
    except Exception as exc:
        raise SystemExit(f"Patient billing test failed: {provider.redact(str(exc))}") from exc
    text = "" if result.response_text is None else str(result.response_text).strip()
    if result.error or not text:
        raise SystemExit(
            f"Patient billing test returned no text. finish_reason={result.finish_reason} error={result.error}"
        )
    print("patient_billing_test: ok", flush=True)


def run_live(project_dir: Path, config: dict[str, object], doctor_slug: str, only_blocked: bool = False) -> None:
    patient_model = config.get("patient_model_id")
    if not patient_model:
        raise SystemExit("patient_model_id is not set. No patient request was sent.")
    if str(patient_model) not in CONTEXT_WINDOWS:
        raise SystemExit(f"No official context window is recorded for patient model {patient_model}.")
    frozen = project_dir / str(config["frozen_dir"]) / str(config["main_frozen_filename"])
    subset = load_subset(frozen)
    wanted = {(row["context_id"], condition) for row in subset for condition in CONDITIONS}
    expected_rollouts = 900
    if doctor_slug == "medllama":
        missing = wanted & SKIPPED_MISSING_EXPERIMENT1
        if missing != SKIPPED_MISSING_EXPERIMENT1:
            raise SystemExit(f"Expected to skip {sorted(SKIPPED_MISSING_EXPERIMENT1)}, found {sorted(missing)}.")
        wanted -= SKIPPED_MISSING_EXPERIMENT1
        expected_rollouts = 899
        print("skipped_missing_experiment1: P2_003101 P4", flush=True)
    specs = doctor_specs(config)
    spec = next(item for item in specs if item["slug"] == doctor_slug)
    doctor_prompts = load_prompt_file(project_dir / str(config["prompt_file"]))
    doctor_prompt_path = project_dir / str(config["prompt_file"])
    doctor_sha = matching_sha256(doctor_prompt_path, DOCTOR_PROMPT_SHA)
    patient_path = project_dir / str(config["patient_prompt_file"])
    if patient_path.name != "p2_patient_v2.yaml":
        raise SystemExit(f"Rollouts must use p2_patient_v2.yaml, found {patient_path.name}.")
    patient_prompts = load_patient_prompts(patient_path)
    patient_sha = matching_sha256(patient_path, PATIENT_PROMPT_SHA)
    dialogue_dir = Path(str(config["osce_dialogues_path"]))
    if not dialogue_dir.is_dir():
        fallback = Path("data/raw")
        if not fallback.is_dir():
            raise SystemExit(f"Transcript directory does not exist: {dialogue_dir}")
        print(f"osce_dialogues_path is not on this machine. Using {fallback}", flush=True)
        dialogue_dir = fallback
    cases = {row["dialogue_id"]: case_record(dialogue_dir, row["dialogue_id"]) for row in subset}
    rollout_dir = project_dir / str(config["rollout_dir"])
    max_attempts = int(config["max_attempts"])
    initial = float(config["retry_initial_seconds"])
    multiplier = float(config["retry_multiplier"])
    patient_spec = _patient_spec(config, specs)
    index = load_experiment1(project_dir / str(spec["cleaned_csv"]), str(spec["model_id"]), wanted)
    output_path = rollout_dir / f"{spec['slug']}.jsonl"
    jsonl_before = output_path.read_bytes() if output_path.exists() else b""
    lines_before = jsonl_before.count(b"\n")
    if only_blocked:
        if doctor_slug != "gemini":
            raise SystemExit("The blocked-request retry applies only to the stored Gemini rollouts.")
        _assert_blocked_gemini(output_path)
    done = completed_turns(output_path)
    doctor_provider = make_provider(spec, config)
    patient_provider = doctor_provider if spec["slug"] == "gemini" else make_provider(patient_spec, config)
    lock = threading.Lock()
    stop = threading.Event()
    fail_lock = threading.Lock()
    tokenizer_lock = threading.Lock()
    consecutive_failures = 0
    window_checked = 0
    largest_prompt = {str(spec["model_id"]): 0, str(patient_spec["model_id"]): 0}
    checked_models: set[str] = set()
    halt_reason = ""
    context_overflows: list[str] = []
    order = [(row, condition) for row in subset for condition in CONDITIONS]
    if len(order) != 900:
        raise SystemExit(f"Expected 900 rollouts, found {len(order)}.")
    random.Random(20261002).shuffle(order)
    if doctor_slug == "medllama":
        order = [item for item in order if (item[0]["context_id"], item[1]) not in SKIPPED_MISSING_EXPERIMENT1]
        if len(order) != expected_rollouts:
            raise SystemExit(f"Expected {expected_rollouts} rollouts after the skip, found {len(order)}.")
    print(f"patient_model_id: {patient_spec['model_id']}", flush=True)
    print(f"patient_reasoning_setting: thinking_budget={patient_spec['thinking_budget']}", flush=True)
    print(f"patient_prompt_sha256: {patient_sha}", flush=True)
    print(f"doctor_model_id: {spec['model_id']}", flush=True)
    print("shuffle_seed: 20261002", flush=True)
    print(f"rollouts: {len(order)}", flush=True)

    def note_request(failed: bool) -> None:
        nonlocal consecutive_failures, halt_reason
        with fail_lock:
            if failed:
                consecutive_failures += 1
                if consecutive_failures >= 20:
                    halt_reason = "20 consecutive requests failed."
                    stop.set()
            else:
                consecutive_failures = 0

    def count_claude_tokens(system_text: str, user_text: str) -> int:
        import time

        last_error: Exception | None = None
        for attempt in range(1, max_attempts + 1):
            try:
                with tokenizer_lock:
                    return doctor_provider.count_prompt_tokens(str(spec["model_id"]), system_text, user_text)
            except Exception as exc:
                last_error = exc
                if is_pause_exception(exc) or attempt == max_attempts or not is_retryable(exc):
                    raise
                time.sleep(initial * (multiplier ** (attempt - 1)))
        raise RuntimeError(str(last_error))

    def check_window(model_id: str, system_text: str, user_text: str, limit: int) -> None:
        nonlocal window_checked, halt_reason
        try:
            if model_id == "claude-haiku-4-5-20251001":
                tokens = count_claude_tokens(system_text, user_text)
            else:
                with tokenizer_lock:
                    tokens, _method = count_tokens(model_id, system_text, user_text)
        except SystemExit:
            raise
        except Exception as exc:
            message = doctor_provider.redact(f"{type(exc).__name__}: {exc}")
            halt_reason = f"Token count failed for {model_id}: {message}"
            stop.set()
            raise SystemExit(halt_reason) from exc
        with fail_lock:
            window_checked += 1
            checked_models.add(model_id)
            if tokens > largest_prompt[model_id]:
                largest_prompt[model_id] = tokens
        try:
            assert_fits(model_id, tokens, limit)
        except SystemExit as exc:
            halt_reason = str(exc)
            stop.set()
            raise

    def execute(row: dict[str, str], condition: str) -> str:
        nonlocal halt_reason, context_overflows
        history = row["context"]
        sequence = [(1, "doctor"), (1, "patient"), (2, "doctor"), (2, "patient"), (3, "doctor"), (3, "patient"), (4, "doctor")]
        for turn, role in sequence:
            if stop.is_set():
                return "stopped"
            key = (row["context_id"], condition, turn, role)
            if key in done:
                history = _extend_from_saved(output_path, row["context_id"], condition, turn, role, history)
                continue
            if role == "doctor" and turn == 1:
                source = index[(row["context_id"], condition)]
                text = source["analysis_text"]
                record = _base_record(row, condition, spec, turn, role, doctor_sha)
                record.update(
                    {
                        "model_id": spec["model_id"],
                        "model_version": source.get("model_version"),
                        "doctor_model_version": source.get("model_version"),
                        "request_parameters": {"reused_from_experiment1": True},
                        "raw_response": source.get("response_text"),
                        "analysis_text": text,
                        "finish_reason": source.get("finish_reason"),
                        "token_usage": None,
                        "attempt_count": 0,
                        "reused_from_experiment1": True,
                        "closing_detected": closing_detected(text),
                        "error": None,
                    }
                )
                append_record(output_path, record, lock)
                history = append_turn(history, "Doctor", analysis_text(text))
                continue
            if role == "doctor":
                active = spec
                system_text = assemble_system(doctor_prompts, condition)
                user_text = assemble_user(doctor_prompts, history)
                prompt_hash = doctor_sha
                label = "Doctor"
            else:
                active = patient_spec
                system_text = patient_prompts["patient_system"]
                user_text = assemble_patient(patient_prompts, cases[row["dialogue_id"]], history)
                prompt_hash = patient_sha
                label = "Patient"
            limit = int(active["max_output_tokens"])
            if role == "doctor" and str(active["model_id"]) in {
                "llama-2-13b-chat@q8_0",
                "medgemma-4b-it",
                "bio-medical-multimodal-llama-3-8b-v1-i1",
                "bartowski/meta-llama-3-8b-instruct",
            }:
                if str(active["model_id"]) == "llama-2-13b-chat@q8_0":
                    from providers.llama2chat import output_limit as local_output_limit
                elif str(active["model_id"]) == "medgemma-4b-it":
                    from providers.medgemma import output_limit as local_output_limit
                elif str(active["model_id"]) == "bio-medical-multimodal-llama-3-8b-v1-i1":
                    from providers.biomedllama import output_limit as local_output_limit
                else:
                    from providers.llama3instruct import output_limit as local_output_limit

                try:
                    with tokenizer_lock:
                        doctor_tokens, _method = count_tokens(str(active["model_id"]), system_text, user_text)
                    limit = local_output_limit(doctor_tokens)
                except RuntimeError as exc:
                    if str(active["model_id"]) in {
                        "llama-2-13b-chat@q8_0",
                        "bio-medical-multimodal-llama-3-8b-v1-i1",
                        "bartowski/meta-llama-3-8b-instruct",
                    } and "leave no room" in str(exc):
                        note = (
                            f"{row['context_id']} {condition} doctor turn {turn}: {exc} "
                            "This rollout stopped at that turn. The other rollouts continued."
                        )
                        context_overflows.append(note)
                        print(f"context_overflow {note}", flush=True)
                        record = _base_record(row, condition, spec, turn, role, prompt_hash)
                        record.update(_result_fields(active, None, None, "", 0, str(exc), False))
                        record["doctor_model_id"] = spec["model_id"]
                        append_record(output_path, record, lock)
                        return "incomplete"
                    halt_reason = str(exc)
                    stop.set()
                    return "stopped"
            try:
                check_window(str(active["model_id"]), system_text, user_text, limit)
            except SystemExit:
                return "stopped"
            if stop.is_set():
                return "stopped"
            request = GenerationRequest(
                model_id=str(active["model_id"]),
                system_instruction=system_text,
                user_text=user_text,
                max_output_tokens=limit,
                thinking_level=active["thinking_level"],
                thinking_budget=active["thinking_budget"],
                reasoning_effort=active["reasoning_effort"],
            )
            active_provider = doctor_provider if role == "doctor" else patient_provider
            prior_attempt = 0
            for earlier in _records_for_turn(output_path, row["context_id"], condition, turn, role):
                prior_attempt = max(prior_attempt, int(earlier.get("attempt_count") or 0))
            while True:
                blocked = returned_no_output_records(output_path, row["context_id"], condition, turn, role)
                if len(blocked) >= 2:
                    return "incomplete"
                if blocked:
                    mismatch = request_mismatch(blocked[-1], request)
                    if mismatch:
                        raise SystemExit(f"{row['context_id']} {condition} turn {turn} {role}: {mismatch}")
                if stop.is_set():
                    return "stopped"
                result, error, attempts = generate_once(active_provider, request, max_attempts, initial, multiplier)
                raw = None if result is None else result.response_text
                if result is None and error and is_payment_or_quota(error):
                    error = active_provider.redact(error)
                    stored = ""
                    record = _base_record(row, condition, spec, turn, role, prompt_hash)
                    record.update(_result_fields(active, result, None, stored, prior_attempt + attempts, error, False))
                    record["doctor_model_id"] = spec["model_id"]
                    append_record(output_path, record, lock)
                    halt_reason = (
                        "Paused on HTTP 402 or 429. The affected rollout was left resumable "
                        "and was not marked incomplete."
                    )
                    stop.set()
                    return "paused"
                empty = result is not None and (raw is None or str(raw).strip() == "")
                if empty:
                    error = error or "no output returned"
                    raw = None
                stored = analysis_text(raw) if role == "doctor" else patient_history_text(raw)
                record = _base_record(row, condition, spec, turn, role, prompt_hash)
                record.update(_result_fields(active, result, raw, stored, prior_attempt + attempts, error, False))
                record["doctor_model_id"] = spec["model_id"]
                append_record(output_path, record, lock)
                prior_attempt += attempts
                if error is None and raw is not None and str(raw).strip():
                    note_request(False)
                    history = append_turn(history, label, stored)
                    if stop.is_set():
                        return "stopped"
                    break
                note_request(True)
                if stop.is_set():
                    return "stopped"
                if not empty:
                    return "incomplete"
        return "complete"

    def run_pairs(pairs: list[tuple[dict[str, str], str]]) -> list[str]:
        statuses: list[str] = []
        for index_number, (row, condition) in enumerate(pairs, start=1):
            if stop.is_set():
                break
            status = execute(row, condition)
            statuses.append(status)
            print(f"rollout {index_number} {row['context_id']} {condition} {status}", flush=True)
            if status == "stopped":
                break
        return statuses

    output_limits = {
        str(spec["model_id"]): int(spec["max_output_tokens"]),
        str(patient_spec["model_id"]): int(patient_spec["max_output_tokens"]),
    }
    if str(spec["model_id"]) == "claude-haiku-4-5-20251001":
        print("doctor_token_count: POST /v1/messages/count_tokens", flush=True)

    def run_queue(pairs: list[tuple[dict[str, str], str]]) -> None:
        work: queue.Queue[tuple[dict[str, str], str]] = queue.Queue()
        for item in pairs:
            work.put(item)
        workers = min(int(config["concurrency"]), max(1, len(pairs)))

        def worker() -> None:
            while not stop.is_set():
                try:
                    row, condition = work.get_nowait()
                except queue.Empty:
                    return
                status = execute(row, condition)
                print(f"rollout {row['context_id']} {condition} {status}", flush=True)

        with ThreadPoolExecutor(max_workers=workers) as pool:
            running = [pool.submit(worker) for _ in range(workers)]
            for job in running:
                job.result()

    resume_targets: list[tuple[str, str]] = []
    try:
        if only_blocked:
            selected = [item for item in order if (item[0]["context_id"], item[1]) in BLOCKED_GEMINI]
            if len(selected) != len(BLOCKED_GEMINI):
                raise SystemExit("The two blocked Gemini rollouts were not in the shuffled 900. No retry was sent.")
            print("retry_blocked: P2_001509 P3 doctor turn 2; P2_004885 P5 doctor turn 4", flush=True)
            run_pairs(selected)
            if halt_reason:
                print(f"halt: {halt_reason}", flush=True)
        elif lines_before and doctor_slug in {"medllama", "llama2chat", "medgemma", "biomedllama", "llama3instruct"}:
            states = rollout_states(output_path)
            held = [
                item
                for item in order
                if states.get((item[0]["context_id"], item[1])) in {"incomplete", "other_error", "paused"}
            ]
            fresh_pairs = [item for item in order if (item[0]["context_id"], item[1]) not in states]
            complete_pairs = [item for item in order if states.get((item[0]["context_id"], item[1])) == "complete"]
            print(f"already_complete: {len(complete_pairs)}", flush=True)
            print(f"resume_incomplete: {len(held)}", flush=True)
            print(f"resume_not_started: {len(fresh_pairs)}", flush=True)
            probe_patient_billing(config)
            run_pairs(held + fresh_pairs)
            if halt_reason:
                print(f"halt: {halt_reason}", flush=True)
        elif lines_before and doctor_slug == "gpt":
            states = rollout_states(output_path)
            held = [
                item
                for item in order
                if states.get((item[0]["context_id"], item[1])) in {"incomplete", "other_error", "paused"}
            ]
            fresh_pairs = [item for item in order if (item[0]["context_id"], item[1]) not in states]
            complete_pairs = [item for item in order if states.get((item[0]["context_id"], item[1])) == "complete"]
            print(f"already_complete: {len(complete_pairs)}", flush=True)
            print(f"resume_incomplete: {len(held)}", flush=True)
            print(f"resume_not_started: {len(fresh_pairs)}", flush=True)
            probe_patient_billing(config)
            run_queue(held + fresh_pairs)
            if halt_reason:
                print(f"halt: {halt_reason}", flush=True)
        elif lines_before:
            states = rollout_states(output_path)
            payment_pairs = [item for item in order if states.get((item[0]["context_id"], item[1])) == "paused"]
            fresh_pairs = [item for item in order if (item[0]["context_id"], item[1]) not in states]
            complete_pairs = [item for item in order if states.get((item[0]["context_id"], item[1])) == "complete"]
            held = [
                item
                for item in order
                if states.get((item[0]["context_id"], item[1])) in {"incomplete", "other_error"}
            ]
            expected_counts = {"claude": (476, 24, 400), "gpt": (0, 20, 880)}
            expected = expected_counts.get(str(spec["slug"]))
            actual = (len(complete_pairs), len(payment_pairs), len(fresh_pairs))
            if held or expected != actual:
                raise SystemExit(
                    f"{spec['slug']} resume set is complete={len(complete_pairs)} "
                    f"paused={len(payment_pairs)} not_started={len(fresh_pairs)} held={len(held)}. "
                    "No request was sent."
                )
            resume_targets = [(item[0]["context_id"], item[1]) for item in payment_pairs]
            print(f"resume_paused: {len(payment_pairs)}", flush=True)
            print(f"resume_not_started: {len(fresh_pairs)}", flush=True)
            print(f"already_complete: {len(complete_pairs)}", flush=True)
            probe_patient_billing(config)
            run_queue(payment_pairs)
            if halt_reason:
                print(f"halt: {halt_reason}", flush=True)
            else:
                run_queue(fresh_pairs)
                if halt_reason:
                    print(f"halt: {halt_reason}", flush=True)
            now = rollout_states(output_path)
            resumed_complete = sum(now.get(key) == "complete" for key in resume_targets)
            print(f"resumed_rollouts: {len(resume_targets)}", flush=True)
            print(f"resumed_now_complete: {resumed_complete}", flush=True)
        else:
            probe_patient_billing(config)
            first_statuses = run_pairs(order[:20])
            incomplete_first = sum(status == "incomplete" for status in first_statuses)
            if halt_reason:
                print(f"halt: {halt_reason}", flush=True)
            elif len(first_statuses) == 20 and incomplete_first > 2:
                halt_reason = f"{incomplete_first} of the first 20 rollouts were incomplete."
                print(f"halt: {halt_reason}", flush=True)
            elif len(first_statuses) == 20:
                run_queue(order[20:])
                if halt_reason:
                    print(f"halt: {halt_reason}", flush=True)
    finally:
        if jsonl_before and output_path.exists() and not output_path.read_bytes().startswith(jsonl_before):
            raise SystemExit(f"{output_path.name} was not append-only. Earlier rollouts were modified.")

    if context_overflows:
        print(f"context_overflows: {len(context_overflows)}", flush=True)
        for note in context_overflows:
            print(f"context_overflow {note}", flush=True)
    if str(spec["model_id"]) in {
        "llama-2-13b-chat@q8_0",
        "medgemma-4b-it",
        "bio-medical-multimodal-llama-3-8b-v1-i1",
        "bartowski/meta-llama-3-8b-instruct",
    }:
        peak = largest_prompt.get(str(spec["model_id"]), 0)
        output_limits[str(spec["model_id"])] = CONTEXT_WINDOWS[str(spec["model_id"])] - peak
    cleaned_path = rollout_dir / f"{spec['slug']}_cleaned.csv"
    if output_path.exists():
        written = write_rollout_cleaned(output_path, cleaned_path)
        print(f"cleaned_rollout_rows: {written}", flush=True)
    summarize_rollouts(
        output_path,
        expected_rollouts,
        window_checked,
        largest_prompt,
        halt_reason,
        usage_after_line=0 if doctor_slug in {"medllama", "llama2chat", "medgemma", "biomedllama", "llama3instruct", "gpt"} else (lines_before if lines_before else 0),
        output_limits=output_limits,
        checked_models=checked_models,
    )


def _usage_parts(model_id: str, usage: dict[str, object]) -> tuple[int, int, int, int, str]:
    """Return prompt, cached, cache-write, output, and whether cached tokens sit inside prompt."""
    if "prompt_token_count" in usage or model_id.startswith("gemini"):
        prompt = int(usage.get("prompt_token_count") or 0)
        cached = int(usage.get("cached_content_token_count") or 0)
        candidates = int(usage.get("candidates_token_count") or 0)
        thoughts = int(usage.get("thoughts_token_count") or 0)
        total = usage.get("total_token_count")
        output = candidates
        if thoughts and total is not None and int(total) == prompt + candidates + thoughts:
            output += thoughts
        return prompt, cached, 0, output, "included"
    if model_id.startswith("claude"):
        return (
            int(usage.get("input_tokens") or 0),
            int(usage.get("cache_read_input_tokens") or 0),
            int(usage.get("cache_creation_input_tokens") or 0),
            int(usage.get("output_tokens") or 0),
            "separate",
        )
    return (
        int(usage.get("input_tokens") or 0),
        int(usage.get("cached_tokens") or 0),
        int(usage.get("cache_write_tokens") or 0),
        int(usage.get("output_tokens") or 0),
        "included",
    )


def summarize_rollouts(
    path: Path,
    expected: int,
    window_checked: int,
    largest_prompt: dict[str, int],
    halt_reason: str,
    usage_after_line: int = 0,
    output_limits: dict[str, int] | None = None,
    checked_models: set[str] | None = None,
) -> None:
    # Input, cache-read, cache-write, output, per million tokens.
    # Gemini cache reads are the published cache price. Claude cache write is the 5-minute price.
    # GPT cached input is the published cached price. A GPT cache-write field is printed and not given a second price.
    rates = {
        "gemini-2.5-flash-lite": (0.10, 0.01, 0.0, 0.40),
        "gemini-2.5-flash": (0.30, 0.03, 0.0, 2.50),
        "claude-haiku-4-5-20251001": (1.0, 0.10, 1.25, 5.0),
        "gpt-4o-mini-2024-07-18": (0.15, 0.075, 0.0, 0.60),
        "gpt-5-nano-2025-08-07": (0.05, 0.005, 0.0, 0.40),
        "med-llama3-8b": (0.0, 0.0, 0.0, 0.0),
        "llama-2-13b-chat@q8_0": (0.0, 0.0, 0.0, 0.0),
        "medgemma-4b-it": (0.0, 0.0, 0.0, 0.0),
        "bio-medical-multimodal-llama-3-8b-v1-i1": (0.0, 0.0, 0.0, 0.0),
        "bartowski/meta-llama-3-8b-instruct": (0.0, 0.0, 0.0, 0.0),
    }
    present: dict[tuple[str, str, int, str], str] = {}
    usage_rows: list[tuple[str, dict[str, object]]] = []
    if path.exists():
        with path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                record = json.loads(line)
                key = (str(record["context_id"]), str(record["condition"]), int(record["turn"]), str(record["role"]))
                state = record_turn_state(record)
                if state == "ok":
                    present[key] = "ok"
                elif present.get(key) != "ok":
                    present[key] = state
                if (
                    line_number > usage_after_line
                    and record.get("role") in {"doctor", "patient"}
                    and not record.get("reused_from_experiment1")
                    and record.get("token_usage")
                ):
                    usage_rows.append((str(record["role"]), record))
    started = {(context_id, condition) for context_id, condition, _turn, _role in present}
    counts = {"complete": 0, "incomplete": 0, "paused": 0, "other_error": 0}
    for context_id, condition in started:
        outcomes = [present.get((context_id, condition, turn, role)) for turn, role in TURN_SEQUENCE]
        if all(item == "ok" for item in outcomes):
            counts["complete"] += 1
        elif any(item == "content" for item in outcomes):
            counts["incomplete"] += 1
        elif any(item == "error" for item in outcomes):
            counts["other_error"] += 1
        else:
            counts["paused"] += 1
    print(f"rollouts_complete: {counts['complete']}", flush=True)
    print(f"rollouts_incomplete: {counts['incomplete']}", flush=True)
    print(f"rollouts_paused: {counts['paused']}", flush=True)
    if counts["other_error"]:
        print(f"rollouts_other_error: {counts['other_error']}", flush=True)
    print(f"rollouts_not_started: {expected - len(started)}", flush=True)
    if usage_after_line:
        print(f"usage_scope: appended calls after line {usage_after_line}", flush=True)
    totals: dict[tuple[str, str], dict[str, int]] = {}
    styles: dict[str, str] = {}
    for role, record in usage_rows:
        model_id = str(record["model_id"])
        usage = record["token_usage"]
        if not isinstance(usage, dict):
            continue
        prompt, cached, cache_write, output, style = _usage_parts(model_id, usage)
        styles[model_id] = style
        bucket = totals.setdefault((role, model_id), {"prompt": 0, "cached": 0, "cache_write": 0, "output": 0, "calls": 0})
        bucket["prompt"] += prompt
        bucket["cached"] += cached
        bucket["cache_write"] += cache_write
        bucket["output"] += output
        bucket["calls"] += 1
    for (role, model_id), bucket in totals.items():
        input_rate, cache_rate, cache_write_rate, output_rate = rates[model_id]
        if styles[model_id] == "separate":
            uncached = bucket["prompt"]
            cost = (
                uncached * input_rate
                + bucket["cached"] * cache_rate
                + bucket["cache_write"] * cache_write_rate
                + bucket["output"] * output_rate
            ) / 1_000_000
        else:
            uncached = bucket["prompt"] - bucket["cached"]
            cost = (uncached * input_rate + bucket["cached"] * cache_rate + bucket["output"] * output_rate) / 1_000_000
        print(
            f"{role}_model: {model_id} calls={bucket['calls']} prompt_tokens={bucket['prompt']} "
            f"cached_tokens={bucket['cached']} cache_write_tokens={bucket['cache_write']} "
            f"output_tokens={bucket['output']} cost_usd={cost:.6f}",
            flush=True,
        )
    print(f"context_window_checks: {window_checked}", flush=True)
    limits = output_limits or {}
    shown = checked_models if checked_models is not None else set(largest_prompt)
    for model_id, tokens in largest_prompt.items():
        if model_id not in shown:
            continue
        limit = limits.get(model_id)
        if limit is None:
            raise SystemExit(f"No output limit was recorded for {model_id}.")
        window = CONTEXT_WINDOWS[model_id]
        print(
            f"context_window {model_id}: largest_prompt_tokens={tokens} output_limit={limit} "
            f"sum={tokens + limit} window={window} fits={'yes' if tokens + limit <= window else 'no'}",
            flush=True,
        )
    if halt_reason:
        print(f"halted: {halt_reason}", flush=True)
    else:
        print("context_window_result: every checked request fit; nothing was truncated", flush=True)


def _extend_from_saved(path: Path, context_id: str, condition: str, turn: int, role: str, history: str) -> str:
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if (
                record.get("context_id") == context_id
                and record.get("condition") == condition
                and int(record.get("turn", -1)) == turn
                and record.get("role") == role
                and record.get("error") is None
            ):
                label = "Doctor" if role == "doctor" else "Patient"
                text = record.get("analysis_text") or ""
                return append_turn(history, label, str(text))
    raise SystemExit(f"Completed turn {context_id} {condition} {turn} {role} has no stored text.")


def _base_record(row: dict[str, str], condition: str, spec: dict[str, object], turn: int, role: str, prompt_hash: str) -> dict[str, object]:
    return {
        "context_id": row["context_id"],
        "dialogue_id": row["dialogue_id"],
        "position": row["position"],
        "condition": condition,
        "doctor_model_id": spec["model_id"],
        "doctor_model_version": None,
        "turn": turn,
        "role": role,
        "prompt_file_hash": prompt_hash,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def _result_fields(spec, result, raw, text, attempts: int, error: str | None, reused: bool) -> dict[str, object]:
    version = None if result is None else result.model_version
    return {
        "model_id": spec["model_id"],
        "model_version": version,
        "doctor_model_version": version if spec.get("slug") else version,
        "request_parameters": {} if result is None else result.request_parameters,
        "raw_response": raw,
        "analysis_text": text,
        "finish_reason": None if result is None else result.finish_reason,
        "token_usage": None if result is None else result.token_usage,
        "attempt_count": attempts,
        "reused_from_experiment1": reused,
        "closing_detected": closing_detected(text or ""),
        "error": error,
    }


def _patient_spec(config: dict[str, object], specs: list[dict[str, object]]) -> dict[str, object]:
    model_id = str(config["patient_model_id"])
    for spec in specs:
        if spec["model_id"] == model_id:
            return spec
    if model_id == "gemini-2.5-flash" and int(config["patient_thinking_budget"]) == 0:
        return {
            "slug": "patient",
            "model_id": model_id,
            "max_output_tokens": int(config["patient_max_output_tokens"]),
            "thinking_level": None,
            "thinking_budget": 0,
            "reasoning_effort": None,
            "system_delivery": "Gemini system_instruction",
            "sampling": "temperature, top_p, and top_k omitted",
        }
    raise SystemExit(
        f"patient_model_id {model_id} has no recorded request settings, so no patient request was sent."
    )


def first_middle_pilot(path: Path) -> dict[str, str]:
    refuse_human_reference(path)
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("position") == "Middle":
                return row
    raise SystemExit(f"No Middle-position context in {path.name}.")


def pilot_d1(path: Path, context_id: str) -> dict[str, dict[str, object]]:
    refuse_human_reference(path)
    found: dict[str, dict[str, object]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("context_id") != context_id or record.get("model_id") != "gemini-2.5-flash-lite":
                continue
            if record.get("error") is not None or record.get("response_text") is None:
                continue
            condition = str(record["condition"])
            if condition in found:
                raise SystemExit(f"Duplicate pilot D1 for {context_id} {condition}.")
            found[condition] = record
    missing = [condition for condition in CONDITIONS if condition not in found]
    if missing:
        raise SystemExit(f"Pilot output has no D1 for {missing}.")
    return found


def smoke_test(project_dir: Path, config: dict[str, object]) -> None:
    patient_id = str(config["patient_model_id"])
    patient_budget = int(config["patient_thinking_budget"])
    print(f"patient_model_id: {patient_id}", flush=True)
    print(f"reasoning_setting: thinking_budget={patient_budget}", flush=True)
    if patient_id != "gemini-2.5-flash" or patient_budget != 0:
        raise SystemExit("Smoke test expects gemini-2.5-flash with thinking_budget 0.")
    patient_limit = int(config["patient_max_output_tokens"])
    if patient_limit != 65536:
        raise SystemExit("Patient output limit is not the documented 65536.")

    row = first_middle_pilot(project_dir / str(config["frozen_dir"]) / str(config["pilot_frozen_filename"]))
    print(
        f"smoke_context: {row['context_id']} dialogue_id={row['dialogue_id']} position={row['position']}",
        flush=True,
    )
    print("doctor_model_id: gemini-2.5-flash-lite", flush=True)
    print("doctor_reasoning_setting: thinking_budget=0", flush=True)
    print("storage: outputs/smoke_not_data_v2 (not experiment data)", flush=True)

    d1 = pilot_d1(project_dir / "outputs/pilot_gemini.jsonl", row["context_id"])
    doctor_prompts = load_prompt_file(project_dir / str(config["prompt_file"]))
    doctor_sha = sha256(project_dir / str(config["prompt_file"]))
    if doctor_sha != DOCTOR_PROMPT_SHA:
        raise SystemExit(f"Doctor prompt SHA changed: {doctor_sha}")
    patient_path = project_dir / str(config["patient_prompt_file"])
    if patient_path.name != "p2_patient_v2.yaml":
        raise SystemExit(f"Rollouts must use p2_patient_v2.yaml, found {patient_path.name}.")
    patient_prompts = load_patient_prompts(patient_path)
    patient_sha = sha256(patient_path)
    print(f"patient_prompt_sha256: {patient_sha}", flush=True)
    full_case = case_record(Path(str(config["osce_dialogues_path"])), row["dialogue_id"])
    if not full_case.startswith(row["context"].strip()):
        raise SystemExit(f"{row['context_id']} is not a prefix of its transcript.")

    doctor = next(item for item in doctor_specs(config) if item["slug"] == "gemini")
    if doctor["model_id"] != "gemini-2.5-flash-lite" or doctor["thinking_budget"] != 0:
        raise SystemExit("Doctor smoke model is not gemini-2.5-flash-lite with thinking_budget 0.")
    patient = {
        "slug": "patient",
        "model_id": patient_id,
        "max_output_tokens": patient_limit,
        "thinking_level": None,
        "thinking_budget": 0,
        "reasoning_effort": None,
        "system_delivery": "Gemini system_instruction",
        "sampling": "temperature, top_p, and top_k omitted",
    }
    output_path = project_dir / "outputs/smoke_not_data_v2" / f"{row['context_id']}_gemini.jsonl"
    done = completed_turns(output_path)
    from providers.gemini import GeminiProvider

    provider = GeminiProvider(str(config["gemini_api_key_env"]))
    lock = threading.Lock()
    max_attempts = int(config["max_attempts"])
    initial = float(config["retry_initial_seconds"])
    multiplier = float(config["retry_multiplier"])
    sequence = [(1, "doctor"), (1, "patient"), (2, "doctor"), (2, "patient"), (3, "doctor"), (3, "patient"), (4, "doctor")]

    for condition in CONDITIONS:
        history = row["context"]
        for turn, role in sequence:
            key = (row["context_id"], condition, turn, role)
            if key in done:
                history = _extend_from_saved(output_path, row["context_id"], condition, turn, role, history)
                continue
            if role == "doctor" and turn == 1:
                source = d1[condition]
                text = analysis_text(str(source.get("response_text")))
                record = _base_record(row, condition, doctor, turn, role, doctor_sha)
                record.update(
                    {
                        "model_id": doctor["model_id"],
                        "model_version": source.get("model_version"),
                        "doctor_model_version": source.get("model_version"),
                        "request_parameters": {"copied_from_pilot": True},
                        "raw_response": source.get("response_text"),
                        "analysis_text": text,
                        "finish_reason": source.get("finish_reason"),
                        "token_usage": source.get("token_usage"),
                        "attempt_count": source.get("attempt_count"),
                        "reused_from_experiment1": False,
                        "copied_from_pilot": True,
                        "not_experiment_data": True,
                        "closing_detected": closing_detected(text),
                        "error": None,
                    }
                )
                append_record(output_path, record, lock)
                history = append_turn(history, "Doctor", text)
                print(f"copied D1 {condition}", flush=True)
                continue
            if role == "doctor":
                spec = doctor
                system_text = assemble_system(doctor_prompts, condition)
                user_text = assemble_user(doctor_prompts, history)
                prompt_hash = doctor_sha
                label = "Doctor"
                stored_text = None
            else:
                spec = patient
                system_text = patient_prompts["patient_system"]
                user_text = assemble_patient(patient_prompts, full_case, history)
                prompt_hash = patient_sha
                label = "Patient"
                stored_text = None
            tokens, _method = count_tokens(str(spec["model_id"]), system_text, user_text)
            limit = int(spec["max_output_tokens"])
            if str(spec["model_id"]) in {
                "llama-2-13b-chat@q8_0",
                "medgemma-4b-it",
                "bio-medical-multimodal-llama-3-8b-v1-i1",
                "bartowski/meta-llama-3-8b-instruct",
            } and role == "doctor":
                if str(spec["model_id"]) == "llama-2-13b-chat@q8_0":
                    from providers.llama2chat import output_limit as local_output_limit
                elif str(spec["model_id"]) == "medgemma-4b-it":
                    from providers.medgemma import output_limit as local_output_limit
                elif str(spec["model_id"]) == "bio-medical-multimodal-llama-3-8b-v1-i1":
                    from providers.biomedllama import output_limit as local_output_limit
                else:
                    from providers.llama3instruct import output_limit as local_output_limit

                limit = local_output_limit(tokens)
            assert_fits(str(spec["model_id"]), tokens, limit)
            request = GenerationRequest(
                model_id=str(spec["model_id"]),
                system_instruction=system_text,
                user_text=user_text,
                max_output_tokens=limit,
                thinking_level=spec["thinking_level"],
                thinking_budget=spec["thinking_budget"],
                reasoning_effort=spec["reasoning_effort"],
            )
            result, error, attempts = generate_once(provider, request, max_attempts, initial, multiplier)
            raw = None if result is None else result.response_text
            if role == "doctor":
                stored_text = analysis_text(raw)
            else:
                stored_text = patient_history_text(raw)
            record = _base_record(row, condition, doctor, turn, role, prompt_hash)
            record.update(_result_fields(spec, result, raw, stored_text, attempts, error, False))
            record["copied_from_pilot"] = False
            record["not_experiment_data"] = True
            record["doctor_model_id"] = doctor["model_id"]
            record["doctor_model_version"] = None if result is None or role == "patient" else result.model_version
            append_record(output_path, record, lock)
            if error or raw is None:
                raise SystemExit(f"No output for {condition} turn {turn} {role}: {error}")
            history = append_turn(history, label, stored_text)
            print(f"generated {condition} {role} turn {turn}", flush=True)

    print_smoke_conversations(output_path)


def print_smoke_conversations(path: Path) -> None:
    chosen: dict[tuple[str, int, str], dict[str, object]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("error") is not None:
                continue
            chosen[(str(record["condition"]), int(record["turn"]), str(record["role"]))] = record
    print("\n===== SMOKE CONVERSATIONS =====", flush=True)
    for condition in CONDITIONS:
        print(f"\n##### {condition} #####", flush=True)
        for turn, role in ((1, "doctor"), (1, "patient"), (2, "doctor"), (2, "patient"), (3, "doctor"), (3, "patient"), (4, "doctor")):
            record = chosen.get((condition, turn, role))
            if record is None:
                raise SystemExit(f"Missing stored turn {condition} {turn} {role}.")
            label = "Doctor" if role == "doctor" else "Patient"
            print(f"{label}: {record.get('analysis_text')}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--doctor", choices=("gemini", "claude", "gpt", "medllama", "llama2chat", "medgemma", "biomedllama", "llama3instruct"))
    parser.add_argument("--retry-blocked", action="store_true")
    args = parser.parse_args()
    if sum((args.dry_run, args.run, args.smoke)) != 1:
        raise SystemExit("Pass exactly one of --dry-run, --run, or --smoke.")
    project_dir = Path(__file__).resolve().parents[1]
    config = load_config(project_dir / "config.yaml")
    if args.dry_run:
        dry_run(project_dir, config)
        return
    if args.smoke:
        smoke_test(project_dir, config)
        return
    if args.doctor is None:
        raise SystemExit("Pass --doctor.")
    if args.retry_blocked:
        if args.doctor != "gemini":
            raise SystemExit("--retry-blocked applies only to the stored Gemini rollouts.")
        run_live(project_dir, config, "gemini", only_blocked=True)
        return
    if args.doctor == "gemini":
        raise SystemExit("Gemini rollouts are already stored. Refusing to run them again.")
    run_live(project_dir, config, args.doctor)


if __name__ == "__main__":
    main()
