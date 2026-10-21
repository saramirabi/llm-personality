# External validation: pre-specified mapping

Date written: 2026-10-05, before any output was scored with Empath or ConvoKit.

Post hoc validation, specified after the Experiment 1 results were known. Reanalysis of existing
Experiment 1 (OSCE) outputs of five models (gemini, claude, gpt, llama2chat, medgemma), using
`analysis_text` (the text after the patient-label rule), on full text and on the first 25
whitespace-separated words. No model is called and no existing file is changed.

## Mapping (fixed)

| Existing marker | External measure |
| --- | --- |
| psychosocial rate (`psychosocial_per_100`) | Empath psychosocial composite: emotional, sadness, fear, nervousness, suffering, positive_emotion, negative_emotion, sympathy, family, friends, home, work, leisure, children |
| medical-term density (`med_per_100`) | Empath medical composite: health, medical_emergency, body, pain |
| hedges rate (`hedge_per_100`) | ConvoKit Hedges (and HASHEDGE) |
| instructions rate (`instruction_per_100`) | ConvoKit 2nd_person_start |
| plan statements (`plan_statement_present`) | ConvoKit 1st_person_start |
| any-question share (`has_question`) | ConvoKit Direct_question (rough proxy only) |

Empath: built-in categories only, `analyze(normalize=True)`, converted to a rate per 100 words;
composite = sum of the listed categories; per-category values kept. `create_category` is not used.

ConvoKit: one utterance per output, parsed, PolitenessStrategies applied. Binary presence per
output, and count per 100 words where the tool provides counts.

## Analyses (per model, existing cluster bootstrap, 2,000 resamples by dialogue, plan seed)

- A. Convergence: Spearman correlation between each existing marker and its mapped external
  measure at output level, with 95% interval.
- B. Replication with the external measure in place of the marker, as paired differences on the
  same context, same verdict rule:
  - psychosocial: P1-P0 down, P2-P1 up, P3-P0 up, P4-P0 up, P4-P3 up
  - medical: P1-P0 up, P4-P0 down, P4-P3 down
  - P5-P0: 2nd_person_start up, 1st_person_start up, Direct_question down
  - Hedges: P5-P0 reported as exploratory (no prediction).
- C. Agreement table: existing verdict next to external verdict, per prediction and model.
- D. Empath per-category differences for P4-P0 and P1-P0.

If any Empath category or ConvoKit feature name above is missing in the installed version, the
analysis stops and nothing is substituted.
