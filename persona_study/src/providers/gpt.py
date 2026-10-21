"""OpenAI Chat Completions provider.

The system prompt is a Chat Completions message with role "system".
gpt-4o-mini-2024-07-18 has no reasoning step, so reasoning_effort is omitted.
temperature, top_p, and service_tier are omitted so the API defaults apply.
top_k is not a Chat Completions parameter.
The API key is read from the environment and is never stored on the result.
"""

from __future__ import annotations

import os

from openai import OpenAI

from providers.base import GenerationRequest, GenerationResult


class GPTProvider:
    name = "gpt"

    def __init__(self, api_key_env: str = "OPENAI_API_KEY") -> None:
        api_key = os.environ.get(api_key_env)
        if not api_key:
            raise RuntimeError(
                f"Set {api_key_env} in the environment. Do not put the key in a file."
            )
        self._api_key = api_key
        self._client = OpenAI(api_key=api_key)

    def redact(self, text: str) -> str:
        if self._api_key and self._api_key in text:
            return text.replace(self._api_key, "[REDACTED]")
        return text

    def generate(self, request: GenerationRequest) -> GenerationResult:
        if request.thinking_level is not None or request.thinking_budget is not None:
            raise RuntimeError("Do not send a Gemini thinking setting to the OpenAI API.")
        if request.temperature is not None or request.top_p is not None or request.top_k is not None:
            raise RuntimeError("Sampling parameters are omitted so the model default is used.")
        if request.reasoning_effort not in (None, "minimal"):
            raise RuntimeError("Reasoning is omitted for gpt-4o-mini. Only minimal is accepted for a reasoning GPT model.")
        parameters = {
            "model": request.model_id,
            "max_completion_tokens": request.max_output_tokens,
            "system_delivery": "chat_completions_system_role",
            "messages": [
                {"role": "system", "content": request.system_instruction},
                {"role": "user", "content": request.user_text},
            ],
            "reasoning_effort": "omitted" if request.reasoning_effort is None else request.reasoning_effort,
            "temperature": "omitted",
            "top_p": "omitted",
            "service_tier": "omitted",
        }
        kwargs = {
            "model": request.model_id,
            "messages": [
                {"role": "system", "content": request.system_instruction},
                {"role": "user", "content": request.user_text},
            ],
            "max_completion_tokens": request.max_output_tokens,
        }
        if request.reasoning_effort is not None:
            kwargs["reasoning_effort"] = request.reasoning_effort
        completion = self._client.chat.completions.create(**kwargs)
        choice = completion.choices[0]
        message = choice.message
        usage = completion.usage
        token_usage: dict[str, int | None] = {}
        if usage is not None:
            token_usage["input_tokens"] = int(usage.prompt_tokens)
            token_usage["output_tokens"] = int(usage.completion_tokens)
            details = usage.completion_tokens_details
            reasoning_tokens = None if details is None else getattr(details, "reasoning_tokens", None)
            token_usage["reasoning_tokens"] = 0 if reasoning_tokens is None else int(reasoning_tokens)
            prompt_details = usage.prompt_tokens_details
            if prompt_details is not None:
                cached_tokens = getattr(prompt_details, "cached_tokens", None)
                cache_write_tokens = getattr(prompt_details, "cache_write_tokens", None)
                if cached_tokens is not None:
                    token_usage["cached_tokens"] = int(cached_tokens)
                if cache_write_tokens is not None:
                    token_usage["cache_write_tokens"] = int(cache_write_tokens)
        if completion.service_tier is not None:
            parameters["service_tier_returned"] = completion.service_tier
        return GenerationResult(
            response_text=message.content,
            model_version=str(completion.model),
            finish_reason=None if choice.finish_reason is None else str(choice.finish_reason),
            token_usage=token_usage,
            request_parameters=parameters,
            error=None,
        )
