"""Text features for the persona study. Rules come from analysis_plan_v1.yaml."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

TOKEN_RE = re.compile(r"[a-z0-9]+(?:['-][a-z0-9]+)*")
SENTENCE_RE = re.compile(r"[^.!?]*[.!?]|[^.!?]+")
APOSTROPHES = str.maketrans({
    "\u2018": "'",
    "\u2019": "'",
    "\u201b": "'",
    "`": "'",
})


def load_plan(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    return text.translate(APOSTROPHES).lower()


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(normalize(text))


def sentences(text: str) -> list[str]:
    parts = [part.strip() for part in SENTENCE_RE.findall(text) if part.strip()]
    return parts


def _phrase_tokens(phrase: str) -> list[str]:
    return tokenize(phrase)


def strip_fillers(tokens: list[str], fillers: list[str]) -> list[str]:
    phrases = sorted((_phrase_tokens(item) for item in fillers), key=len, reverse=True)
    remaining = list(tokens)
    changed = True
    while changed and remaining:
        changed = False
        for phrase in phrases:
            if phrase and remaining[: len(phrase)] == phrase:
                del remaining[: len(phrase)]
                changed = True
                break
    return remaining


def _starts(tokens: list[str], phrase: str) -> bool:
    wanted = _phrase_tokens(phrase)
    return bool(wanted) and tokens[: len(wanted)] == wanted


def classify_question(tokens: list[str], plan: dict) -> str:
    for phrase in plan["question_closed_quantity"]:
        if _starts(tokens, phrase):
            return "closed"
    for phrase in plan["question_open"]:
        if _starts(tokens, phrase):
            return "open"
    for phrase in plan["question_closed"]:
        if _starts(tokens, phrase):
            return "closed"
    return "other"


def is_leading(sentence: str, stripped_tokens: list[str], plan: dict) -> bool:
    norm = normalize(sentence).strip()
    for ending in plan["leading_endings"]:
        if norm.endswith(ending):
            return True
    if norm.endswith("do you?"):
        earlier = norm[: norm.rfind("do you?")]
        if "don't" in tokenize(earlier):
            return True
    return stripped_tokens[:2] == ["so", "you"]


def question_features(text: str, plan: dict) -> dict[str, float]:
    n_open = n_closed = n_other = n_leading = 0
    for sentence in sentences(text):
        if not normalize(sentence).strip().endswith("?"):
            continue
        body = tokenize(sentence.replace("?", " "))
        stripped = strip_fillers(body, plan["fillers"])
        label = classify_question(stripped, plan)
        if label == "open":
            n_open += 1
        elif label == "closed":
            n_closed += 1
        else:
            n_other += 1
        if is_leading(sentence, stripped, plan):
            n_leading += 1
    denom = n_open + n_closed
    share = (n_open / denom) if denom else None
    return {
        "n_open": n_open,
        "n_closed": n_closed,
        "n_other_q": n_other,
        "share_open": share,
        "n_leading": n_leading,
        "leading_present": int(n_leading > 0),
    }


def _count_phrases(tokens: list[str], phrases: list[str]) -> int:
    total = 0
    for phrase in phrases:
        wanted = _phrase_tokens(phrase)
        if not wanted:
            continue
        width = len(wanted)
        index = 0
        while index <= len(tokens) - width:
            if tokens[index : index + width] == wanted:
                total += 1
                index += width
            else:
                index += 1
    return total


def lexicon_count(tokens: list[str], spec: dict, blocked: set[str] | None = None) -> int:
    blocked = blocked or set()
    prefixes = [item for item in spec.get("prefix", []) if item not in blocked]
    exact = {item for item in spec.get("exact", []) if item not in blocked}
    count = 0
    for token in tokens:
        if token in blocked:
            continue
        if token in exact or any(token.startswith(prefix) for prefix in prefixes):
            count += 1
    count += _count_phrases(tokens, spec.get("phrases", []))
    return count


def per_hundred(count: int, n_words: int) -> float | None:
    if n_words <= 0:
        return None
    return 100.0 * count / n_words


def basic_features(text: str) -> dict[str, float]:
    tokens = tokenize(text)
    n_words = len(tokens)
    n_sent = len(sentences(text)) if text.strip() else 0
    n_questions = text.count("?")
    return {
        "n_words": n_words,
        "n_sentences": n_sent,
        "n_questions": n_questions,
        "has_question": int(n_questions > 0),
    }


def content_words(persona_texts: list[str], stopwords: set[str]) -> set[str]:
    words: set[str] = set()
    for text in persona_texts:
        for token in tokenize(text):
            if token not in stopwords:
                words.add(token)
    return words
