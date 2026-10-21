# Gemini main-sample run report

Main sample only. No other model was run.

## Model and reasoning

- Model id: `gemini-2.5-flash-lite`
- Model version returned: `gemini-2.5-flash-lite` on all 4,825 API calls
- Reasoning setting, identical on every request including the retry: `thinking_budget=0`
- The Gemini thinking guide lists `thinkingBudget = 0` as the way to disable thinking on Gemini 2.5 Flash-Lite. That is the lowest setting this model allows. The retry used the same setting. Gemini 3 `thinking_level` was not sent.
- Every record stores `reasoning_setting` = `thinking_budget=0` and `reasoning_token_count` = 0.
- The API omitted `thoughts_token_count` on every call. On every call, prompt tokens plus output tokens equal `total_token_count`. The blocked first attempt omitted `candidates_token_count`; its prompt count equals its total, so its output count is 0. The recorded reasoning count is 0.

## Requests

- Output file: `persona_study/outputs/main_gemini.jsonl` (not the pilot file)
- Contexts: `p2_contexts_FROZEN.csv` only. The pilot context file and the human reference file were not read.
- Prompt SHA-256: `5d91f7d1e52d4b6b3ec38d6b05ab9eef8d184113eb9597f52cd52de88bae7999`. This is the pilot hash and the original main-run hash. The prompt file was not edited.
- The retried user message was built with the same prompt code. Its last line is exactly `Doctor:`. The unchanged template keeps a trailing newline, so the string ends with `Doctor:\n`.
- API calls, including the retry: 4,825
- Initial failed attempt: 1 (`P2_006268` P5, `PROHIBITED_CONTENT`, empty response, `attempt_count` 1). That line is still in the JSONL.
- Retry attempts: 1. The same request was sent once more (`attempt_count` 2) and finished `STOP`.
- Final successful canonical records: 4,824
- Final failed canonical records: 0
- Each of the 4,824 keys `(context_id, condition)` has exactly one canonical record, and that record finished `STOP` with a non-empty response. Counts are 804 in each of P0–P5.
- `P2_006268` / P5 initially returned `PROHIBITED_CONTENT` and was retried. The retry succeeded. The other 4,823 successful responses were not sent again and their stored response text is unchanged.

## Post-processing

Raw `response_text` is stored unchanged. For the canonical table, `analysis_text` is the text before the first `Patient:` label, which is the first doctor turn. If there is no `Patient:` label, `analysis_text` is the whole response. Existing flags use the same code as the rest of the main run. The cleaned table is `persona_study/outputs/main_gemini_cleaned.csv` (4,824 canonical rows). Word counts below are whitespace tokens in `analysis_text`.

### Flags by condition (n = 804)

| Condition | Empty | Truncated | Patient turn | Multiple doctor turns | Refusal or AI meta |
| --- | ---: | ---: | ---: | ---: | ---: |
| P0 | 0 | 0 | 10 | 6 | 0 |
| P1 | 0 | 0 | 1 | 0 | 0 |
| P2 | 0 | 0 | 11 | 10 | 0 |
| P3 | 0 | 0 | 2 | 2 | 0 |
| P4 | 0 | 0 | 0 | 0 | 0 |
| P5 | 0 | 0 | 2 | 2 | 0 |

### Flags by position (n = 1,608)

| Position | Empty | Truncated | Patient turn | Multiple doctor turns | Refusal or AI meta |
| --- | ---: | ---: | ---: | ---: | ---: |
| Early | 0 | 0 | 0 | 0 | 0 |
| Middle | 0 | 0 | 8 | 7 | 0 |
| Late | 0 | 0 | 18 | 13 | 0 |

### Analysis-text word count by condition (n = 804)

| Condition | Min | Median | Max |
| --- | ---: | ---: | ---: |
| P0 | 3 | 16 | 235 |
| P1 | 4 | 13 | 223 |
| P2 | 4 | 16 | 273 |
| P3 | 3 | 43 | 230 |
| P4 | 4 | 52 | 189 |
| P5 | 3 | 21 | 178 |

### Analysis-text word count by position (n = 1,608)

| Position | Min | Median | Max |
| --- | ---: | ---: | ---: |
| Early | 3 | 17 | 220 |
| Middle | 3 | 22 | 170 |
| Late | 3 | 29 | 273 |

Median is the average of the two central values. Here the two central values were equal, so each median is a whole number.

## Tokens and cost

Token totals are the sums of the usage fields stored on all 4,825 API calls, including the blocked first attempt and the retry. They are not estimates.

List price used: Gemini 2.5 Flash-Lite standard tier, $0.10 per million input tokens and $0.40 per million output tokens. The output price includes thinking tokens. Reasoning tokens are 0, so they add nothing to the output charge.

| | Tokens |
| --- | ---: |
| Input | 5,187,255 |
| Output | 223,597 |
| Reasoning | 0 |
| Total | 5,410,852 |

Total cost: **$0.6081643** (input $0.5187255 + output $0.0894388).
