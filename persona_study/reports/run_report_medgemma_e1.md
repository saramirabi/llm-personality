# MedGemma 4B IT E1 run

- model_id: `medgemma-4b-it`
- source: unsloth/medgemma-4b-it-GGUF, Q4_K_S, base model google/medgemma-4b-it
- server: `http://localhost:1234/v1`
- endpoint: `POST /v1/chat/completions`
- chat template: Gemma 3 conversational template from the MedGemma tokenizer. The system role is prefixed onto the first user turn.
- context_length: 131072 (text_config max_position_embeddings)
- max_new_tokens: the tokens remaining inside that context. generation_config.json states no separate max_new_tokens.
- stop: `<end_of_turn>` and `<eos>`
- reasoning: no reasoning control on the model card; no thinking prompt added
- tokenizer: `unsloth/medgemma-4b-it`
- sampling: temperature, top_p, and top_k omitted
- output: `outputs/main_medgemma.jsonl`

- requests recorded: 4824
- successes: 4824
- failures: 0
- empty analyses: 0
- input tokens: 5898480
- output tokens: 339339
- doctor API cost: 0
