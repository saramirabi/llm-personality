# Meta Llama 3 8B Instruct E1 run

- model_id: `bartowski/meta-llama-3-8b-instruct`
- source: bartowski/Meta-Llama-3-8B-Instruct-GGUF, Q4_K_S, base model meta-llama/Meta-Llama-3-8B-Instruct
- server: `http://localhost:1234/v1`
- endpoint: `POST /v1/chat/completions`
- chat template: Meta Llama 3 Instruct chat template. The system role is a real system header.
- context_length: 8192 (generation_config max_length)
- max_new_tokens: the tokens remaining inside that context. generation_config.json states max_length 8192 and no max_new_tokens.
- stop: `<|eot_id|>` and `<|end_of_text|>`
- reasoning: no reasoning control on the model card; no thinking prompt added
- tokenizer: `unsloth/llama-3-8b-Instruct`
- sampling: temperature, top_p, and top_k omitted
- output: `outputs/main_llama3instruct.jsonl`

- requests recorded: 4824
- successes: 4824
- failures: 0
- empty analyses: 0
- input tokens: 5031144
- output tokens: 261702
- doctor API cost: 0
