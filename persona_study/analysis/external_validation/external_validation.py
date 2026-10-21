"""Post hoc external validation of the Experiment 1 style markers with Empath and ConvoKit.

Specified on 2026-10-05 after the Experiment 1 results were known; mapping fixed in
prespec_mapping.md before scoring. Reanalysis of existing outputs only: no model is called and
no existing file is changed. Writes only to analysis/external_validation/.
"""
from __future__ import annotations

import hashlib
import importlib.metadata as md
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")
PROJECT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT / "src"))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy.stats import spearmanr  # noqa: E402
import run_measurement as rm  # noqa: E402

OUT = Path(__file__).resolve().parent
MODELS = ["gemini", "claude", "gpt", "llama2chat", "medgemma"]
VERSIONS = ["FULL", "T25"]
PSY = ["emotional", "sadness", "fear", "nervousness", "suffering", "positive_emotion", "negative_emotion",
       "sympathy", "family", "friends", "home", "work", "leisure", "children"]
MED = ["health", "medical_emergency", "body", "pain"]
CK = ["Hedges", "HASHEDGE", "2nd_person_start", "1st_person_start", "Direct_question"]

# (existing marker, external measure) for analysis A
PAIRS = [
    ("psychosocial_per_100", "empath_psychosocial_per_100"),
    ("med_per_100", "empath_medical_per_100"),
    ("hedge_per_100", "ck_Hedges_per_100"),
    ("hedge_per_100", "ck_HASHEDGE_present"),
    ("instruction_per_100", "ck_2nd_person_start_per_100"),
    ("plan_statement_present", "ck_1st_person_start_present"),
    ("has_question", "ck_Direct_question_present"),
]
# (left, right, existing marker, external measure, direction, status) for analysis B
PREDICTIONS = [
    ("P1", "P0", "psychosocial_per_100", "empath_psychosocial_per_100", "lower", "prediction"),
    ("P2", "P1", "psychosocial_per_100", "empath_psychosocial_per_100", "higher", "prediction"),
    ("P3", "P0", "psychosocial_per_100", "empath_psychosocial_per_100", "higher", "prediction"),
    ("P4", "P0", "psychosocial_per_100", "empath_psychosocial_per_100", "higher", "prediction"),
    ("P4", "P3", "psychosocial_per_100", "empath_psychosocial_per_100", "higher", "prediction"),
    ("P1", "P0", "med_per_100", "empath_medical_per_100", "higher", "prediction"),
    ("P4", "P0", "med_per_100", "empath_medical_per_100", "lower", "prediction"),
    ("P4", "P3", "med_per_100", "empath_medical_per_100", "lower", "prediction"),
    ("P5", "P0", "instruction_per_100", "ck_2nd_person_start_present", "higher", "prediction"),
    ("P5", "P0", "plan_statement_present", "ck_1st_person_start_present", "higher", "prediction"),
    ("P5", "P0", "has_question", "ck_Direct_question_present", "lower", "prediction"),
    ("P5", "P0", "hedge_per_100", "ck_Hedges_present", None, "exploratory"),
    ("P5", "P0", "hedge_per_100", "ck_HASHEDGE_present", None, "exploratory"),
]
# Secondary: ConvoKit counts per 100 words for the same P5 contrasts.
SECONDARY = [
    ("P5", "P0", "instruction_per_100", "ck_2nd_person_start_per_100", "higher", "prediction (count)"),
    ("P5", "P0", "plan_statement_present", "ck_1st_person_start_per_100", "higher", "prediction (count)"),
    ("P5", "P0", "has_question", "ck_Direct_question_per_100", "lower", "prediction (count)"),
    ("P5", "P0", "hedge_per_100", "ck_Hedges_per_100", None, "exploratory (count)"),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def t25(text: str) -> str:
    return " ".join(str(text).split()[:25])


def score_external(texts: pd.Series) -> pd.DataFrame:
    from empath import Empath
    from convokit import Corpus, PolitenessStrategies, Speaker, TextParser, Utterance

    lex = Empath()
    n_words = texts.str.split().str.len().astype(float)
    rows = []
    for text, nw in zip(texts, n_words):
        scores = lex.analyze(text, categories=PSY + MED, normalize=True) or {}
        row = {f"empath_{c}_per_100": 100.0 * float(scores.get(c, 0.0) or 0.0) for c in PSY + MED}
        row["empath_psychosocial_per_100"] = sum(row[f"empath_{c}_per_100"] for c in PSY)
        row["empath_medical_per_100"] = sum(row[f"empath_{c}_per_100"] for c in MED)
        rows.append(row)
    empath = pd.DataFrame(rows, index=texts.index)

    speaker = Speaker(id="doctor")
    utts = [Utterance(id=str(i), speaker=speaker, text=str(t)) for i, t in zip(texts.index, texts)]
    corpus = Corpus(utterances=utts)
    corpus = TextParser(verbosity=0).transform(corpus)
    corpus = PolitenessStrategies(verbose=0).transform(corpus, markers=True)
    ck_rows = []
    for i, nw in zip(texts.index, n_words):
        meta = corpus.get_utterance(str(i)).meta
        strategies = meta["politeness_strategies"]
        markers = meta.get("politeness_markers", {})
        row = {}
        for name in CK:
            row[f"ck_{name}_present"] = int(strategies[f"feature_politeness_=={name}=="] > 0)
            count = len(markers.get(f"politeness_markers_=={name}==", []) or [])
            row[f"ck_{name}_count"] = count
            row[f"ck_{name}_per_100"] = 100.0 * count / nw if nw > 0 else np.nan
        ck_rows.append(row)
    return pd.concat([empath, pd.DataFrame(ck_rows, index=texts.index)], axis=1)


def spearman_ci(x: np.ndarray, y: np.ndarray, groups: np.ndarray, plan: dict, seed: int):
    ok = ~(np.isnan(x) | np.isnan(y))
    x, y, groups = x[ok], y[ok], groups[ok]
    point = float(spearmanr(x, y).correlation)
    unique = np.unique(groups)
    index = {g: np.flatnonzero(groups == g) for g in unique}
    rng = np.random.default_rng(seed)
    draws = np.empty(int(plan["bootstrap_resamples"]))
    for b in range(len(draws)):
        chosen = np.concatenate([index[g] for g in rng.choice(unique, len(unique), replace=True)])
        draws[b] = spearmanr(x[chosen], y[chosen]).correlation
    low, high = rm.percentile_ci(draws)
    return point, low, high, int(ok.sum())


def paired(features: pd.DataFrame, marker: str, left: str, right: str, plan: dict, seed: int):
    wide = rm.paired_frame(features, marker)
    diff = (wide[left] - wide[right]).dropna()
    est, low, high, p = rm.bootstrap_mean(diff, wide["dialogue_id"], plan, seed)
    return est, low, high, len(diff)


def main() -> None:
    plan = rm.load_plan(rm.PLAN_PATH)
    seed = int(plan["seed"])
    np.random.seed(seed)
    config = rm.load_config(PROJECT / "config.yaml")
    _frames, frozen, persona_texts = rm.load_inputs(config)

    log = ["# External validation log", "", f"Run at {datetime.now(timezone.utc).isoformat()}", "",
           "Post hoc validation, specified on 2026-10-05 after the Experiment 1 results were known.",
           "Mapping fixed in prespec_mapping.md before scoring. No model API was called; no existing file was modified.",
           "", "## Package versions", ""]
    for pkg in ["empath", "convokit", "spacy", "en_core_web_sm", "scispacy", "numpy", "pandas", "scipy", "scikit-learn"]:
        try:
            log.append(f"- {pkg} {md.version(pkg)}")
        except md.PackageNotFoundError:
            log.append(f"- {pkg} not found")
    log += ["", "## Input file SHA-256", ""]
    for path in [PROJECT / f"outputs/main_{m}_cleaned.csv" for m in MODELS] + \
                [PROJECT / f"analysis/features_{m}.csv" for m in MODELS] + \
                [PROJECT / f"analysis/results/{m}/c_predictions.csv" for m in MODELS] + \
                [rm.PLAN_PATH, PROJECT / "src/run_measurement.py", PROJECT / "src/measure_text.py", OUT / "prespec_mapping.md", Path(__file__)]:
        log.append(f"- `{path.relative_to(PROJECT)}`: `{sha(path)}`")

    a_rows, b_rows, d_rows = [], [], []
    for model in MODELS:
        outputs = pd.read_csv(PROJECT / f"outputs/main_{model}_cleaned.csv")
        original = pd.read_csv(PROJECT / f"analysis/results/{model}/c_predictions.csv")
        original = original.loc[original["scope"] == "overall"]
        for version in VERSIONS:
            print(f"{model} {version}", flush=True)
            text = outputs.copy()
            if version == "T25":
                text["analysis_text"] = text["analysis_text"].map(t25)
                mine, _echo = rm.build_features(model, text, frozen, persona_texts, plan, "na")
                mine = rm.usable_rows(mine)
            else:
                mine = pd.read_csv(PROJECT / f"analysis/features_{model}.csv")
                mine = mine.loc[mine["missing_analysis"] == 0]
            ext = score_external(text["analysis_text"].fillna("").astype(str))
            ext = pd.concat([text[["context_id", "condition"]], ext], axis=1)
            data = mine.merge(ext, on=["context_id", "condition"], how="inner", validate="one_to_one")
            data.drop(columns=[c for c in data.columns if c == "plan_sha256"]).to_csv(
                OUT / f"scores_{version}_{model}.csv", index=False)
            groups = data["dialogue_id"].astype(str).to_numpy()
            # A. convergence
            for marker, external in PAIRS:
                r, low, high, n = spearman_ci(data[marker].to_numpy(float), data[external].to_numpy(float), groups, plan, seed)
                a_rows.append({"version": version, "model": model, "marker": marker, "external": external,
                               "spearman": r, "ci_low": low, "ci_high": high, "n": n})
            # B. replication
            for left, right, marker, external, direction, status in PREDICTIONS + SECONDARY:
                e_est, e_low, e_high, n = paired(data, external, left, right, plan, seed)
                m_est, m_low, m_high, _ = paired(data, marker, left, right, plan, seed)
                orig = original.loc[(original["contrast"] == f"{left} - {right}") & (original["marker"] == marker)]
                b_rows.append({
                    "version": version, "model": model, "contrast": f"{left} - {right}", "status": status,
                    "direction": direction or "", "marker": marker, "external": external,
                    "marker_estimate": m_est, "marker_ci_low": m_low, "marker_ci_high": m_high,
                    "marker_verdict_this_text": rm.verdict(m_low, m_high, direction) if direction else "",
                    "marker_verdict_original_full_text": (orig["verdict"].iloc[0] if len(orig) else "no original prediction"),
                    "external_estimate": e_est, "external_ci_low": e_low, "external_ci_high": e_high,
                    "external_verdict": rm.verdict(e_low, e_high, direction) if direction else "", "n_pairs": n,
                })
            # D. per-category Empath differences
            for left, right in [("P4", "P0"), ("P1", "P0")]:
                for cat in PSY + MED:
                    est, low, high, n = paired(data, f"empath_{cat}_per_100", left, right, plan, seed)
                    d_rows.append({"version": version, "model": model, "contrast": f"{left} - {right}",
                                   "category": cat, "composite": "psychosocial" if cat in PSY else "medical",
                                   "estimate_per_100": est, "ci_low": low, "ci_high": high, "n_pairs": n})

    a = pd.DataFrame(a_rows); b = pd.DataFrame(b_rows); d = pd.DataFrame(d_rows)
    for version in VERSIONS:
        a.loc[a["version"] == version].to_csv(OUT / f"A_convergence_{version}.csv", index=False)
        b.loc[b["version"] == version].to_csv(OUT / f"B_replication_{version}.csv", index=False)
        d.loc[d["version"] == version].to_csv(OUT / f"D_empath_categories_{version}.csv", index=False)
        # C. agreement table: original full-text verdict vs external verdict, primary predictions only
        c = b.loc[(b["version"] == version) & (b["status"] == "prediction")].copy()
        c["agree"] = (c["marker_verdict_original_full_text"] == c["external_verdict"]).astype(int)
        table = c.pivot_table(index=["contrast", "marker", "external", "direction"], columns="model",
                              values=["marker_verdict_original_full_text", "external_verdict"], aggfunc="first")
        table.columns = [f"{model}_{'original' if kind.startswith('marker') else 'external'}" for kind, model in table.columns]
        table = table[[f"{m}_{k}" for m in MODELS for k in ("original", "external")]]
        agree = c.groupby(["contrast", "marker", "external", "direction"])["agree"].sum().rename("n_models_agree")
        table = table.join(agree).reset_index()
        table.to_csv(OUT / f"C_agreement_{version}.csv", index=False)
        totals = c.groupby("model")["agree"].agg(["sum", "count"]).reset_index()
        totals.to_csv(OUT / f"C_agreement_totals_{version}.csv", index=False)
    (OUT / "log.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
