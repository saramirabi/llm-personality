# Length-matched robustness analysis log

Run at 2026-10-18T03:56:14.217255+00:00

Post hoc robustness analysis, specified on 2026-10-05 after the Experiment 1 results were known.
No model API was called and no existing output or result file was modified.

## Input file SHA-256

- `outputs/main_gemini_cleaned.csv`: `63e2151914aa184acf7ef85e341e25282a50b118d38b35cd17c2e2fb2451a51b`
- `outputs/main_claude_cleaned.csv`: `70c0b1e6e056581cf21ba9db7c2291fa0dd15c2297e498e9fae9ba7c940ae2ac`
- `outputs/main_gpt_cleaned.csv`: `255644a9c5d884b4e0afd335754c2c048f227fb0dc5c335a2dc9fadaf9fa4af3`
- `data\frozen\p2_contexts_FROZEN.csv`: `443fff63f4222c3935366751454b0191a55579e1f663182e1b21a5a02c15e1c1`
- `analysis/analysis_plan_v1.yaml`: `c742158d7ae455ffa11d0551922fbdf5321b0c49504fcba19ac92c71d3c810f2`
- `src/run_measurement.py`: `07a80f179398d9b8a1e350d1789bc226720803215be759b1ad1741d377f28f37`
- `src/measure_text.py`: `a136f288ae6ee59291a8e319e49139ab3187bfdd896ce52026bae47dc91bf4d5`
- `analysis/length_matched/length_matched.py`: `955cff2be64e4c47eef4f72ce7be15e4826c74e9a0448385f452507509c1084e`

- gemini: 4824 rows, 804 contexts, conditions {'P0': 804, 'P1': 804, 'P2': 804, 'P3': 804, 'P4': 804, 'P5': 804}
- claude: 4824 rows, 804 contexts, conditions {'P0': 804, 'P1': 804, 'P2': 804, 'P3': 804, 'P4': 804, 'P5': 804}
- gpt: 4824 rows, 804 contexts, conditions {'P0': 804, 'P1': 804, 'P2': 804, 'P3': 804, 'P4': 804, 'P5': 804}
