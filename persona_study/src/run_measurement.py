"""Run the pre-specified measurement plan. No generation and no API calls."""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
from pathlib import Path

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler

SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))

from generate import load_config  # noqa: E402
from measure_text import (  # noqa: E402
    basic_features,
    content_words,
    lexicon_count,
    load_plan,
    per_hundred,
    question_features,
    tokenize,
)
from prompting import load_prompt_file  # noqa: E402

PROJECT = SRC.parent
PLAN_PATH = PROJECT / "analysis" / "analysis_plan_v1.yaml"
RESULTS = PROJECT / "analysis" / "results"
FIGURES = RESULTS / "figures"
CONDITIONS = ["P0", "P1", "P2", "P3", "P4", "P5"]
POSITIONS = ["Early", "Middle", "Late"]
LEXICON_NAMES = [
    "emotion",
    "life_context",
    "empathy_phrases",
    "instruction",
    "plan_statement",
    "invitation",
    "hedge",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def assert_allowed(path: Path) -> None:
    name = path.name.lower()
    if "pilot" in name or "human_reference" in name:
        raise SystemExit(f"Refusing to read {path.name}.")


def model_slug(path: Path) -> str:
    name = path.name
    if name.startswith("main_") and name.endswith("_cleaned.csv"):
        return name[len("main_") : -len("_cleaned.csv")]
    return path.stem


def write_csv(frame: pd.DataFrame, path: Path, plan_sha: str) -> None:
    out = frame.copy()
    out["plan_sha256"] = plan_sha
    path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(path, index=False)


def md_table(frame: pd.DataFrame, columns: list[str]) -> str:
    show = frame[columns].copy()
    for column in show.columns:
        if pd.api.types.is_float_dtype(show[column]):
            show[column] = show[column].map(lambda value: "" if pd.isna(value) else f"{value:.4f}")
        else:
            show[column] = show[column].map(lambda value: "" if pd.isna(value) else str(value))
    header = "| " + " | ".join(columns) + " |"
    rule = "| " + " | ".join("---" for _ in columns) + " |"
    lines = [header, rule]
    for row in show.itertuples(index=False):
        lines.append("| " + " | ".join(str(item) for item in row) + " |")
    return "\n".join(lines)


def load_inputs(config: dict) -> tuple[list[tuple[str, pd.DataFrame]], pd.DataFrame, list[str]]:
    files = config.get("analysis_output_files")
    if not isinstance(files, list) or not files:
        raise SystemExit("config.yaml needs analysis_output_files.")
    frozen_path = PROJECT / str(config["frozen_dir"]) / str(config["main_frozen_filename"])
    prompt_path = PROJECT / str(config["prompt_file"])
    assert_allowed(frozen_path)
    assert_allowed(prompt_path)
    frozen = pd.read_csv(frozen_path, usecols=["context_id", "context_word_count"])
    prompts = load_prompt_file(prompt_path)
    personas = prompts["personas"]
    persona_texts = [text for text in personas.values() if isinstance(text, str)]
    frames = []
    for item in files:
        path = PROJECT / str(item)
        assert_allowed(path)
        frame = pd.read_csv(
            path,
            usecols=[
                "context_id",
                "dialogue_id",
                "position",
                "condition",
                "analysis_text",
                "flag_empty",
                "flag_truncated",
                "flag_patient_turn",
                "flag_multiple_doctor_turns",
                "flag_refusal_or_ai_meta",
            ],
        )
        frames.append((model_slug(path), frame))
    return frames, frozen, persona_texts


def build_features(
    model: str,
    outputs: pd.DataFrame,
    frozen: pd.DataFrame,
    persona_texts: list[str],
    plan: dict,
    plan_sha: str,
) -> tuple[pd.DataFrame, set[str]]:
    echo = content_words(persona_texts, set(ENGLISH_STOP_WORDS))
    rows: list[dict] = []
    texts: list[str] = []
    usable: list[bool] = []
    for record in outputs.itertuples(index=False):
        text = "" if pd.isna(record.analysis_text) else str(record.analysis_text)
        missing = text.strip() == ""
        row = {
            "model": model,
            "context_id": record.context_id,
            "dialogue_id": record.dialogue_id,
            "position": record.position,
            "condition": record.condition,
            "missing_analysis": int(missing),
            "flag_empty": int(record.flag_empty),
            "flag_truncated": int(record.flag_truncated),
            "flag_patient_turn": int(record.flag_patient_turn),
            "flag_multiple_doctor_turns": int(record.flag_multiple_doctor_turns),
            "flag_refusal_or_ai_meta": int(record.flag_refusal_or_ai_meta),
        }
        if missing:
            rows.append(row)
            texts.append("")
            usable.append(False)
            continue
        basic = basic_features(text)
        questions = question_features(text, plan)
        tokens = tokenize(text)
        n_words = int(basic["n_words"])
        row.update(basic)
        row.update(questions)
        for name in LEXICON_NAMES:
            count = lexicon_count(tokens, plan["lexicons"][name])
            row[f"n_{name}"] = count
            row[f"{name}_per_100"] = per_hundred(count, n_words)
            row[f"{name}_present"] = int(count > 0)
        emotion_rate = row["emotion_per_100"]
        life_rate = row["life_context_per_100"]
        row["psychosocial_per_100"] = (
            None if emotion_rate is None or life_rate is None else emotion_rate + life_rate
        )
        echo_emotion = lexicon_count(tokens, plan["lexicons"]["emotion"], echo)
        echo_life = lexicon_count(tokens, plan["lexicons"]["life_context"], echo)
        echo_emotion_rate = per_hundred(echo_emotion, n_words)
        echo_life_rate = per_hundred(echo_life, n_words)
        row["psychosocial_echo_free"] = (
            None
            if echo_emotion_rate is None or echo_life_rate is None
            else echo_emotion_rate + echo_life_rate
        )
        rows.append(row)
        texts.append(text)
        usable.append(True)

    import spacy

    nlp = spacy.load("en_core_sci_sm")
    entity_counts = [0] * len(texts)
    live = [text for text, keep in zip(texts, usable) if keep]
    live_index = [index for index, keep in enumerate(usable) if keep]
    for index, doc in zip(live_index, nlp.pipe(live, batch_size=128)):
        entity_counts[index] = len(doc.ents)
    for index, row in enumerate(rows):
        if not usable[index]:
            row["med_entity_count"] = None
            row["med_per_100"] = None
            continue
        count = entity_counts[index]
        row["med_entity_count"] = count
        row["med_per_100"] = per_hundred(count, int(row["n_words"]))

    from sentence_transformers import SentenceTransformer

    encoder = SentenceTransformer(plan["packages"]["sentence_transformer_model"])
    vectors = [None] * len(texts)
    if live:
        encoded = encoder.encode(live, normalize_embeddings=True, show_progress_bar=False)
        for index, vector in zip(live_index, encoded):
            vectors[index] = np.asarray(vector)
    by_key = {
        (row["context_id"], row["condition"]): vectors[index]
        for index, row in enumerate(rows)
    }
    for index, row in enumerate(rows):
        own = vectors[index]
        reference = by_key.get((row["context_id"], "P0"))
        if own is None or reference is None:
            row["persona_distance"] = None
        else:
            row["persona_distance"] = float(1.0 - np.dot(own, reference))

    features = pd.DataFrame(rows)
    features = features.merge(frozen, on="context_id", how="left", validate="many_to_one")
    if features["context_word_count"].isna().any():
        raise SystemExit("A context_id is missing from p2_contexts_FROZEN.csv.")
    features["plan_sha256"] = plan_sha
    return features, echo


B4_FEATURES = [
    "n_words",
    "n_sentences",
    "n_questions",
    "has_question",
    "n_open",
    "n_closed",
    "n_other_q",
    "share_open",
    "med_per_100",
    "emotion_per_100",
    "emotion_present",
    "life_context_per_100",
    "life_context_present",
    "empathy_phrases_per_100",
    "empathy_phrases_present",
    "instruction_per_100",
    "instruction_present",
    "plan_statement_per_100",
    "plan_statement_present",
    "invitation_per_100",
    "invitation_present",
    "hedge_per_100",
    "hedge_present",
    "n_leading",
    "leading_present",
    "psychosocial_per_100",
    "psychosocial_echo_free",
]


def usable_rows(features: pd.DataFrame) -> pd.DataFrame:
    return features.loc[features["missing_analysis"] == 0].copy()


def first_words(text: str, n_words: int) -> str:
    return " ".join(tokenize(text)[:n_words])


def remove_words(text: str, blocked: set[str]) -> str:
    return " ".join(token for token in tokenize(text) if token not in blocked)


def classifier(seed: int, plan: dict) -> LogisticRegression:
    return LogisticRegression(
        max_iter=int(plan["logistic"]["max_iter"]),
        C=float(plan["logistic"]["C"]),
        random_state=seed,
    )


def vectorizer(plan: dict) -> TfidfVectorizer:
    ngram = plan["tfidf"]["ngram_range"]
    return TfidfVectorizer(
        ngram_range=(int(ngram[0]), int(ngram[1])),
        min_df=int(plan["tfidf"]["min_df"]),
        sublinear_tf=bool(plan["tfidf"]["sublinear_tf"]),
    )


def oof_text(texts: np.ndarray, labels: np.ndarray, groups: np.ndarray, plan: dict, seed: int) -> np.ndarray:
    predicted = np.empty(len(labels), dtype=object)
    splitter = GroupKFold(n_splits=int(plan["group_kfold_splits"]))
    for train, test in splitter.split(np.zeros(len(labels)), labels, groups):
        vec = vectorizer(plan)
        train_x = vec.fit_transform(texts[train])
        test_x = vec.transform(texts[test])
        model = classifier(seed, plan)
        model.fit(train_x, labels[train])
        predicted[test] = model.predict(test_x)
    return predicted


def oof_matrix(values: np.ndarray, labels: np.ndarray, groups: np.ndarray, plan: dict, seed: int, scale: bool) -> np.ndarray:
    predicted = np.empty(len(labels), dtype=object)
    splitter = GroupKFold(n_splits=int(plan["group_kfold_splits"]))
    for train, test in splitter.split(np.zeros(len(labels)), labels, groups):
        train_x = values[train]
        test_x = values[test]
        imputer = SimpleImputer(strategy="median")
        train_x = imputer.fit_transform(train_x)
        test_x = imputer.transform(test_x)
        if scale:
            scaler = StandardScaler()
            train_x = scaler.fit_transform(train_x)
            test_x = scaler.transform(test_x)
        model = classifier(seed, plan)
        model.fit(train_x, labels[train])
        predicted[test] = model.predict(test_x)
    return predicted


def variant_texts(frame: pd.DataFrame, variant: str, echo: set[str], plan: dict) -> np.ndarray:
    raw = frame["analysis_text"].astype(str).to_numpy()
    if variant == "B1":
        return raw
    if variant == "B2":
        limit = int(plan["length_control_words"])
        return np.array([first_words(text, limit) for text in raw], dtype=object)
    if variant == "B3":
        return np.array([remove_words(text, echo) for text in raw], dtype=object)
    if variant == "B6":
        return raw
    raise ValueError(variant)


def prepare_variant(frame: pd.DataFrame, variant: str, echo: set[str], plan: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray, list[str], float, str]:
    data = frame
    chance = float(plan["chance_six"])
    kind = "text"
    labels_order = CONDITIONS.copy()
    if variant == "B6":
        data = frame.loc[frame["condition"] != "P0"].copy()
        chance = float(plan["chance_five"])
        labels_order = ["P1", "P2", "P3", "P4", "P5"]
    elif variant == "B7":
        data = frame.copy()
        data["condition"] = data["condition"].replace({"P1": "P1P2", "P2": "P1P2"})
        chance = float(plan["chance_five"])
        labels_order = ["P0", "P1P2", "P3", "P4", "P5"]
        kind = "text"
    labels = data["condition"].to_numpy()
    groups = data["dialogue_id"].astype(str).to_numpy()
    if variant in {"B1", "B2", "B3", "B6", "B7"}:
        texts = variant_texts(data, "B1" if variant == "B7" else variant, echo, plan)
        if variant == "B7":
            texts = data["analysis_text"].astype(str).to_numpy()
        return texts, labels, groups, labels_order, chance, "text"
    if variant == "B4":
        matrix = data[B4_FEATURES].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float)
        return matrix, labels, groups, labels_order, chance, "matrix"
    if variant == "B5":
        matrix = np.log1p(data["n_words"].to_numpy(dtype=float)).reshape(-1, 1)
        return matrix, labels, groups, labels_order, chance, "matrix_unscaled"
    raise ValueError(variant)


def fit_variant(frame: pd.DataFrame, variant: str, echo: set[str], plan: dict, seed: int) -> pd.DataFrame:
    values, labels, groups, order, chance, kind = prepare_variant(frame, variant, echo, plan)
    if kind == "text":
        predicted = oof_text(values, labels, groups, plan, seed)
    elif kind == "matrix":
        predicted = oof_matrix(values, labels, groups, plan, seed, scale=True)
    else:
        predicted = oof_matrix(values, labels, groups, plan, seed, scale=False)
    source = frame if variant not in {"B6"} else frame.loc[frame["condition"] != "P0"]
    if variant == "B7":
        source = frame
    out = source[["model", "context_id", "dialogue_id", "position", "condition"]].copy()
    if variant == "B7":
        out["y_true"] = out["condition"].replace({"P1": "P1P2", "P2": "P1P2"})
    elif variant == "B6":
        out["y_true"] = out["condition"]
    else:
        out["y_true"] = out["condition"]
    out["y_pred"] = predicted
    out["variant"] = variant
    out["chance"] = chance
    out["label_order"] = "|".join(order)
    return out.reset_index(drop=True)


def _dialogue_lists(dialogue_ids: np.ndarray) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    unique = np.unique(dialogue_ids)
    mapping = {dialogue: np.flatnonzero(dialogue_ids == dialogue) for dialogue in unique}
    return unique, mapping


def resample(rng: np.random.Generator, unique: np.ndarray, mapping: dict[str, np.ndarray]) -> np.ndarray:
    drawn = rng.choice(unique, size=len(unique), replace=True)
    return np.concatenate([mapping[item] for item in drawn])


def percentile_ci(samples: np.ndarray) -> tuple[float, float]:
    finite = samples[np.isfinite(samples)]
    if len(finite) == 0:
        return (np.nan, np.nan)
    low, high = np.quantile(finite, [0.025, 0.975])
    return float(low), float(high)


def bootstrap_p(samples: np.ndarray) -> float:
    finite = samples[np.isfinite(samples)]
    if len(finite) == 0:
        return np.nan
    return float(min(1.0, 2 * min(np.mean(finite <= 0), np.mean(finite >= 0))))


def metric_tables(predictions: pd.DataFrame, plan: dict, seed: int) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    draws = int(plan["bootstrap_resamples"])
    accuracy_rows = []
    recall_rows = []
    confusion_rows = []
    for variant, block in predictions.groupby("variant", sort=False):
        order = str(block["label_order"].iloc[0]).split("|")
        chance = float(block["chance"].iloc[0])
        y_true = block["y_true"].to_numpy()
        y_pred = block["y_pred"].to_numpy()
        dialogues = block["dialogue_id"].astype(str).to_numpy()
        positions = block["position"].to_numpy()
        unique, mapping = _dialogue_lists(dialogues)
        rng = np.random.default_rng(seed)
        boot_index = [resample(rng, unique, mapping) for _ in range(draws)]
        slices = [("overall", np.ones(len(block), dtype=bool))]
        for position in POSITIONS:
            slices.append((position, positions == position))
        for scope, mask in slices:
            idx = np.flatnonzero(mask)
            point = float(np.mean(y_true[idx] == y_pred[idx])) if len(idx) else np.nan
            scope_mask = np.zeros(len(y_true), dtype=bool)
            scope_mask[idx] = True
            samples = np.empty(len(boot_index))
            for draw_i, draw in enumerate(boot_index):
                chosen = draw[scope_mask[draw]]
                samples[draw_i] = np.mean(y_true[chosen] == y_pred[chosen]) if len(chosen) else np.nan
            low, high = percentile_ci(samples)
            accuracy_rows.append({
                "variant": variant,
                "scope": scope,
                "accuracy": point,
                "ci_low": low,
                "ci_high": high,
                "chance": chance,
                "n": int(len(idx)),
            })
            present = [label for label in order if np.any(y_true[idx] == label)]
            for label in present:
                class_idx = idx[y_true[idx] == label]
                recall = float(np.mean(y_pred[class_idx] == label))
                class_mask = np.zeros(len(y_true), dtype=bool)
                class_mask[class_idx] = True
                recall_samples = np.empty(len(boot_index))
                for draw_i, draw in enumerate(boot_index):
                    chosen = draw[class_mask[draw]]
                    recall_samples[draw_i] = np.mean(y_pred[chosen] == label) if len(chosen) else np.nan
                recall_low, recall_high = percentile_ci(recall_samples)
                recall_rows.append({
                    "variant": variant,
                    "scope": scope,
                    "condition": label,
                    "recall": recall,
                    "ci_low": recall_low,
                    "ci_high": recall_high,
                    "chance": chance,
                    "n": int(len(class_idx)),
                })
            for true_label in order:
                for pred_label in order:
                    count = int(np.sum((y_true[idx] == true_label) & (y_pred[idx] == pred_label))) if len(idx) else 0
                    confusion_rows.append({
                        "variant": variant,
                        "scope": scope,
                        "true_label": true_label,
                        "pred_label": pred_label,
                        "count": count,
                    })
    return pd.DataFrame(accuracy_rows), pd.DataFrame(recall_rows), pd.DataFrame(confusion_rows)


def fit_b1_gee(predictions: pd.DataFrame, features: pd.DataFrame, plan: dict) -> pd.DataFrame:
    block = predictions.loc[predictions["variant"] == "B1"].copy()
    merged = block.merge(
        features[["context_id", "condition", "context_word_count"]],
        on=["context_id", "condition"],
        how="left",
    )
    merged["correct"] = (merged["y_true"] == merged["y_pred"]).astype(int)
    merged["log_context"] = np.log(merged["context_word_count"].astype(float))
    merged = merged.sort_values("dialogue_id")
    try:
        result = smf.gee(
            "correct ~ C(position, Treatment(reference='Early')) + log_context",
            groups="dialogue_id",
            data=merged,
            family=sm.families.Binomial(),
            cov_struct=sm.cov_struct.Exchangeable(),
        ).fit()
        return pd.DataFrame({
            "term": result.params.index,
            "coef": result.params.values,
            "std_err": result.bse.values,
            "p_value": result.pvalues.values,
            "ci_low": result.conf_int()[0].values,
            "ci_high": result.conf_int()[1].values,
        })
    except Exception as exc:  # noqa: BLE001
        return pd.DataFrame([{"term": "FIT_FAILED", "coef": np.nan, "std_err": np.nan, "p_value": np.nan, "ci_low": np.nan, "ci_high": np.nan, "error": str(exc)}])


def paired_frame(features: pd.DataFrame, marker: str) -> pd.DataFrame:
    wide = features.pivot(index="context_id", columns="condition", values=marker)
    meta = features.groupby("context_id")[["dialogue_id", "position"]].first()
    return wide.join(meta)


def contrast_values(wide: pd.DataFrame, left: str, right: str, scope: str) -> pd.Series:
    data = wide if scope == "overall" else wide.loc[wide["position"] == scope]
    diff = data[left] - data[right]
    return diff.dropna()


def bootstrap_mean(values: pd.Series, dialogues: pd.Series, plan: dict, seed: int) -> tuple[float, float, float, float]:
    point = float(values.mean()) if len(values) else np.nan
    if len(values) == 0:
        return point, np.nan, np.nan, np.nan
    dialogue_ids = dialogues.loc[values.index].astype(str).to_numpy()
    unique, mapping = _dialogue_lists(dialogue_ids)
    aligned = values.to_numpy()
    # mapping indexes the current values array, so rebuild from this array's order
    order = pd.Series(np.arange(len(values)), index=values.index)
    groups = dialogues.loc[values.index].astype(str)
    mapping = {dialogue: order.loc[groups.index[groups == dialogue]].to_numpy() for dialogue in unique}
    rng = np.random.default_rng(seed)
    samples = np.empty(int(plan["bootstrap_resamples"]))
    for draw in range(int(plan["bootstrap_resamples"])):
        chosen = resample(rng, unique, mapping)
        samples[draw] = float(np.mean(aligned[chosen]))
    low, high = percentile_ci(samples)
    return point, low, high, bootstrap_p(samples)


def holm(p_values: list[float]) -> list[float]:
    usable = [value for value in p_values if np.isfinite(value)]
    adjusted = [np.nan] * len(p_values)
    order = sorted((index for index, value in enumerate(p_values) if np.isfinite(value)), key=lambda index: p_values[index])
    running = 0.0
    total = len(usable)
    for rank, index in enumerate(order):
        value = min(1.0, (total - rank) * p_values[index])
        running = max(running, value)
        adjusted[index] = running
    return adjusted


def verdict(low: float, high: float, direction: str) -> str:
    if not np.isfinite(low) or not np.isfinite(high):
        return "not confirmed"
    if direction == "higher":
        if low > 0:
            return "confirmed"
        if high < 0:
            return "opposite"
        return "not confirmed"
    if high < 0:
        return "confirmed"
    if low > 0:
        return "opposite"
    return "not confirmed"


def prediction_label(item: dict, model_name: str, plan: dict) -> tuple[str, int]:
    erratum_id = item.get("erratum")
    if erratum_id is None:
        return "pre-specified", 1
    exploratory: set[str] = set()
    for erratum in plan.get("errata") or []:
        if erratum.get("id") == erratum_id:
            exploratory = {str(name) for name in erratum.get("exploratory_models") or []}
    label = "exploratory" if model_name in exploratory else "pre-specified"
    in_realised_rule = 0 if int(erratum_id) == 2 else 1
    return label, in_realised_rule


def prediction_table(features: pd.DataFrame, plan: dict, seed: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    model_name = str(features["model"].iloc[0]) if "model" in features.columns and len(features) else ""
    rows = []
    labels: dict[tuple[str, str], tuple[str, int]] = {}
    for item in plan["predictions"]:
        left, right = item["contrast"]
        marker = item["marker"]
        label, in_rule = prediction_label(item, model_name, plan)
        labels[(f"{left} - {right}", marker)] = (label, in_rule)
        wide = paired_frame(features, marker)
        for scope in ["overall", *POSITIONS]:
            subset = wide if scope == "overall" else wide.loc[wide["position"] == scope]
            diff = (subset[left] - subset[right]).dropna()
            estimate, low, high, p_value = bootstrap_mean(diff, subset["dialogue_id"], plan, seed)
            rows.append({
                "contrast": f"{left} - {right}",
                "left": left,
                "right": right,
                "marker": marker,
                "direction": item["direction"],
                "specification": label,
                "in_realised_rule": in_rule,
                "scope": scope,
                "estimate": estimate,
                "ci_low": low,
                "ci_high": high,
                "p_value": p_value,
                "n_pairs": int(len(diff)),
                "verdict": verdict(low, high, item["direction"]),
            })
    table = pd.DataFrame(rows)
    for marker, index in table.groupby("marker").groups.items():
        overall = [i for i in index if table.at[i, "scope"] == "overall"]
        by_pos = [i for i in index if table.at[i, "scope"] != "overall"]
        for family in (overall, by_pos):
            adjusted = holm([float(table.at[i, "p_value"]) for i in family])
            for i, value in zip(family, adjusted):
                table.at[i, "p_holm"] = value
    h2_rows = []
    for item in plan["predictions"]:
        left, right = item["contrast"]
        wide = paired_frame(features, item["marker"])
        diff = (wide[left] - wide[right]).dropna()
        joined = wide.loc[diff.index, ["dialogue_id", "position"]]
        early = diff.loc[joined["position"] == "Early"]
        late = diff.loc[joined["position"] == "Late"]
        both = pd.concat([
            pd.DataFrame({"diff": early, "arm": "early", "dialogue_id": joined.loc[early.index, "dialogue_id"]}),
            pd.DataFrame({"diff": late, "arm": "late", "dialogue_id": joined.loc[late.index, "dialogue_id"]}),
        ])
        point = float(late.mean() - early.mean()) if len(early) and len(late) else np.nan
        early_values = early.to_numpy(dtype=float)
        late_values = late.to_numpy(dtype=float)
        early_groups = joined.loc[early.index, "dialogue_id"].astype(str).to_numpy()
        late_groups = joined.loc[late.index, "dialogue_id"].astype(str).to_numpy()
        unique = np.unique(np.concatenate([early_groups, late_groups]))
        early_map = {dialogue: np.flatnonzero(early_groups == dialogue) for dialogue in unique}
        late_map = {dialogue: np.flatnonzero(late_groups == dialogue) for dialogue in unique}
        rng = np.random.default_rng(seed)
        sample_array = np.empty(int(plan["bootstrap_resamples"]))
        for draw_i in range(int(plan["bootstrap_resamples"])):
            drawn = rng.choice(unique, size=len(unique), replace=True)
            early_parts = [early_map[item] for item in drawn if len(early_map[item])]
            late_parts = [late_map[item] for item in drawn if len(late_map[item])]
            if not early_parts or not late_parts:
                sample_array[draw_i] = np.nan
                continue
            early_idx = np.concatenate(early_parts)
            late_idx = np.concatenate(late_parts)
            if len(early_idx) == 0 or len(late_idx) == 0:
                sample_array[draw_i] = np.nan
            else:
                sample_array[draw_i] = float(np.mean(late_values[late_idx]) - np.mean(early_values[early_idx]))
        low, high = percentile_ci(sample_array)
        h2_direction = "higher" if item["direction"] == "lower" else "lower"
        label, in_rule = labels[(f"{left} - {right}", item["marker"])]
        h2_rows.append({
            "contrast": f"{left} - {right}",
            "marker": item["marker"],
            "prediction_direction": item["direction"],
            "specification": label,
            "in_realised_rule": in_rule,
            "estimate_late_minus_early": point,
            "ci_low": low,
            "ci_high": high,
            "p_value": bootstrap_p(sample_array),
            "verdict": verdict(low, high, h2_direction),
        })
    h2 = pd.DataFrame(h2_rows)
    adjusted = []
    for marker, index in h2.groupby("marker").groups.items():
        family = list(index)
        adjusted.extend(zip(family, holm([float(h2.at[i, "p_value"]) for i in family])))
    for index, value in adjusted:
        h2.at[index, "p_holm"] = value
    return table, h2


def realised_table(recall: pd.DataFrame, predictions: pd.DataFrame) -> pd.DataFrame:
    b1 = recall.loc[recall["variant"] == "B1"]
    rows = []
    for scope in ["overall", *POSITIONS]:
        for persona in ["P1", "P2", "P3", "P4", "P5"]:
            recall_row = b1.loc[(b1["scope"] == scope) & (b1["condition"] == persona)]
            if recall_row.empty:
                continue
            item = recall_row.iloc[0]
            above = bool(item["ci_low"] > item["chance"])
            matched = predictions.loc[
                (predictions["scope"] == scope)
                & (predictions["left"] == persona)
                & (predictions["right"] == "P0")
            ]
            if "in_realised_rule" in matched.columns:
                matched = matched.loc[matched["in_realised_rule"] == 1]
            confirmed = int((matched["verdict"] == "confirmed").sum()) if len(matched) else 0
            if len(matched) == 0:
                assessment = "not assessed"
                realised_flag = pd.NA
            else:
                realised_flag = int(above and confirmed == len(matched))
                assessment = "realised" if realised_flag == 1 else "not realised"
            rows.append({
                "scope": scope,
                "persona": persona,
                "recall": item["recall"],
                "ci_low": item["ci_low"],
                "ci_high": item["ci_high"],
                "chance": item["chance"],
                "recall_above_chance": int(above),
                "n_predictions_vs_p0": int(len(matched)),
                "n_confirmed_vs_p0": confirmed,
                "realised": realised_flag,
                "assessment": assessment,
            })
    return pd.DataFrame(rows)


def descriptive_table(features: pd.DataFrame) -> pd.DataFrame:
    markers = [
        "has_question",
        "plan_statement_present",
        "empathy_phrases_present",
        "hedge_per_100",
        "n_words",
        "persona_distance",
    ]
    rows = []
    for condition in CONDITIONS:
        for position in ["overall", *POSITIONS]:
            block = features.loc[features["condition"] == condition]
            if position != "overall":
                block = block.loc[block["position"] == position]
            for marker in markers:
                values = pd.to_numeric(block[marker], errors="coerce").dropna()
                rows.append({
                    "condition": condition,
                    "scope": position,
                    "marker": marker,
                    "mean": float(values.mean()) if len(values) else np.nan,
                    "n": int(len(values)),
                })
    return pd.DataFrame(rows)


def fit_marker_gee(features: pd.DataFrame) -> pd.DataFrame:
    specs = {
        "psychosocial_per_100": sm.families.Gaussian(),
        "med_per_100": sm.families.Gaussian(),
        "share_open": sm.families.Gaussian(),
        "instruction_per_100": sm.families.Gaussian(),
        "invitation_per_100": sm.families.Gaussian(),
        "hedge_per_100": sm.families.Gaussian(),
        "n_words": sm.families.Gaussian(),
        "persona_distance": sm.families.Gaussian(),
        "n_leading": sm.families.Poisson(),
        "has_question": sm.families.Binomial(),
        "plan_statement_present": sm.families.Binomial(),
        "empathy_phrases_present": sm.families.Binomial(),
        "leading_present": sm.families.Binomial(),
    }
    rows = []
    for marker, family in specs.items():
        data = features[["dialogue_id", "condition", "position", marker]].copy()
        data[marker] = pd.to_numeric(data[marker], errors="coerce")
        data = data.dropna().sort_values("dialogue_id")
        data = data.rename(columns={marker: "y"})
        try:
            result = smf.gee(
                "y ~ C(condition, Treatment(reference='P0')) * C(position, Treatment(reference='Early'))",
                groups="dialogue_id",
                data=data,
                family=family,
                cov_struct=sm.cov_struct.Exchangeable(),
            ).fit()
            for term in result.params.index:
                rows.append({
                    "marker": marker,
                    "family": family.__class__.__name__,
                    "term": term,
                    "coef": float(result.params[term]),
                    "std_err": float(result.bse[term]),
                    "p_value": float(result.pvalues[term]),
                    "ci_low": float(result.conf_int().loc[term, 0]),
                    "ci_high": float(result.conf_int().loc[term, 1]),
                    "error": "",
                })
        except Exception as exc:  # noqa: BLE001
            rows.append({
                "marker": marker,
                "family": family.__class__.__name__,
                "term": "FIT_FAILED",
                "coef": np.nan,
                "std_err": np.nan,
                "p_value": np.nan,
                "ci_low": np.nan,
                "ci_high": np.nan,
                "error": str(exc),
            })
    return pd.DataFrame(rows)


def cross_model_generalise(text_frames: list[pd.DataFrame], plan: dict, seed: int) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Train on every model but one and test on the held-out model's full text.

    The same vectoriser and logistic regression as Part B are used. The split
    is by model, not GroupKFold. Intervals still resample the held-out model's
    dialogues. The fit is skipped when only one model is present.
    """
    if len(text_frames) < 2:
        skipped = pd.DataFrame([{
            "status": "skipped",
            "reason": "only one model is present",
            "n_models": len(text_frames),
        }])
        return skipped, skipped.iloc[0:0].copy(), skipped.iloc[0:0].copy()
    prediction_rows = []
    for held in text_frames:
        held_name = str(held["model"].iloc[0])
        train_frames = [frame for frame in text_frames if str(frame["model"].iloc[0]) != held_name]
        train = pd.concat(train_frames, ignore_index=True)
        train_names = "|".join(str(frame["model"].iloc[0]) for frame in train_frames)
        vec = vectorizer(plan)
        train_x = vec.fit_transform(train["analysis_text"].astype(str))
        test_x = vec.transform(held["analysis_text"].astype(str))
        fitted = classifier(seed, plan)
        fitted.fit(train_x, train["condition"].to_numpy())
        predicted = fitted.predict(test_x)
        out = held[["model", "context_id", "dialogue_id", "position", "condition"]].copy()
        out["y_true"] = out["condition"]
        out["y_pred"] = predicted
        out["variant"] = "B1_cross"
        out["chance"] = float(plan["chance_six"])
        out["label_order"] = "|".join(CONDITIONS)
        out["held_out_model"] = held_name
        out["train_models"] = train_names
        out["status"] = "ran"
        prediction_rows.append(out)
    predictions = pd.concat(prediction_rows, ignore_index=True)
    accuracy_parts = []
    recall_parts = []
    confusion_parts = []
    for held_name, block in predictions.groupby("held_out_model", sort=False):
        accuracy, recall, confusion = metric_tables(block, plan, seed)
        for frame in (accuracy, recall, confusion):
            frame.insert(0, "held_out_model", held_name)
            frame.insert(1, "train_models", block["train_models"].iloc[0])
            frame.insert(2, "status", "ran")
        accuracy_parts.append(accuracy)
        recall_parts.append(recall)
        confusion_parts.append(confusion)
    return (
        pd.concat(accuracy_parts, ignore_index=True),
        pd.concat(recall_parts, ignore_index=True),
        pd.concat(confusion_parts, ignore_index=True),
    )


def plot_accuracy(accuracy: pd.DataFrame, path: Path, plan_sha: str) -> None:
    use = accuracy.loc[accuracy["variant"].isin(["B1", "B2", "B3"]) & accuracy["scope"].isin(POSITIONS)]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    offsets = {"B1": -0.18, "B2": 0.0, "B3": 0.18}
    for variant, offset in offsets.items():
        block = use.loc[use["variant"] == variant].set_index("scope").loc[POSITIONS]
        x = np.arange(len(POSITIONS)) + offset
        y = block["accuracy"].to_numpy()
        low = y - block["ci_low"].to_numpy()
        high = block["ci_high"].to_numpy() - y
        ax.errorbar(x, y, yerr=np.vstack([low, high]), fmt="o", capsize=3, label=variant)
    ax.axhline(1 / 6, color="0.4", linestyle="--", linewidth=1, label="chance 1/6")
    ax.set_xticks(np.arange(len(POSITIONS)))
    ax.set_xticklabels(POSITIONS)
    ax.set_ylabel("Accuracy")
    ax.set_ylim(0, 1)
    ax.set_title("Accuracy by position")
    ax.legend(frameon=False)
    fig.text(0.01, 0.01, plan_sha, fontsize=6, color="0.4")
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_confusion(confusion: pd.DataFrame, path: Path, plan_sha: str, variant: str, scopes: list[str]) -> None:
    fig, axes = plt.subplots(1, len(scopes), figsize=(4.2 * len(scopes), 4.2))
    if len(scopes) == 1:
        axes = [axes]
    for ax, scope in zip(axes, scopes):
        block = confusion.loc[(confusion["variant"] == variant) & (confusion["scope"] == scope)]
        labels = list(dict.fromkeys(block["true_label"]))
        matrix = np.zeros((len(labels), len(labels)))
        for row in block.itertuples(index=False):
            matrix[labels.index(row.true_label), labels.index(row.pred_label)] = row.count
        image = ax.imshow(matrix, cmap="Blues")
        ax.set_xticks(range(len(labels)), labels, rotation=45, ha="right")
        ax.set_yticks(range(len(labels)), labels)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("True")
        ax.set_title(f"{variant} {scope}")
        for i in range(len(labels)):
            for j in range(len(labels)):
                ax.text(j, i, int(matrix[i, j]), ha="center", va="center", fontsize=7)
        fig.colorbar(image, ax=ax, fraction=0.046)
    fig.text(0.01, 0.01, plan_sha, fontsize=6, color="0.4")
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=140)
    plt.close(fig)


def plot_shifts(predictions: pd.DataFrame, path: Path, plan_sha: str) -> None:
    markers = list(dict.fromkeys(predictions["marker"]))
    fig, axes = plt.subplots(len(markers), 1, figsize=(9, 2.4 * len(markers)), sharex=False)
    colors = {"overall": "black", "Early": "#1b4f72", "Middle": "#148f77", "Late": "#b9770e"}
    for ax, marker in zip(axes, markers):
        block = predictions.loc[predictions["marker"] == marker].copy()
        contrasts = list(dict.fromkeys(block["contrast"]))
        for scope in ["overall", *POSITIONS]:
            part = block.loc[block["scope"] == scope]
            y = np.array([contrasts.index(item) for item in part["contrast"]], dtype=float)
            if scope != "overall":
                y = y + {"Early": -0.18, "Middle": 0.0, "Late": 0.18}[scope]
            x = part["estimate"].to_numpy()
            low = x - part["ci_low"].to_numpy()
            high = part["ci_high"].to_numpy() - x
            ax.errorbar(x, y, xerr=np.vstack([low, high]), fmt="o", color=colors[scope], capsize=2, label=scope)
        ax.axvline(0, color="0.5", linewidth=1)
        ax.set_yticks(range(len(contrasts)), contrasts)
        ax.set_title(marker)
        ax.set_xlabel("Paired difference")
    axes[0].legend(frameon=False, ncol=4, loc="upper right")
    fig.text(0.01, 0.005, plan_sha, fontsize=6, color="0.4")
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=140)
    plt.close(fig)


def changed_conclusions(main: pd.DataFrame, sensitivity: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    left = main[keys + ["verdict"]].rename(columns={"verdict": "verdict_main"})
    right = sensitivity[keys + ["verdict"]].rename(columns={"verdict": "verdict_sensitivity"})
    merged = left.merge(right, on=keys, how="outer")
    merged["changed"] = (merged["verdict_main"] != merged["verdict_sensitivity"]).astype(int)
    return merged


def recorded_plan_hashes(plan: dict, plan_sha: str) -> list[str]:
    lines = [f"Plan SHA-256: `{plan_sha}`"]
    for erratum in plan.get("errata") or []:
        erratum_id = erratum.get("id")
        dated = erratum.get("date")
        original = erratum.get("original_plan_sha256")
        before = erratum.get("plan_sha256_before_this_erratum")
        if original:
            lines.append(f"Erratum {erratum_id} ({dated}) original plan SHA-256: `{original}`")
        if before:
            lines.append(f"Erratum {erratum_id} ({dated}) plan SHA-256 before this erratum: `{before}`")
    return lines


def support_phrase(block: pd.DataFrame, verdict_name: str) -> str:
    if verdict_name == "other":
        chosen = block.loc[~block["verdict"].isin(["confirmed", "opposite"])]
    else:
        chosen = block.loc[block["verdict"] == verdict_name]
    names = []
    for row in chosen.itertuples(index=False):
        spec = getattr(row, "specification", "")
        model_name = str(row.model)
        names.append(f"{model_name} ({spec})" if spec else model_name)
    return ", ".join(names) if names else "no model"


def write_report(
    path: Path,
    model: str,
    plan_sha: str,
    prompt_sha: str,
    features: pd.DataFrame,
    accuracy: pd.DataFrame,
    recall: pd.DataFrame,
    predictions: pd.DataFrame,
    h2: pd.DataFrame,
    realised: pd.DataFrame,
    descriptive: pd.DataFrame,
    gee_b1: pd.DataFrame,
    sensitivity_notes: str,
    echo_count: int,
    plan: dict,
) -> None:
    missing = int(features["missing_analysis"].sum())
    used = features.loc[features["missing_analysis"] == 0]
    flag_cols = [
        "flag_empty",
        "flag_truncated",
        "flag_patient_turn",
        "flag_multiple_doctor_turns",
        "flag_refusal_or_ai_meta",
    ]
    flagged = int((used[flag_cols].sum(axis=1) > 0).sum())
    lines = [
        f"# {model} measurement report",
        "",
        *recorded_plan_hashes(plan, plan_sha),
        f"Prompt SHA-256: `{prompt_sha}`",
        "",
        "No generation was run. Measurements use `analysis_text` only.",
        "",
        "## Data",
        "",
        f"- Output rows: {len(features)}",
        f"- Missing `analysis_text`: {missing}. Those rows stay in the feature file and are excluded from calculations.",
        f"- Rows in the calculations: {len(used)}",
        f"- Contexts: {features['context_id'].nunique()}",
        f"- Rows by condition: {used.groupby('condition').size().to_dict()}",
        f"- Rows by position: {used.groupby('position').size().to_dict()}",
        f"- Rows with any format flag, among analysed rows: {flagged}",
        f"- Persona content words removed for the echo controls: {echo_count}",
        "",
        "## Part B accuracy",
        "",
        md_table(accuracy, ["variant", "scope", "accuracy", "ci_low", "ci_high", "chance", "n"]),
        "",
        "## Part B recall",
        "",
        md_table(recall, ["variant", "scope", "condition", "recall", "ci_low", "ci_high", "chance", "n"]),
        "",
        "## Part B1 GEE",
        "",
        "Logistic GEE of out-of-fold correctness, clustered by dialogue: `correct ~ position + log(context_word_count)`. Working correlation: exchangeable. Position reference: Early.",
        "",
        md_table(gee_b1, [column for column in ["term", "coef", "std_err", "p_value", "ci_low", "ci_high", "error"] if column in gee_b1.columns]),
        "",
        "## Part C predictions",
        "",
        "Verdicts use the pre-specified interval rule. Holm p-values are within each marker and do not change the verdict. Erratum 2 predictions are exploratory for Gemini and Claude, and pre-specified for any model run after 2026-10-02. They are not part of the realised rule.",
        "",
        md_table(predictions, ["scope", "contrast", "marker", "direction", "specification", "estimate", "ci_low", "ci_high", "p_value", "p_holm", "n_pairs", "verdict"]),
        "",
        "## H2 position tests",
        "",
        "The estimate is the Late paired difference minus the Early paired difference. H2 predicts that this move is toward zero: positive when the main prediction is lower, and negative when the main prediction is higher.",
        "",
        md_table(h2, ["contrast", "marker", "prediction_direction", "specification", "estimate_late_minus_early", "ci_low", "ci_high", "p_value", "p_holm", "verdict"]),
        "",
        "## Realised personas",
        "",
        "A persona is realised when its B1 recall interval lies entirely above chance and every pre-specified prediction against P0 is confirmed. A persona with no prediction against P0 is not assessed. Erratum 1, 2026-10-02. The two erratum 2 P5 predictions are excluded from this count.",
        "",
        md_table(realised, ["scope", "persona", "recall", "ci_low", "ci_high", "chance", "recall_above_chance", "n_predictions_vs_p0", "n_confirmed_vs_p0", "realised", "assessment"]),
        "",
        "## Descriptive means",
        "",
        md_table(descriptive, ["condition", "scope", "marker", "mean", "n"]),
        "",
        "## Part D",
        "",
        sensitivity_notes,
        "",
        "## Problems and assumptions",
        "",
        "- The leading-question rule that looks for a sentence starting with \"so you\" is applied after filler stripping. \"so\" is itself a filler, so that clause cannot match. It was not changed.",
        "- A6, the distance to the P0 response, is stored as a feature and is excluded from the B4 classifier because it is computed from the labelled P0 output.",
        "- In B4, `share_open` is median-imputed inside each training fold. The imputer is not tuned.",
        "- Sentences are splits on `.`, `!`, and `?`. `n_questions` counts question marks. `n_words` counts the same tokens used for lexicon matching.",
        "- Stopwords are scikit-learn's English list. Echo words are the remaining tokens in the P1-P5 persona texts, not the shared base instruction.",
        "- A lexicon hit is dropped in the echo-free psychosocial score when the matched word is one of those persona content words. Separate phrases can each add a count when they overlap.",
        "- Accuracy and recall intervals resample dialogues on the fixed out-of-fold predictions. They do not refit the classifier.",
        "- Each bootstrap uses NumPy `default_rng(20261002)` on its own.",
        "- Cosine distance is 1 minus the cosine similarity of L2-normalised MiniLM embeddings.",
        "- Package pins are in the plan: scispaCy 0.5.5 with `en_core_sci_sm` 0.5.4, sentence-transformers 3.4.1, and NumPy 1.26.4. The scispaCy build needed that NumPy version.",
        "- Erratum 2 (2026-10-02) adds P5 versus P0 predictions for lower `has_question` and higher `plan_statement_present`. For Gemini and Claude these are exploratory. They are excluded from the realised count.",
        "- Cross-model generalisation is reported in `persona_study/reports/analysis_report_all_models.md`.",
        "- Confusion matrices are in `persona_study/analysis/results/b_confusion.csv` and the figures under `persona_study/analysis/results/figures/`.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")



def write_combined_report(
    path: Path,
    plan_sha: str,
    prompt_sha: str,
    summaries: list[dict],
    accuracy_all: pd.DataFrame,
    recall_all: pd.DataFrame,
    prediction_all: pd.DataFrame,
    h2_all: pd.DataFrame,
    realised_all: pd.DataFrame,
    cross_accuracy: pd.DataFrame,
    cross_recall: pd.DataFrame,
    plan: dict,
) -> None:
    acc = accuracy_all.loc[accuracy_all["variant"].isin(["B1", "B2", "B3"])].copy()
    recall = recall_all.loc[
        (recall_all["variant"] == "B1") & (recall_all["condition"].isin(["P1", "P2", "P3", "P4", "P5"]))
    ].copy()
    lines = [
        "# All-models measurement report",
        "",
        *recorded_plan_hashes(plan, plan_sha),
        f"Prompt SHA-256: `{prompt_sha}`",
        "",
        "Each model has its own tables under `persona_study/analysis/results/<model>/` and its own report. Erratum 2 adds two P5 versus P0 predictions. They are exploratory for Gemini and Claude, pre-specified for any later model, and excluded from the realised rule.",
        "",
        "## Data",
        "",
    ]
    for item in summaries:
        features = item["features"]
        used = features.loc[features["missing_analysis"] == 0]
        lines.append(
            f"- {item['model']}: {len(features)} rows, missing analysis_text {int(features['missing_analysis'].sum())}, analysed {len(used)}."
        )
    lines.extend([
        "",
        "## B1, B2 and B3 accuracy",
        "",
        md_table(acc, ["model", "variant", "scope", "accuracy", "ci_low", "ci_high", "chance", "n"]),
        "",
        "## B1 recall per persona",
        "",
        md_table(recall, ["model", "scope", "condition", "recall", "ci_low", "ci_high", "chance", "n"]),
        "",
        "## Prediction verdicts",
        "",
        md_table(prediction_all, ["model", "scope", "contrast", "marker", "direction", "specification", "estimate", "ci_low", "ci_high", "verdict"]),
        "",
        "## H2 position tests",
        "",
        md_table(h2_all, ["model", "contrast", "marker", "prediction_direction", "specification", "estimate_late_minus_early", "ci_low", "ci_high", "verdict"]),
        "",
        "## Realised personas",
        "",
        "A persona with no prediction against P0 is not assessed. The two erratum 2 P5 predictions are excluded from the realised count. They are exploratory for Gemini and Claude.",
        "",
        md_table(realised_all, ["model", "scope", "persona", "recall", "ci_low", "ci_high", "n_predictions_vs_p0", "n_confirmed_vs_p0", "realised", "assessment"]),
        "",
        "## Cross-model generalisation",
        "",
        "Each row trains the Part B1 text classifier on every model except one and tests it on the held-out model. Chance is 1/6.",
        "",
    ])
    if "accuracy" in cross_accuracy.columns:
        lines.append(md_table(cross_accuracy, ["held_out_model", "train_models", "scope", "accuracy", "ci_low", "ci_high", "chance", "n"]))
        lines.extend([
            "",
            "Recall on the held-out model:",
            "",
            md_table(cross_recall, ["held_out_model", "scope", "condition", "recall", "ci_low", "ci_high", "n"]),
        ])
    else:
        lines.append("Cross-model generalisation was skipped because fewer than two models were present.")
    lines.extend(["", "## Which models support each hypothesis", ""])
    overall = prediction_all.loc[prediction_all["scope"] == "overall"]
    grouped = overall.groupby(["contrast", "marker", "direction"], sort=False)
    for (contrast, marker, direction), block in grouped:
        lines.append(
            f"- {contrast}, {marker} {direction}: confirmed for {support_phrase(block, 'confirmed')}; "
            f"opposite for {support_phrase(block, 'opposite')}; "
            f"not confirmed for {support_phrase(block, 'other')}."
        )
    lines.extend([
        "",
        "H2 predicts that each paired difference is smaller at Late than at Early. A model supports H2 for a contrast when that Late-minus-Early interval excludes zero in the attenuation direction.",
        "",
    ])
    for (contrast, marker), block in h2_all.groupby(["contrast", "marker"], sort=False):
        lines.append(
            f"- H2 {contrast}, {marker}: confirmed for {support_phrase(block, 'confirmed')}; "
            f"opposite for {support_phrase(block, 'opposite')}; "
            f"not confirmed for {support_phrase(block, 'other')}."
        )
    lines.extend(["", "## Part D", ""])
    for item in summaries:
        lines.append(f"- {item['model']}: {item['sensitivity_notes'].splitlines()[0]}")
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path)
    parser.add_argument(
        "--skip-combined",
        action="store_true",
        help="Write only the per-model report. Do not replace analysis_report_all_models.md or the comparison tables.",
    )
    args = parser.parse_args()
    plan = load_plan(PLAN_PATH)
    plan_sha = sha256_file(PLAN_PATH)
    config_path = PROJECT / "config.yaml" if args.config is None else args.config
    config = load_config(config_path)
    prompt_sha = sha256_file(PROJECT / str(config["prompt_file"]))
    frames, frozen, persona_texts = load_inputs(config)
    if len(frames) != 1:
        print(f"Models configured: {len(frames)}")
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    seed = int(plan["seed"])
    np.random.seed(seed)
    all_features = []
    echo: set[str] = set()
    for model, outputs in frames:
        print(f"features {model}", flush=True)
        features, echo = build_features(model, outputs, frozen, persona_texts, plan, plan_sha)
        # analysis_text was an input column and is not retained
        write_csv(features, PROJECT / "analysis" / f"features_{model}.csv", plan_sha)
        all_features.append(features)
    summaries = []
    text_frames = []
    for (model, outputs), features in zip(frames, all_features):
        result_dir = RESULTS / model
        figure_dir = result_dir / "figures"
        result_dir.mkdir(parents=True, exist_ok=True)
        figure_dir.mkdir(parents=True, exist_ok=True)
        analysed = usable_rows(features)
        analysed_ids = set(zip(analysed["context_id"], analysed["condition"]))
        text_frame = outputs.copy()
        text_frame["model"] = model
        text_frame = text_frame.loc[
            text_frame.apply(lambda row: (row["context_id"], row["condition"]) in analysed_ids, axis=1)
        ].copy()
        text_frame = text_frame.merge(
            analysed[["context_id", "condition", "n_words"] + B4_FEATURES[1:]],
            on=["context_id", "condition"],
            how="left",
        )
        # n_words may have been duplicated. Keep the feature column.
        if "n_words_y" in text_frame.columns:
            text_frame["n_words"] = text_frame["n_words_y"]
        print("classifiers", flush=True)
        prediction_frames = []
        for variant in ["B1", "B2", "B3", "B4", "B5", "B6", "B7"]:
            print(f"  {variant}", flush=True)
            prediction_frames.append(fit_variant(text_frame, variant, echo, plan, seed))
        predictions_oof = pd.concat(prediction_frames, ignore_index=True)
        write_csv(predictions_oof, result_dir / "oof_predictions.csv", plan_sha)
        accuracy, recall, confusion = metric_tables(predictions_oof, plan, seed)
        write_csv(accuracy, result_dir / "b_accuracy.csv", plan_sha)
        write_csv(recall, result_dir / "b_recall.csv", plan_sha)
        write_csv(confusion, result_dir / "b_confusion.csv", plan_sha)
        gee_b1 = fit_b1_gee(predictions_oof, analysed, plan)
        write_csv(gee_b1, result_dir / "b1_gee.csv", plan_sha)
        print("style", flush=True)
        pred_table, h2 = prediction_table(analysed, plan, seed)
        realised = realised_table(recall, pred_table)
        descriptive = descriptive_table(analysed)
        gee_markers = fit_marker_gee(analysed)
        write_csv(pred_table, result_dir / "c_predictions.csv", plan_sha)
        write_csv(h2, result_dir / "c_h2.csv", plan_sha)
        write_csv(realised, result_dir / "c_realised.csv", plan_sha)
        write_csv(descriptive, result_dir / "c_descriptive.csv", plan_sha)
        write_csv(gee_markers, result_dir / "c_gee.csv", plan_sha)
        write_csv(pd.DataFrame({"word": sorted(echo)}), result_dir / "echo_content_words.csv", plan_sha)
        print("sensitivity", flush=True)
        flag_cols = [
            "flag_empty",
            "flag_truncated",
            "flag_patient_turn",
            "flag_multiple_doctor_turns",
            "flag_refusal_or_ai_meta",
        ]
        clean = analysed.loc[analysed[flag_cols].sum(axis=1) == 0].copy()
        clean_ids = set(zip(clean["context_id"], clean["condition"]))
        clean_text = text_frame.loc[
            text_frame.apply(lambda row: (row["context_id"], row["condition"]) in clean_ids, axis=1)
        ].copy()
        b1_clean = fit_variant(clean_text, "B1", echo, plan, seed)
        acc_d, rec_d, conf_d = metric_tables(b1_clean, plan, seed)
        pred_d, h2_d = prediction_table(clean, plan, seed)
        realised_d = realised_table(rec_d, pred_d)
        write_csv(acc_d, result_dir / "d_b1_accuracy.csv", plan_sha)
        write_csv(rec_d, result_dir / "d_b1_recall.csv", plan_sha)
        write_csv(conf_d, result_dir / "d_b1_confusion.csv", plan_sha)
        write_csv(pred_d, result_dir / "d_predictions.csv", plan_sha)
        write_csv(h2_d, result_dir / "d_h2.csv", plan_sha)
        write_csv(realised_d, result_dir / "d_realised.csv", plan_sha)
        pred_change = changed_conclusions(pred_table, pred_d, ["scope", "contrast", "marker"])
        h2_change = changed_conclusions(h2, h2_d, ["contrast", "marker"])
        real_change = realised.merge(
            realised_d[["scope", "persona", "realised"]],
            on=["scope", "persona"],
            suffixes=("_main", "_sensitivity"),
        )
        real_change["changed"] = (
            real_change["realised_main"].fillna(-1) != real_change["realised_sensitivity"].fillna(-1)
        ).astype(int)
        write_csv(pred_change, result_dir / "d_prediction_changes.csv", plan_sha)
        write_csv(h2_change, result_dir / "d_h2_changes.csv", plan_sha)
        write_csv(real_change, result_dir / "d_realised_changes.csv", plan_sha)
        n_pred_changed = int(pred_change["changed"].sum())
        n_h2_changed = int(h2_change["changed"].sum())
        n_real_changed = int(real_change["changed"].sum())
        sensitivity_notes = (
            f"Part D drops {len(analysed) - len(clean)} analysed rows with any format flag, leaving {len(clean)}. "
            f"Prediction verdicts changed in {n_pred_changed} of {len(pred_change)} rows. "
            f"H2 verdicts changed in {n_h2_changed} of {len(h2_change)} rows. "
            f"Realised flags changed in {n_real_changed} of {len(real_change)} rows."
        )
        if n_pred_changed:
            changed_bits = pred_change.loc[pred_change["changed"] == 1, ["scope", "contrast", "marker", "verdict_main", "verdict_sensitivity"]]
            sensitivity_notes += "\n\nChanged prediction verdicts:\n\n" + md_table(
                changed_bits, ["scope", "contrast", "marker", "verdict_main", "verdict_sensitivity"]
            )
        print("figures", flush=True)
        plot_accuracy(accuracy, figure_dir / "accuracy_by_position.png", plan_sha)
        plot_confusion(confusion, figure_dir / "confusion_b1.png", plan_sha, "B1", ["overall", *POSITIONS])
        for variant in ["B2", "B3", "B4", "B5", "B6", "B7"]:
            plot_confusion(confusion, figure_dir / f"confusion_{variant.lower()}.png", plan_sha, variant, ["overall"])
        plot_shifts(pred_table, figure_dir / "marker_shifts.png", plan_sha)
        report_path = PROJECT / "reports" / f"analysis_report_{model}.md"
        write_report(
            report_path,
            model,
            plan_sha,
            prompt_sha,
            features,
            accuracy,
            recall,
            pred_table,
            h2,
            realised,
            descriptive,
            gee_b1,
            sensitivity_notes,
            len(echo),
            plan,
        )
        print(f"report {report_path}")
        print(f"plan_sha256 {plan_sha}")
        print(sensitivity_notes.split(".")[0])
        text_frames.append(
            text_frame.loc[:, ["model", "context_id", "dialogue_id", "position", "condition", "analysis_text"]].copy()
        )
        summaries.append({
            "model": model,
            "features": features,
            "accuracy": accuracy,
            "recall": recall,
            "predictions": pred_table,
            "h2": h2,
            "realised": realised,
            "sensitivity_notes": sensitivity_notes,
        })

    if args.skip_combined:
        print(
            "Skipped the combined report. analysis_report_all_models.md and the comparison tables were not written.",
            flush=True,
        )
        return
    print("cross-model", flush=True)
    cross_accuracy, cross_recall, cross_confusion = cross_model_generalise(text_frames, plan, seed)
    write_csv(cross_accuracy, RESULTS / "cross_model_accuracy.csv", plan_sha)
    write_csv(cross_recall, RESULTS / "cross_model_recall.csv", plan_sha)
    write_csv(cross_confusion, RESULTS / "cross_model_confusion.csv", plan_sha)

    def tagged(frame: pd.DataFrame, model_name: str) -> pd.DataFrame:
        copied = frame.copy()
        copied.insert(0, "model", model_name)
        return copied

    accuracy_all = pd.concat([tagged(item["accuracy"], item["model"]) for item in summaries], ignore_index=True)
    recall_all = pd.concat([tagged(item["recall"], item["model"]) for item in summaries], ignore_index=True)
    prediction_all = pd.concat([tagged(item["predictions"], item["model"]) for item in summaries], ignore_index=True)
    h2_all = pd.concat([tagged(item["h2"], item["model"]) for item in summaries], ignore_index=True)
    realised_all = pd.concat([tagged(item["realised"], item["model"]) for item in summaries], ignore_index=True)
    write_csv(accuracy_all, RESULTS / "comparison_accuracy.csv", plan_sha)
    write_csv(recall_all, RESULTS / "comparison_recall.csv", plan_sha)
    write_csv(prediction_all, RESULTS / "comparison_predictions.csv", plan_sha)
    write_csv(h2_all, RESULTS / "comparison_h2.csv", plan_sha)
    write_csv(realised_all, RESULTS / "comparison_realised.csv", plan_sha)
    write_combined_report(
        PROJECT / "reports" / "analysis_report_all_models.md",
        plan_sha,
        prompt_sha,
        summaries,
        accuracy_all,
        recall_all,
        prediction_all,
        h2_all,
        realised_all,
        cross_accuracy,
        cross_recall,
        plan,
    )
    print("combined report", PROJECT / "reports" / "analysis_report_all_models.md")



if __name__ == "__main__":
    main()
