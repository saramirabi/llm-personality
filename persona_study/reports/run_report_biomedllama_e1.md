# bio-medical Llama 3 E1 run

- model_id: `bio-medical-multimodal-llama-3-8b-v1-i1`
- source: mradermacher/Bio-Medical-MultiModal-Llama-3-8B-V1-i1-GGUF, Q4_K_S, base model ContactDoctor/Bio-Medical-MultiModal-Llama-3-8B-V1
- server: `http://localhost:1234/v1`
- endpoint: `POST /v1/chat/completions`
- chat template: Llama 3 chat template. The system role is a real system header.
- context_length: 8192 (max_position_embeddings)
- max_new_tokens: the tokens remaining inside that context. generation_config.json states no separate max_new_tokens.
- stop: `<|eot_id|>` and `<|end_of_text|>`
- reasoning: no reasoning control on the model card; no thinking prompt added
- tokenizer: `unsloth/llama-3-8b-Instruct`
- sampling: temperature, top_p, and top_k omitted
- output: `outputs/main_biomedllama.jsonl`

- requests recorded: 4824
- successes: 4824
- failures: 0
- empty analyses: 0
- input tokens: 5031144
- output tokens: 545853
- doctor API cost: 0
