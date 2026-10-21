# Claude main-sample run report

Main sample only. The Gemini outputs were not changed.

## Model and reasoning

- Model id: `claude-haiku-4-5-20251001` (Claude Haiku 4.5). The Models API returned this id, display name Claude Haiku 4.5, and `max_tokens` 64000.
- This is the cheapest model still offered on the Claude API price list checked on 2 October 2026: $1 per million input tokens and $5 per million output tokens. Claude Haiku 3.5 is listed at $0.80 / $4 but is retired on the Claude API.
- Model version returned: `claude-haiku-4-5-20251001` on all 4,824 successful calls.
- System prompt delivery: the Messages API top-level `system` parameter. The Messages API has no system role inside `messages`. The user text is one `user` message.
- Transport: `messages.stream`. A non-streaming `messages.create` with `max_tokens` 64000 is rejected by the Python SDK before the request is sent, because the SDK treats that limit as a request that may exceed 10 minutes. Streaming is the documented way to send the same parameters. The 24 rejected calls were not sent to the API.
- Reasoning setting, identical on every request: `thinking_omitted_default_off`. The thinking guide lists Claude Haiku 4.5 as thinking off when the `thinking` field is omitted. `thinking.type` `disabled` and `adaptive` both return a 400 error. Extended thinking is optional and was not enabled. Enabling it requires `budget_tokens` of at least 1,024, which is a higher setting.
- Sampling: `temperature`, `top_p`, and `top_k` were omitted. The Messages API default temperature is 1.0. Haiku 4.5 still accepts a non-default temperature, but the study uses the default, so the parameter was not sent.
- `max_tokens` was 64000, the model's documented maximum output.
- SDK: `anthropic` 0.125.0.
- Every record stores `reasoning_setting` = `thinking_omitted_default_off`. Successful records store `token_usage.reasoning_tokens` = 0. The separate `reasoning_token_count` field is null: the shared writer fills that field from Gemini's `thoughts_token_count`, or sets it to 0 only when `thinking_budget` is 0. No thinking blocks were returned.

## Requests

- Output file: `persona_study/outputs/main_claude.jsonl` (not the Gemini file and not the pilot file)
- Contexts: `p2_contexts_FROZEN.csv` only. The pilot context file and the human reference file were not read. The frozen SHA-256 matched the manifest.
- Prompt SHA-256: `5d91f7d1e52d4b6b3ec38d6b05ab9eef8d184113eb9597f52cd52de88bae7999`. This matches the Gemini pilot and the Gemini main run. The prompt file was not edited.
- Every assembled user message ends with `Doctor:`. The template keeps a trailing newline, so the string ends with `Doctor:\n`.
- API calls that reached the model: 4,824. All finished `end_turn`.
- Client-side rejections before any request was sent: 24. Each is a `ValueError` from the non-streaming call, `attempt_count` 1, empty response, no token usage. Those lines are still in the JSONL.
- Each of those 24 keys was sent once more with streaming (`attempt_count` 2) and finished `end_turn`. The other 4,800 successful responses were not sent again.
- Final successful canonical records: 4,824
- Final failed canonical records: 0
- Each of the 4,824 keys `(context_id, condition)` has exactly one canonical record with a non-empty response. Counts are 804 in each of P0–P5 and 1,608 in each of Early, Middle, and Late.
- Early-stop check after the first 30 completed streaming requests: 0 empty, truncated, errors, or `Patient:` turns.

## Post-processing

Raw `response_text` is stored unchanged. For the canonical table, `analysis_text` is the text before the first `Patient:` label. If there is no `Patient:` label, `analysis_text` is the whole response. The cleaned table is `persona_study/outputs/main_claude_cleaned.csv` (4,824 canonical rows). No `analysis_text` is empty. Word counts below are whitespace tokens in `analysis_text`.

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
| P0 | 5 | 25 | 169 |
| P1 | 4 | 18 | 170 |
| P2 | 4 | 27 | 193 |
| P3 | 4 | 48.5 | 223 |
| P4 | 6 | 59 | 166 |
| P5 | 4 | 32 | 194 |

### Analysis-text word count by position (n = 1,608)

| Position | Min | Median | Max |
| --- | ---: | ---: | ---: |
| Early | 5 | 29 | 147 |
| Middle | 4 | 30 | 205 |
| Late | 6 | 36 | 223 |

Median is the average of the two central values. For P3 those two values differed, so the median is 48.5. The other medians are whole numbers.

## Tokens and cost

Token totals are the sums of the usage fields on the 4,824 calls that reached the API. The 24 client-side rejections have no usage and are not included. They are not estimates.

List price used: Claude Haiku 4.5, $1 per million input tokens and $5 per million output tokens. Cache creation and cache read tokens are 0. Reasoning tokens in the usage object are 0.

| | Tokens |
| --- | ---: |
| Input | 5,358,168 |
| Output | 277,149 |
| Cache write | 0 |
| Cache read | 0 |
| Reasoning | 0 |

Input cost $5.358168. Output cost $1.385745. Total cost $6.743913.
