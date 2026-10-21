"""Gemini Developer API provider.

Uses google-genai generate_content, which returns finish_reason, usage_metadata,
and model_version. Official docs (checked October 2026) also offer the newer
Interactions API; this provider stays on generate_content because that is the
documented call that exposes those three fields in google-genai 2.17.0.

Sampling and thinking parameters are omitted unless the caller sets them, so
the model default is used. max_output_tokens is always sent. The API key is
read from the environment and is never returned in request_parameters.
"""

from __future__ import annotations

import os

from google import genai
from google.genai import types

from providers.base import GenerationRequest, GenerationResult


class GeminiProvider:
    name = "gemini"

    def __init__(self, api_key_env: str = "GEMINI_API_KEY") -> None:
        api_key = os.environ.get(api_key_env) or os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError(
                f"Set {api_key_env} or GOOGLE_API_KEY in the environment. Do not put the key in a file."
            )
        self._api_key = api_key
        self._client = genai.Client(api_key=api_key)

    def redact(self, text: str) -> str:
        if self._api_key and self._api_key in text:
            return text.replace(self._api_key, "[REDACTED]")
        return text

    def generate(self, request: GenerationRequest) -> GenerationResult:
        config_kwargs: dict[str, object] = {
            "system_instruction": request.system_instruction,
            "max_output_tokens": request.max_output_tokens,
        }
        if request.temperature is not None:
            config_kwargs["temperature"] = request.temperature
        if request.top_p is not None:
            config_kwargs["top_p"] = request.top_p
        if request.top_k is not None:
            config_kwargs["top_k"] = request.top_k
        thinking: dict[str, object] = {}
        if request.thinking_level is not None:
            thinking["thinking_level"] = request.thinking_level
        if request.thinking_budget is not None:
            thinking["thinking_budget"] = request.thinking_budget
        if thinking:
            config_kwargs["thinking_config"] = types.ThinkingConfig(**thinking)

        parameters = {
            "model": request.model_id,
            "contents": request.user_text,
            "config": {
                key: value
                for key, value in config_kwargs.items()
                if key != "thinking_config"
            },
        }
        if thinking:
            parameters["config"]["thinking_config"] = thinking

        response = self._client.models.generate_content(
            model=request.model_id,
            contents=request.user_text,
            config=types.GenerateContentConfig(**config_kwargs),
        )
        candidate = response.candidates[0] if response.candidates else None
        finish_reason = None
        if candidate is not None and candidate.finish_reason is not None:
            finish_reason = str(getattr(candidate.finish_reason, "value", candidate.finish_reason))
        usage = {}
        if response.usage_metadata is not None:
            dumped = response.usage_metadata.model_dump(exclude_none=True)
            usage = {key: value for key, value in dumped.items() if isinstance(value, int)}
        return GenerationResult(
            response_text=response.text,
            model_version=response.model_version,
            finish_reason=finish_reason,
            token_usage=usage,
            request_parameters=parameters,
            error=None,
        )
