"""Claude Messages API provider.

Checked against the Claude API docs on 2 October 2026.
The system prompt is sent as the top-level `system` parameter. The Messages
API has no system role inside `messages`.
Claude Haiku 4.5 defaults to thinking off. Sending thinking.type "disabled"
or "adaptive" returns a 400 error, so the lowest setting is to omit `thinking`.
temperature, top_p, and top_k are omitted so the API defaults apply.
The API key is read from the environment and is never stored on the result.
"""

from __future__ import annotations

import os

import anthropic

from providers.base import GenerationRequest, GenerationResult


class ClaudeProvider:
    name = "claude"

    def __init__(self, api_key_env: str = "ANTHROPIC_API_KEY") -> None:
        api_key = os.environ.get(api_key_env)
        if not api_key:
            raise RuntimeError(
                f"Set {api_key_env} in the environment. Do not put the key in a file."
            )
        self._api_key = api_key
        self._client = anthropic.Anthropic(api_key=api_key)

    def redact(self, text: str) -> str:
        if self._api_key and self._api_key in text:
            return text.replace(self._api_key, "[REDACTED]")
        return text

    def generate(self, request: GenerationRequest) -> GenerationResult:
        if request.thinking_level is not None or request.thinking_budget is not None:
            raise RuntimeError(
                "Claude Haiku 4.5 lowest reasoning is thinking omitted. Do not send a thinking field."
            )
        if request.temperature is not None or request.top_p is not None or request.top_k is not None:
            raise RuntimeError("Sampling parameters are omitted so the model default is used.")
        parameters = {
            "model": request.model_id,
            "max_tokens": request.max_output_tokens,
            "system_delivery": "messages_api_top_level_system",
            "transport": "messages.stream",
            "system": request.system_instruction,
            "messages": [{"role": "user", "content": request.user_text}],
            "thinking": "omitted",
            "temperature": "omitted",
            "top_p": "omitted",
            "top_k": "omitted",
        }
        with self._client.messages.stream(
            model=request.model_id,
            max_tokens=request.max_output_tokens,
            system=request.system_instruction,
            messages=[{"role": "user", "content": request.user_text}],
        ) as stream:
            message = stream.get_final_message()
        texts = [block.text for block in message.content if getattr(block, "type", None) == "text"]
        usage = message.usage
        token_usage: dict[str, int | None] = {
            "input_tokens": int(usage.input_tokens),
            "output_tokens": int(usage.output_tokens),
            "reasoning_tokens": 0,
        }
        for field_name in (
            "cache_creation_input_tokens",
            "cache_read_input_tokens",
        ):
            value = getattr(usage, field_name, None)
            if isinstance(value, int):
                token_usage[field_name] = value
        return GenerationResult(
            response_text="".join(texts) if texts else None,
            model_version=str(message.model),
            finish_reason=None if message.stop_reason is None else str(message.stop_reason),
            token_usage=token_usage,
            request_parameters=parameters,
            error=None,
        )

    def count_prompt_tokens(self, model_id: str, system_text: str, user_text: str) -> int:
        """Official counter: POST /v1/messages/count_tokens. Thinking stays omitted."""
        counted = self._client.messages.count_tokens(
            model=model_id,
            system=system_text,
            messages=[{"role": "user", "content": user_text}],
        )
        return int(counted.input_tokens)
