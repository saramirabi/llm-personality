# GPT main-sample run report

Main sample only. The Gemini and Claude outputs were not changed.

## Model and reasoning

- Model id: `gpt-5-nano-2025-08-07`. The Models API returned this snapshot and the alias `gpt-5-nano`.
- This is the cheapest text model on the OpenAI standard price list checked on 2 October 2026: $0.05 per million input tokens, $0.005 per million cached input tokens, and $0.40 per million output tokens. GPT-4.1 nano is $0.10 / $0.40 and has no reasoning step. GPT-6 Luna is $0.10 / $0.50. GPT-5.6 Luna is $0.20 / $1.20.
- Model version returned: `gpt-5-nano-2025-08-07` on all 4,824 calls.
- System prompt delivery: Chat Completions `messages`, one message with role `system` and one with role `user`.
- Transport: non-streaming `chat.completions.create`.
- Reasoning setting, identical on every request: `reasoning_effort=minimal`. The GPT-5 model page lists `minimal`, `low`, `medium`, and `high`. A probe of this snapshot on 2 October 2026 sent `reasoning_effort` `none` and the API returned HTTP 400: supported values are `minimal`, `low`, `medium`, and `high`. `minimal` is the lowest accepted value.
- Sampling: `temperature` and `top_p` were omitted. `top_k` is not a Chat Completions parameter. `service_tier` was omitted. Every response returned `service_tier` `default`, which is standard pricing.
- `max_completion_tokens` was 128000, the documented maximum output for this model. That limit includes reasoning tokens. Reasoning tokens were 0, so it did not bind the visible answer.
- SDK: `openai` 3.23.0.
- Every record stores `reasoning_setting` = `reasoning_effort=minimal` and `reasoning_token_count` = 0. `token_usage.reasoning_tokens` is 0 on all 4,824 calls. Those reasoning tokens are included in `output_tokens` when present; here they add nothing.

## Requests

- Output file: `persona_study/outputs/main_gpt.jsonl` (not the Gemini file, not the Claude file, and not the pilot file)
- Contexts: `p2_contexts_FROZEN.csv` only. The pilot context file and the human reference file were not read. The frozen SHA-256 matched the manifest.
- Prompt SHA-256: `5d91f7d1e52d4b6b3ec38d6b05ab9eef8d184113eb9597f52cd52de88bae7999`. This matches the Gemini pilot, the Gemini main run, and the Claude main run. The prompt file was not edited.
- Every assembled user message ends with `Doctor:`. The template keeps a trailing newline, so the string ends with `Doctor:\n`.
- API calls that reached the model: 4,824. All finished `stop` on attempt 1. There are no error lines.
- Final successful canonical records: 4,824
- Final failed canonical records: 0
- Each of the 4,824 keys `(context_id, condition)` has exactly one record. Counts are 804 in each of P0–P5 and 1,608 in each of Early, Middle, and Late.
- Early-stop check after the first 30 completed requests: 0 empty, truncated, errors, or `Patient:` turns.

## Post-processing

Raw `response_text` is stored unchanged. For the canonical table, `analysis_text` is the text before the first `Patient:` label. If there is no `Patient:` label, `analysis_text` is the whole response. The cleaned table is `persona_study/outputs/main_gpt_cleaned.csv` (4,824 canonical rows). No `analysis_text` is empty. Word counts below are whitespace tokens in `analysis_text`.

### Flags by condition (n = 804)

| Condition | Empty | Truncated | Patient turn | Multiple doctor turns | Refusal or AI meta |
| --- | ---: | ---: | ---: | ---: | ---: |
| P0 | 0 | 0 | 0 | 0 | 0 |
| P1 | 0 | 0 | 0 | 0 | 0 |
| P2 | 0 | 0 | 0 | 0 | 0 |
| P3 | 0 | 0 | 0 | 0 | 0 |
| P4 | 0 | 0 | 0 | 0 | 0 |
| P5 | 0 | 0 | 0 | 0 | 0 |

### Flags by position (n = 1,608)

| Position | Empty | Truncated | Patient turn | Multiple doctor turns | Refusal or AI meta |
| --- | ---: | ---: | ---: | ---: | ---: |
| Early | 0 | 0 | 0 | 0 | 0 |
| Middle | 0 | 0 | 0 | 0 | 0 |
| Late | 0 | 0 | 0 | 0 | 0 |

### Analysis-text word count by condition (n = 804)

| Condition | Min | Median | Max |
| --- | ---: | ---: | ---: |
| P0 | 36 | 234 | 445 |
| P1 | 20 | 157.5 | 419 |
| P2 | 58 | 287 | 582 |
| P3 | 123 | 344 | 688 |
| P4 | 56 | 324 | 630 |
| P5 | 85 | 329 | 601 |

### Analysis-text word count by position (n = 1,608)

| Position | Min | Median | Max |
| --- | ---: | ---: | ---: |
| Early | 27 | 279 | 598 |
| Middle | 38 | 281.5 | 688 |
| Late | 20 | 291 | 635 |

Median is the average of the two central values. For P1 those two values differed, so the median is 157.5. For Middle they differed, so the median is 281.5. The other medians are whole numbers.

## Tokens and cost

Token totals are the sums of the usage fields on the 4,824 calls. They are not estimates. `service_tier` was `default` on every call, so the standard price applies. Cached input tokens are part of the input total and are billed at the cached rate. The remaining input tokens are billed at the uncached rate. Reasoning tokens are 0 and are already included in the output total.

List price used: GPT-5 nano, $0.05 per million uncached input tokens, $0.005 per million cached input tokens, and $0.40 per million output tokens.

| | Tokens |
| --- | ---: |
| Input | 4,738,926 |
| Cached input | 21,760 |
| Uncached input | 4,717,166 |
| Output | 1,784,390 |
| Cache write | 0 |
| Reasoning | 0 |

Uncached input cost $0.235858. Cached input cost $0.000109. Output cost $0.713756. Total cost $0.949723.
