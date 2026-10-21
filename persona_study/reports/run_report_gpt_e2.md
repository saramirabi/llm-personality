# GPT-4o mini ACI-Bench run

- model_id: `gpt-4o-mini-2024-07-18`
- contexts: `data/aci_bench/aci_contexts.csv`
- output: `outputs/aci_gpt.jsonl`
- cleaned: `outputs/aci_gpt_cleaned.csv`
- OSCE measurement was not run on these rows

- records written: 3672
- successes: 3672
- failures: 0
- empty analyses: 0
- truncated: 0
- Patient: turns: 0
- finish_reason: stop on all 3672
- input tokens: 2887518
- cached input tokens: 73600
- output tokens: 273225
- reasoning tokens: 0
- doctor API cost: about $0.591543 at $0.15 / $0.075 cached / $0.60 per million

Median words: P0 46, P1 45, P2 66.5, P3 81, P4 62, P5 73.
