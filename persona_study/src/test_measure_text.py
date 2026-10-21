"""Unit tests for question form and lexicons. Examples are invented, not taken from the data."""

from __future__ import annotations

import unittest
from pathlib import Path

from measure_text import (
    classify_question,
    lexicon_count,
    load_plan,
    question_features,
    strip_fillers,
    tokenize,
)

PLAN = load_plan(Path(__file__).resolve().parents[1] / "analysis" / "analysis_plan_v1.yaml")


def label_of(text: str) -> str:
    features = question_features(text, PLAN)
    if features["n_open"]:
        return "open"
    if features["n_closed"]:
        return "closed"
    if features["n_other_q"]:
        return "other"
    return "none"


class QuestionTests(unittest.TestCase):
    def test_quantity_before_open_how(self) -> None:
        self.assertEqual(label_of("How many days has the knee been swollen?"), "closed")
        self.assertEqual(label_of("How much water are you drinking?"), "closed")
        self.assertEqual(label_of("How long does the stiffness last?"), "closed")
        self.assertEqual(label_of("How often do you wake at night?"), "closed")

    def test_open_patterns(self) -> None:
        self.assertEqual(label_of("How are you sleeping this week?"), "open")
        self.assertEqual(label_of("What about the swelling in the ankle?"), "open")
        self.assertEqual(label_of("Can you tell me more about the fall?"), "open")
        self.assertEqual(label_of("Why is the pain worse in the morning?"), "open")

    def test_closed_patterns(self) -> None:
        self.assertEqual(label_of("Do you have a cough?"), "closed")
        self.assertEqual(label_of("Are there any allergies in the family?"), "closed")
        self.assertEqual(label_of("When did the dizziness start?"), "closed")

    def test_fillers_then_class(self) -> None:
        self.assertEqual(label_of("OK, so, um, why is it worse at night?"), "open")
        self.assertEqual(label_of("All right, how often do you use the inhaler?"), "closed")
        self.assertEqual(label_of("Yeah?"), "other")

    def test_share_open(self) -> None:
        both = question_features("What is the pain like? Does it spread?", PLAN)
        self.assertEqual(both["share_open"], 0.5)
        only_other = question_features("Yeah?", PLAN)
        self.assertIsNone(only_other["share_open"])

    def test_leading(self) -> None:
        right = question_features("That was yesterday, right?", PLAN)
        self.assertEqual(right["n_leading"], 1)
        tag = question_features("You don't smoke, do you?", PLAN)
        self.assertEqual(tag["n_leading"], 1)
        self.assertEqual(label_of("You don't smoke, do you?"), "other")
        correct = question_features("Is that correct?", PLAN)
        self.assertEqual(correct["n_leading"], 1)
        # "so" is a filler, so the written "so you" test cannot fire.
        so_you = question_features("So you fell on the ice?", PLAN)
        self.assertEqual(so_you["n_leading"], 0)
        self.assertEqual(label_of("So you fell on the ice?"), "other")

    def test_not_a_question(self) -> None:
        told = question_features("Tell me about your sleep.", PLAN)
        self.assertEqual(told["n_open"], 0)
        self.assertEqual(told["n_questions"] if "n_questions" in told else 0, 0)


class LexiconTests(unittest.TestCase):
    def test_emotion_and_life(self) -> None:
        tokens = tokenize("I feel worried and scared about work and money.")
        emotion = lexicon_count(tokens, PLAN["lexicons"]["emotion"])
        life = lexicon_count(tokens, PLAN["lexicons"]["life_context"])
        self.assertEqual(emotion, 3)  # feel, worried, scared
        self.assertEqual(life, 2)  # work, money

    def test_empathy_instruction_plan_invitation_hedge(self) -> None:
        sorry = tokenize("I'm sorry to hear that.")
        self.assertGreaterEqual(lexicon_count(sorry, PLAN["lexicons"]["empathy_phrases"]), 2)
        instruction = tokenize("You need to rest.")
        self.assertEqual(lexicon_count(instruction, PLAN["lexicons"]["instruction"]), 1)
        plan = tokenize("We'll order a blood test.")
        self.assertEqual(lexicon_count(plan, PLAN["lexicons"]["plan_statement"]), 1)
        invite = tokenize("What do you think we should do?")
        self.assertEqual(lexicon_count(invite, PLAN["lexicons"]["invitation"]), 1)
        hedge = tokenize("I think it could be a sprain, maybe.")
        self.assertEqual(lexicon_count(hedge, PLAN["lexicons"]["hedge"]), 3)

    def test_curly_apostrophe_and_prefix_boundary(self) -> None:
        curly = tokenize("I\u2019m sorry.")
        self.assertEqual(lexicon_count(curly, PLAN["lexicons"]["empathy_phrases"]), 1)
        framework = tokenize("The framework is new.")
        self.assertEqual(lexicon_count(framework, PLAN["lexicons"]["life_context"]), 0)

    def test_echo_block_removes_surface_word(self) -> None:
        tokens = tokenize("I feel worried about feelings.")
        full = lexicon_count(tokens, PLAN["lexicons"]["emotion"])
        blocked = lexicon_count(tokens, PLAN["lexicons"]["emotion"], {"feelings"})
        self.assertEqual(full, 3)  # feel, worried, feelings
        self.assertEqual(blocked, 2)

    def test_filler_order(self) -> None:
        tokens = strip_fillers(tokenize("All right, so what is new"), PLAN["fillers"])
        self.assertEqual(tokens[:1], ["what"])
        label = classify_question(tokens, PLAN)
        self.assertEqual(label, "open")


if __name__ == "__main__":
    unittest.main()
