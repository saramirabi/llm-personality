"""Local MedGemma 4B instruction-tuned doctor provider.

The checkpoint is Unsloth's Q4_K_S GGUF of google/medgemma-4b-it, served as
medgemma-4b-it. Its tokenizer chat template is the Gemma 3 conversational
template, and the loaded server applies that same template. System text is a
system role. The template prefixes it onto the first user turn.
"""

from __future__ import annotations

import threading

from openai import OpenAI

from providers.base import GenerationRequest, GenerationResult

MODEL_ID = "medgemma-4b-it"
BASE_URL = "http://localhost:1234/v1"
CONTEXT_LENGTH = 131072
TOKENIZER_ID = "unsloth/medgemma-4b-it"
# generation_config.json eos_token_id is [<eos>, <end_of_turn>].
STOP = ["<end_of_turn>", "<eos>"]
REASONING_SETTING = "no reasoning control on the model card; no thinking prompt added"


def count_prompt_tokens(tokenizer, system: str, user: str) -> int:
    return len(
        tokenizer.apply_chat_template(
            [{"role": "system", "content": system}, {"role": "user", "content": user}],
            tokenize=True,
            add_generation_prompt=True,
        )
    )


def output_limit(prompt_tokens: int) -> int:
    """New-token room left inside the 131072-token context. The card states no separate max_new_tokens."""
    remaining = CONTEXT_LENGTH - prompt_tokens
    if remaining < 1:
        raise RuntimeError(
            f"Prompt tokens {prompt_tokens} leave no room inside the {CONTEXT_LENGTH}-token context. "
            "The prompt was not truncated and the output limit was not lowered."
        )
    return remaining


class MedGemmaProvider:
    name = "medgemma"
    _call_lock = threading.Lock()

    def __init__(self, base_url: str = BASE_URL, timeout: float = 600) -> None:
        self._client = OpenAI(base_url=base_url, api_key="local", timeout=timeout, max_retries=0)

    def redact(self, text: str) -> str:
        return text

    def generate(self, request: GenerationRequest) -> GenerationResult:
        if request.model_id != MODEL_ID:
            raise RuntimeError(f"This provider only sends {MODEL_ID}.")
        if request.temperature is not None or request.top_p is not None or request.top_k is not None:
            raise RuntimeError("Sampling parameters are omitted so the checkpoint default is used.")
        if request.thinking_level is not None or request.thinking_budget is not None or request.reasoning_effort is not None:
            raise RuntimeError("MedGemma has no reasoning control. Do not send one.")
        if not request.user_text.endswith("Doctor:\n"):
            raise RuntimeError("The user string must end with Doctor:\\n.")
        if request.max_output_tokens < 1:
            raise RuntimeError("max_output_tokens must be at least 1.")
        messages = [
            {"role": "system", "content": request.system_instruction},
            {"role": "user", "content": request.user_text},
        ]
        parameters = {
            "model": request.model_id,
            "endpoint": "POST /v1/chat/completions",
            "system_delivery": "gemma3_chat_template_system_role",
            "chat_template": "unsloth/medgemma-4b-it Gemma 3 chat template",
            "messages": messages,
            "stop": list(STOP),
            "temperature": "omitted",
            "top_p": "omitted",
            "top_k": "omitted",
            "reasoning": REASONING_SETTING,
            "context_length": CONTEXT_LENGTH,
            "max_tokens": request.max_output_tokens,
            "tokenizer": TOKENIZER_ID,
        }
        with self._call_lock:
            completion = self._client.chat.completions.create(
                model=request.model_id,
                messages=messages,
                max_tokens=request.max_output_tokens,
                stop=list(STOP),
            )
        choice = completion.choices[0]
        message = choice.message
        usage = completion.usage
        token_usage: dict[str, int | None] = {}
        if usage is not None:
            token_usage["input_tokens"] = int(usage.prompt_tokens)
            token_usage["output_tokens"] = int(usage.completion_tokens)
        return GenerationResult(
            response_text=message.content,
            model_version=str(completion.model),
            finish_reason=None if choice.finish_reason is None else str(choice.finish_reason),
            token_usage=token_usage,
            request_parameters=parameters,
            error=None,
        )
