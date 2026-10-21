"""Provider interface for one-shot text generation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass(frozen=True)
class GenerationRequest:
    model_id: str
    system_instruction: str
    user_text: str
    max_output_tokens: int
    temperature: float | None = None
    top_p: float | None = None
    top_k: int | None = None
    thinking_level: str | None = None
    thinking_budget: int | None = None
    reasoning_effort: str | None = None


@dataclass
class GenerationResult:
    response_text: str | None
    model_version: str | None
    finish_reason: str | None
    token_usage: dict[str, int | None]
    request_parameters: dict[str, object]
    error: str | None = None
    extra: dict[str, object] = field(default_factory=dict)


class TextProvider(Protocol):
    name: str

    def generate(self, request: GenerationRequest) -> GenerationResult:
        """Send one request. Raise on transport or API errors that should be retried or recorded."""
