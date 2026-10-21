# Personas Are Not Dials

Code, model outputs and results for the paper *Personas Are Not Dials: Uneven Behavioral Effects of Assigned Communication Styles in LLM Clinicians* (under double-blind review).

## The study in brief

Five clinician communication styles are assigned to six LLMs through the system prompt. The styles are four steps from narrowly biomedical to psychosocial (P1 to P4) and one directive style (P5). A baseline without a persona (P0) is the reference. Consultation transcripts are cut before a clinician turn early, midway and late in the visit, so every model and condition continues the identical dialogue history. Each persona output is therefore compared with the same model's baseline output for the same context.

| | Task | Corpus | Size |
|---|---|---|---|
| Experiment 1 | Next clinician turn | OSCE: 804 contexts from 268 dialogues | 28,944 outputs |
| Experiment 2 | Four clinician turns with a simulated patient (Gemini 2.5 Flash) | OSCE: 150 contexts | 3,600 clinician turns per model |
| Experiment 3 | Next clinician turn | ACI-Bench: 612 contexts from 204 visits | 22,032 outputs |

| Model | Short name in files |
|---|---|
| Gemini 2.5 Flash-Lite | `gemini` |
| Claude Haiku 4.5 | `claude` |
| GPT-4o mini (`gpt-4o-mini-2024-07-18`) | `gpt` |
| Llama-3-8B-Instruct, Q4_K_S | `llama3instruct` |
| Bio-Medical Llama-3 8B, Q4_K_S | `biomedllama` |
| MedGemma 4B, Q4_K_S | `medgemma` |
| GPT-5 nano (model-version ablation only) | `gpt`, in `ablation_gpt5nano/` and `paper_analysis/exp23_results/` |

## Repository layout

```
persona_study/
  src/                     context construction, generation, post-processing, measurement
    providers/             one client per model
  prompts/                 base instruction, persona texts (Table 1), simulated-patient prompt
  config*.yaml             run settings
  data/
    frozen/                OSCE context set and manifest with its SHA-256 hash
    aci_bench/             ACI-Bench context set and manifest with its SHA-256 hash
    prior_study/           targets of the earlier study, used only to keep the context sets disjoint
  outputs/
    main_<model>_cleaned.csv       Experiment 1 outputs
    rollouts/<model>_cleaned.csv   Experiment 2 outputs (clinician and simulated-patient turns)
    aci_<model>_cleaned.csv        Experiment 3 outputs
    ablation_gpt5nano/             GPT-5 nano outputs and results
  reports/                 run reports (requests, failures, tokens) and measurement reports
  analysis/
    analysis_plan_v1.yaml  versioned analysis plan: markers, predictions, classifier, seed
    features_<model>.csv   markers for every Experiment 1 output
    results/<model>/       accuracy, recall, confusion matrices, verdicts, realization, position models
    family_comparison/     Llama-3-8B-Instruct versus its bio-medical fine-tune
    testability/           degree of realization (R, R*) and testability sensitivity analysis
    reviewer_robustness/   effect-size tables, baseline comparison, matched-length position analysis
    external_validation/   measurement-instrument ablation (Empath, ConvoKit)
    length_matched/        output-length ablation (first 25 words)
paper_analysis/
  analysis_exp2_exp3.py    Experiments 2 and 3
  heldout_six_q4.py        classifier trained on five models and tested on the sixth
  make_figures.py, make_fig_family.py, make_fig_experiments.py
  exp23_results*/          Experiment 2 and 3 results
  figures/                 Figures 1 to 3
```

## Where each result in the paper comes from

| In the paper | Files |
|---|---|
| Table 1 (persona instructions) | `persona_study/prompts/p2_prompts_v1.yaml` |
| Figure 1 | `paper_analysis/make_fig_experiments.py` |
| Section 4.1 (discriminability) | `persona_study/analysis/results/<model>/b_accuracy.csv`, `b_recall.csv`, `b_confusion.csv` |
| Section 4.2, held-out model | `paper_analysis/exp23_results_med/heldout6q4_*.csv` |
| Table 2 (verdicts) | `persona_study/analysis/results/<model>/c_predictions.csv`, `c_realised.csv` |
| Table 2 (degree of realization; sensitivity rule) | `persona_study/analysis/testability/graded_realization.csv`, `testability_realised.csv` |
| Section 4.3, Figure 2 | `persona_study/analysis/family_comparison/` |
| Section 4.4, Figure 3a | `results/<model>/b_accuracy.csv`, `b1_gee.csv`; `reviewer_robustness/position_length_overlap.csv` |
| Section 4.5, Figure 3b | `paper_analysis/exp23_results*/roll_*.csv` |
| Table 3 (ACI-Bench) | `paper_analysis/exp23_results*/aci_*.csv` |
| Section 4.7, model version | `persona_study/outputs/ablation_gpt5nano/` |
| Section 4.7, output length | `persona_study/analysis/length_matched/` |
| Section 4.7, measurement instrument | `persona_study/analysis/external_validation/` |
| Table A1 (effect sizes) | `results/<model>/c_predictions.csv`; `reviewer_robustness/effect_sizes.tex` |
| Table A3 (sensitivity analysis) | `persona_study/analysis/testability/testability_sweep.csv` |
| Appendix B, multiplicity | `p_holm` column of `results/<model>/c_predictions.csv` |
| Supplement S6, Table S5 | `reviewer_robustness/family_baseline.tex` |

Results are split across folders by model:

- **Experiment 2 and 3 results.** `paper_analysis/exp23_results/` holds Gemini and Claude, and its `gpt` rows are GPT-5 nano. GPT-4o mini is in `exp23_results_gpt4o/`, Llama-3-8B-Instruct in `exp23_results_llama3q4/`, the bio-medical Llama in `exp23_results_biomed/`, and MedGemma in `exp23_results_med/`.
- **Measurement-instrument ablation.** In `external_validation/`, the top-level files hold Gemini, Claude, MedGemma and, in the `gpt` columns, GPT-5 nano. GPT-4o mini, the bio-medical Llama and Llama-3-8B-Instruct are in the subfolders.

The human annotation (Table A2) is not included in this release.

## Reproducing the analyses

All analyses read the outputs in this repository and call no model. Run the commands from the repository root with Python 3.10.

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz

python paper_analysis/analysis_exp2_exp3.py paper_analysis/exp23_results_llama3q4 llama3instruct llama3instruct
python paper_analysis/heldout_six_q4.py
python persona_study/analysis/family_comparison/family_comparison.py
python persona_study/analysis/testability/persona_testability.py
python persona_study/analysis/testability/graded_realization.py
python persona_study/analysis/reviewer_robustness/position_length_overlap.py
python persona_study/analysis/reviewer_robustness/appendix_tables.py
python paper_analysis/make_figures.py
```

The Experiment 1 measurement is `persona_study/src/run_measurement.py` (see `--help`). Confidence intervals use a cluster bootstrap over dialogues with 2,000 resamples and seed 20261002.

Generating new outputs needs API keys (`GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`). The open-weight models also need an OpenAI-compatible server at `http://localhost:1234/v1`, such as LM Studio, serving the GGUF weights given in Supplement S2. The context sets in `persona_study/data/` are the frozen sets used in the paper. You can check them against their SHA-256 hashes:

| Context set | SHA-256 |
|---|---|
| OSCE | `4ed0b5b043ed0bf4446fce7cba3332bcc8a2f2d63c7908ad24877486e3d6b36d` |
| ACI-Bench | `1fd9767e8359070740fe9478137c5839d3a8b1fcf3baee5665a36f2168ceac61` |

## Data sources

- **OSCE corpus:** Fareez et al. (2022), *A dataset of simulated patient-physician medical interviews with a focus on respiratory cases*, Scientific Data 9:313.
- **ACI-Bench:** Yim et al. (2023), *ACI-BENCH: a novel ambient clinical intelligence dataset for benchmarking automatic visit note generation*, Scientific Data 10:586.

The original transcripts and recordings are not redistributed. The context files contain only the dialogue prefixes that were given to the models. Rebuilding the context sets from scratch requires the original corpora.

## Licence

The code is released under the MIT License (`LICENSE`). Generated outputs and derived results are released under CC BY 4.0. The context sets are excerpts of the corpora above and remain subject to their licences, so please cite both when using them.
