# Gemini pilot report

Pilot only. The main sample (804 contexts × 6 conditions) was not run.

## Run

- Model id: `gemini-2.5-flash-lite`
- Reasoning setting, identical on every request: `thinking_budget=0`
- Model version returned: `gemini-2.5-flash-lite` on all 360 records
- Requests sent: 360 (60 pilot contexts × P0–P5)
- Succeeded: 360
- Failed: 0
- Retried: 0 (every record has `attempt_count` 1)
- Finish reason: `STOP` on all 360
- Output file: `persona_study/outputs/pilot_gemini.jsonl`
- Cleaned table: `persona_study/outputs/pilot_gemini_cleaned.csv` (360 rows; the JSONL was not rewritten)

Every JSONL record stores `reasoning_setting` = `thinking_budget=0` and `reasoning_token_count` = 0.

## Post-processing flags by condition

Each condition has 60 responses. `flag_empty`, `flag_truncated`, and `flag_refusal_or_ai_meta` are 0 in every condition.

| Condition | Patient turn | Multiple doctor turns | Empty | Truncated | Refusal or AI meta |
| --- | ---: | ---: | ---: | ---: | ---: |
| P0 | 1 | 1 | 0 | 0 | 0 |
| P1 | 0 | 0 | 0 | 0 | 0 |
| P2 | 2 | 1 | 0 | 0 | 0 |
| P3 | 1 | 1 | 0 | 0 | 0 |
| P4 | 1 | 1 | 0 | 0 | 0 |
| P5 | 0 | 0 | 0 | 0 | 0 |

The multi-turn flags are one Late context, `P2_001247`, under P0, P2, P3, and P4: the model continued the consultation with invented `Patient:` and further `Doctor:` turns (241–454 words). `P2_002321` P2 also contains a single trailing `Patient: No.` (10 words) and is flagged only for a patient turn.

## Cleaned-text word count

Word count is whitespace tokens after removing one leading `Doctor:` label. Median is the average of the two central values when the count is even.

### By condition (n = 60)

| Condition | Min | Median | Max |
| --- | ---: | ---: | ---: |
| P0 | 4 | 15.5 | 292 |
| P1 | 4 | 12.0 | 133 |
| P2 | 4 | 14.0 | 241 |
| P3 | 5 | 45.0 | 454 |
| P4 | 6 | 56.5 | 253 |
| P5 | 5 | 22.0 | 104 |

### By position (n = 120, all conditions pooled)

| Position | Min | Median | Max |
| --- | ---: | ---: | ---: |
| Early | 4 | 15.0 | 94 |
| Middle | 5 | 23.5 | 201 |
| Late | 7 | 32.5 | 454 |

### By position and condition (n = 20)

| Position | Condition | Min | Median | Max |
| --- | --- | ---: | ---: | ---: |
| Early | P0 | 4 | 13.0 | 87 |
| Early | P1 | 4 | 11.0 | 33 |
| Early | P2 | 4 | 12.5 | 36 |
| Early | P3 | 5 | 28.5 | 94 |
| Early | P4 | 6 | 35.5 | 82 |
| Early | P5 | 5 | 17.0 | 58 |
| Middle | P0 | 5 | 16.0 | 85 |
| Middle | P1 | 8 | 12.0 | 24 |
| Middle | P2 | 5 | 17.5 | 119 |
| Middle | P3 | 9 | 46.5 | 201 |
| Middle | P4 | 15 | 58.0 | 106 |
| Middle | P5 | 7 | 23.0 | 79 |
| Late | P0 | 8 | 25.5 | 292 |
| Late | P1 | 8 | 17.0 | 133 |
| Late | P2 | 7 | 16.5 | 241 |
| Late | P3 | 8 | 62.5 | 454 |
| Late | P4 | 34 | 64.0 | 253 |
| Late | P5 | 13 | 29.0 | 104 |

P1 and P2 stay short. P3 and P4 are longer, and the longest tails are the multi-turn Late responses above.

## Tokens

Billed usage from `usage_metadata`. The API omitted `thoughts_token_count` on every response. On every response, `prompt_token_count + candidates_token_count = total_token_count`, so the recorded reasoning token count is 0.

| | Prompt | Output | Reasoning | Total |
| --- | ---: | ---: | ---: | ---: |
| Pilot (360) | 368,784 | 17,283 | 0 | 386,067 |
| Projected main (4,824) | 4,941,705.6 | 231,592.2 | 0 | 5,173,297.8 |

The main projection multiplies the pilot totals by 4,824 / 360 = 13.4. It assumes the main contexts have the same average length as the pilot. The earlier dry-run estimate was 357,077 input tokens (characters / 4). Billed prompt tokens were 368,784.

At the standard list price for this model ($0.10 per million input tokens and $0.40 per million output tokens), the pilot is about $0.044. The same rates on the projected main totals are about $0.59. Batch and Flex prices are lower for this same model and were not used.

## Six conditions on three contexts

One context per position, drawn with `numpy.random.default_rng(20261002)` from the sorted pilot context ids in that position. Texts are the cleaned next turns.

### Early: P2_009999 (RES0215)

**P0** (10 words)

```
OK. And any known allergies, either environmental or any medications?
```

**P1** (16 words)

```
Has she had any medical history of asthma or any other breathing problems in the past?
```

**P2** (17 words)

```
OK. Has she had any allergies that you know of? Hay fever, eczema, or any food allergies?
```

**P3** (45 words)

```
OK, thank you for all that information. It's good you've brought her in. It sounds like you've been keeping a close eye on her. Can you tell me a little bit about her past medical history? Any significant illnesses or allergies that you know of?
```

**P4** (57 words)

```
I understand. It sounds like you've been keeping a close eye on your daughter and you're right to bring her in when you're concerned. Can you tell me a little bit about how this has been affecting her day-to-day life? Is she still able to play with her friends, or has this been making her slow down?
```

**P5** (18 words)

```
Right, I'm going to examine your daughter now. Please can you bring her over to the examination couch.
```

### Middle: P2_001676 (MSK0032)

**P0** (16 words)

```
Okay. Um, and she has no other significant family history of any other medical conditions, correct?
```

**P1** (13 words)

```
Okay. And does she have any family history of arthritis or inflammatory conditions?
```

**P2** (24 words)

```
Okay. Now, can you show me which arm is hurting? And can you point to exactly where on the elbow the pain is located?
```

**P3** (83 words)

```
Okay, thank you for all that information. It sounds like this started quite suddenly after your walk yesterday, and it's concerning that she's in so much pain, a 7 out of 10, and it's been constant. It's good that she didn't actually hit herself when she was falling, and that she hasn't had any pain like this before. You mentioned that the pain goes up into her upper arm – can you show me exactly where she's pointing when she says it hurts?
```

**P4** (43 words)

```
Okay, thank you for all that information. It sounds like it's been a pretty uncomfortable day for her, and I can see you're worried about her. I'd like to examine her elbow now and see if we can figure out what's going on.
```

**P5** (16 words)

```
Alright, I'm going to examine your daughter now. Please have her sit on the examination table.
```

### Late: P2_001679 (MSK0032)

**P0** (24 words)

```
Okay, thank you for all that information. I'm going to go ahead and do a physical exam on your daughter's elbow and arm now.
```

**P1** (19 words)

```
Okay, I'm just going to examine her elbow now. Can you have her roll up her sleeve for me?
```

**P2** (42 words)

```
Okay, I have a good understanding of her medical history. Now, I'd like to ask a few questions about the pain itself. Can you tell me if she's had any difficulty moving her elbow, like bending or straightening it since this started?
```

**P3** (44 words)

```
Okay, thank you for all that information. I know it's a lot of questions, but it helps me get a really clear picture. And how are you doing with all of this? It must be worrying to see your daughter in so much pain.
```

**P4** (58 words)

```
Thank you for sharing all that information. It sounds like this has been quite a worrying experience for both you and your daughter. I'd like to examine her arm now, if that's alright with you. We'll just gently have a look and feel around her elbow to see if we can understand what might be causing her pain.
```

**P5** (35 words)

```
Alright, I'm going to examine your daughter now. Please have her take off her shirt so I can get a good look at her arm. I need to see her elbow and upper arm clearly.
```

## Problems and assumptions

- Cheapest text model on the Gemini Developer API standard price list checked on 2 October 2026 is `gemini-2.5-flash-lite` ($0.10 / $0.40 per million tokens). `gemini-2.5-flash` is $0.30 / $2.50, `gemini-3.1-flash-lite` is $0.25 / $1.50, and `gemini-3.5-flash-lite` is $0.30 / $2.50. Image, live, and speech models were not considered.
- Lowest reasoning setting for this model is `thinking_budget=0`, which the thinking guide lists as the way to disable thinking. The on-range starts at 512. Gemini 3 `thinking_level` was not sent. The model card reports that the model supports thinking; the budget of 0 is what turns it off for the request.
- `reasoning_token_count` is 0 because the API did not return `thoughts_token_count` and the token totals contain no remainder. That 0 is recorded on every output record; it is not a separate billed field.
- Before the 360 study calls, the client confirmed the model (`output_token_limit` 65536, so `max_output_tokens` 65536 matches the limit) and sent one 9-token probe (`Reply with the single word ready.`) to check that `thinking_budget=0` is accepted. Those two calls are not in the JSONL and are not part of the 360.
- Requests used `generate_content`, not the Interactions API. Sampling parameters were left unset.
- The character/4 figure is an estimate. The token table above is the billed count.
- The main-run projection scales pilot averages. Main contexts are longer on average than a random pilot draw might be, so the projection can miss the true main total in either direction. It is not a `countTokens` call on the main set.
- Five responses continued past one doctor turn. They are kept in the JSONL and flagged in the cleaned table.
- The human reference file was not read.
