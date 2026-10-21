# Personas Are Not Dials

Code and data for *Personas Are Not Dials: Uneven Behavioral Effects of Assigned Communication Styles in LLM Clinicians*.

Five clinician communication styles (P1 narrowly biomedical, P2 expanded biomedical, P3 biopsychosocial, P4 psychosocial, P5 directive) and a baseline without a persona (P0) are assigned through the system prompt to six LLMs. Every model and condition continues the same, position-matched consultation history, so each persona output can be compared with the same model's baseline output for the same context.

| Experiment | What is generated | Corpus | Outputs per model |
|---|---|---|---|
| 1 | Next clinician turn | OSCE (804 contexts, 268 dialogues) | 4,824 |
| 2 | Four clinician turns with a simulated patient (Gemini 2.5 Flash) | OSCE (150 contexts) | 3,600 clinician turns |
| 3 | Next clinician turn | ACI-Bench (612 contexts, 204 visits) | 3,672 |

Models: Gemini 2.5 Flash-Lite, Claude Haiku 4.5, GPT-4o mini (`gpt-4o-mini-2024-07-18`), Llama-3-8B-Instruct (Q4_K_S), Bio-Medical Llama-3 8B (Q4_K_S), MedGemma 4B (Q4_K_S). GPT-5 nano is included as an ablation.

## Layout

```
persona_study/
  src/                     context construction, generation, post-processing, measurement
    providers/             one client per model (API models; local models via an OpenAI-compatible server)
  prompts/                 base instruction, persona texts, simulated-patient prompt
  config*.yaml             paths and run settings
  data/
    frozen/                OSCE context set (p2_contexts_FROZEN.csv) and its manifest with SHA-256 hashes
    aci_bench/             ACI-Bench context set and manifest
    prior_study/           targets of the earlier study, used only to keep the two context sets disjoint
  outputs/                 generated texts, cleaned and analysis-ready
    main_<model>_cleaned.csv      Experiment 1
    rollouts/<model>_cleaned.csv  Experiment 2
    aci_<model>_cleaned.csv       Experiment 3
    ablation_gpt5nano/            GPT-5 nano outputs, features and results
  reports/                 run reports (requests, failures, token counts) and measurement reports
  analysis/
    analysis_plan_v1.yaml  versioned analysis plan: markers, predictions, classifier settings, seed
    features_<model>.csv   per-output markers (Experiment 1)
    results/<model>/       accuracy, recall, confusion, predictions and verdicts, realization, GEE
    external_validation/   Empath and ConvoKit measures (measurement-instrument ablation)
    length_matched/        output-length ablation (first 25 words, first sentence)
    family_comparison/     Llama-3-8B-Instruct versus its bio-medical fine-tune
    testability/           testability sensitivity analysis and degree of realization (R, R*)
    reviewer_robustness/   matched-length position analysis, effect-size and family tables
paper_analysis/
  analysis_exp2_exp3.py    Experiments 2 and 3 with the unchanged measurement code
  heldout_six_q4.py        held-out-model classifier (train on five models, test on the sixth)
  make_*.py                figures
  exp23_results*/          Experiment 2 and 3 results per model group
  figures/                 figures of the paper
```

In `persona_study/analysis/external_validation/`, the top-level files hold Gemini, Claude, MedGemma and, in the `gpt` columns, the GPT-5 nano ablation; GPT-4o mini, the bio-medical Llama and Llama-3-8B-Instruct are in the subfolders `gpt4omini/`, `biomedllama/` and `llama3instruct_q4/`.

`paper_analysis/exp23_results/` holds Gemini and Claude; its `gpt` rows are the GPT-5 nano ablation. GPT-4o mini is in `exp23_results_gpt4o/`, Llama-3-8B-Instruct in `exp23_results_llama3q4/`, the bio-medical Llama in `exp23_results_biomed/`, and MedGemma and the held-out-model results in `exp23_results_med/`.

## Where each result comes from

| Paper | Files |
|---|---|
| Table 2, Section 4.2 (verdicts) | `persona_study/analysis/results/<model>/c_predictions.csv`, `c_realised.csv` |
| Section 4.1, Table A3 (discriminability and classifier-input ablation) | `results/<model>/b_accuracy.csv`, `b_recall.csv`; held-out row: `paper_analysis/exp23_results_med/heldout6q4_*.csv` |
| Section 4.3, Figure 3, Table A8 (family comparison) | `persona_study/analysis/family_comparison/`, `reviewer_robustness/family_baseline.tex` |
| Section 4.4, Figure 4a (position) | `results/<model>/b_accuracy.csv`, `b1_gee.csv`; matched length: `reviewer_robustness/position_length_overlap.csv` |
| Section 4.5, Figure 4b (rollouts) | `paper_analysis/exp23_results*/roll_*.csv` |
| Section 4.6, Table 3 (ACI-Bench) | `paper_analysis/exp23_results*/aci_*.csv` |
| Sensitivity analysis, degree of realization | `persona_study/analysis/testability/` |
| Effect sizes (Table A7) | `results/<model>/c_predictions.csv`, `reviewer_robustness/effect_sizes.tex` |
| Measurement-instrument ablation | `persona_study/analysis/external_validation/` |
| Output-length ablation | `persona_study/analysis/length_matched/` |
| Model-version ablation (GPT-5 nano) | `persona_study/outputs/ablation_gpt5nano/` |

## Reproducing the analyses

Run every command from the repository root.

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz

# Experiment 1 measurement for one model (writes features and results/<model>/)
python persona_study/src/run_measurement.py --help

# Experiments 2 and 3 for one model
python paper_analysis/analysis_exp2_exp3.py paper_analysis/exp23_results_llama3q4 llama3instruct llama3instruct

# Held-out model, family comparison, sensitivity analyses
python paper_analysis/heldout_six_q4.py
python persona_study/analysis/family_comparison/family_comparison.py
python persona_study/analysis/testability/persona_testability.py
python persona_study/analysis/testability/graded_realization.py
python persona_study/analysis/reviewer_robustness/position_length_overlap.py
```

All analyses read the cleaned outputs in this repository; no model is called. Bootstrap intervals use 2,000 cluster resamples over dialogues with seed 20261002. The analyses in the paper were run with Python 3.10, scikit-learn 1.5.1, spaCy 3.7.5, scispaCy 0.5.5 (`en_core_sci_sm` 0.5.4) and statsmodels 0.15.0.

Generating new outputs requires API keys (`GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`) and, for the open-weight models, an OpenAI-compatible server (LM Studio 0.4.21 was used) at `http://localhost:1234/v1` serving the GGUF weights listed in the paper. Rebuilding the context sets requires the original corpora (below); the frozen context sets in `persona_study/data/` are the ones used, and their SHA-256 hashes are in the manifests and in the paper.

## Data sources and what is not included

- **OSCE corpus**: simulated patient-physician interviews by Fareez et al. (2022), *Scientific Data* 9:132. The original transcripts and audio are not redistributed here; the context files contain only the dialogue prefixes used as model input.
- **ACI-Bench**: Yim et al. (2023), *Scientific Data* 10:586. Raw challenge files are not redistributed; download them from the ACI-Bench repository.
- Not included: raw request/response logs (the cleaned outputs contain every generated text), runs of models that are not reported in the paper, and the human-annotation files.

## Licence

Code: MIT (see `LICENSE`). Generated outputs and derived data: CC BY 4.0. The context sets are derived from the two corpora above, which remain under their own licences; please cite them when using the data.

## Citation

Anonymous (2026). Personas Are Not Dials: Uneven Behavioral Effects of Assigned Communication Styles in LLM Clinicians. Under review.
