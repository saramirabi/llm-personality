# GPT-4o mini E1 run

- model_id: `gpt-4o-mini-2024-07-18`
- endpoint: OpenAI Chat Completions, system role
- max_completion_tokens: 16384
- reasoning: omitted; this model has no reasoning step
- sampling: temperature, top_p, and top_k omitted
- output: `outputs/main_gpt.jsonl`
- cleaned: `outputs/main_gpt_cleaned.csv`
- previous GPT-5 nano outputs: `outputs/gpt5nano_backup/`

- records written: 4848
- successes: 4824
- failed attempts later retried successfully: 24
- remaining failures: 0
- empty analyses: 0
- truncated: 0
- Patient: turns: 0
- finish_reason: stop on all 4824
- input tokens: 4855170
- cached input tokens: 314880
- output tokens: 395694
- reasoning tokens: 0
- doctor API cost: about $0.942076 at $0.15 / $0.075 cached / $0.60 per million

Median analysis words: P0 66, P1 30, P2 76.5, P3 97, P4 75, P5 73.
