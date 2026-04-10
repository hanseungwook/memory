import pytest

from memgen.data.base import Problem
from memgen.evaluation.prompts import MATH_SYSTEM_PROMPT
from memgen.generation.prompts import (
    MATH_SYSTEM_PROMPT as GENERATION_MATH_SYSTEM_PROMPT,
    math_generation_prompt,
)
from memgen.scoring.math_scorer import MathScorer


def make_problem(answer: str = "42") -> Problem:
    return Problem(id="aime-test", domain="math", statement="Compute 6*7.", answer=answer)


def score_generation(generation: str):
    scorer = MathScorer()
    return scorer.score(make_problem(), generation, index=0)


def test_math_generation_prompt_clarifies_response_shape():
    system_prompt, _ = math_generation_prompt(make_problem())

    assert "ANSWER: {answer}" in system_prompt
    assert "step by step" in system_prompt
    assert "ANSWER: 42" in system_prompt
    assert system_prompt == MATH_SYSTEM_PROMPT


def test_math_system_prompt_has_single_canonical_definition():
    assert GENERATION_MATH_SYSTEM_PROMPT is MATH_SYSTEM_PROMPT


def test_scores_plain_integer_answer_line_correct():
    result = score_generation("Reasoning\nANSWER: 42")

    assert result.score == 1.0
    assert result.details["extracted"] == "42"
    assert result.details["reason"] == "correct"


def test_scores_boxed_integer_answer_line_correct():
    result = score_generation("Reasoning\nANSWER: \\boxed{42}")

    assert result.score == 1.0
    assert result.details["extracted"] == "42"
    assert result.details["reason"] == "correct"


def test_scores_expression_answer_line_correct():
    result_fraction = score_generation("Reasoning\nANSWER: 42/1")
    result_product = score_generation("Reasoning\nANSWER: 6*7")

    assert result_fraction.score == 1.0
    assert result_fraction.details["extracted"] == "42"
    assert result_product.score == 1.0
    assert result_product.details["extracted"] == "42"


@pytest.mark.parametrize(
    ("fragment", "expected_reason"),
    [
        ("The answer is 42", "invalid_answer_fragment"),
        ("42 inches", "invalid_answer_fragment"),
        ("43 and 42", "invalid_answer_fragment"),
        (r"6 \\cdot 7", "invalid_answer_fragment"),
    ],
)
def test_rejects_overly_permissive_answer_fragments(
    fragment: str, expected_reason: str
):
    result = score_generation(f"Reasoning\nANSWER: {fragment}")

    assert result.score == 0.0
    assert result.details["reason"] == expected_reason
    assert result.details["extracted"] is None


def test_missing_answer_line_is_incorrect_even_with_correct_integer_elsewhere():
    result = score_generation("The result is 42.\nTherefore the answer is 42.")

    assert result.score == 0.0
    assert result.details["reason"] == "missing_answer_line"
    assert result.details["extracted"] is None


def test_percentage_answer_is_incorrect():
    result = score_generation("Reasoning\nANSWER: 42%")

    assert result.score == 0.0
    assert result.details["reason"] == "percentage_not_allowed"
    assert result.details["extracted"] is None


def test_non_integer_answers_are_incorrect():
    rational = score_generation("Reasoning\nANSWER: 2/3")
    decimal = score_generation("Reasoning\nANSWER: 42.5")

    assert rational.score == 0.0
    assert rational.details["reason"] == "non_integer"
    assert decimal.score == 0.0
    assert decimal.details["reason"] == "non_integer"


def test_leading_zero_answer_normalizes_to_correct_integer():
    result = score_generation("Reasoning\nANSWER: 042")

    assert result.score == 1.0
    assert result.details["extracted"] == "42"
    assert result.details["reason"] == "correct"


def test_scans_upward_for_last_answer_line_when_final_line_is_not_answer():
    result = score_generation("Reasoning\nANSWER: 42\nDone.")

    assert result.score == 1.0
    assert result.details["answer_line"] == "ANSWER: 42"
    assert result.details["reason"] == "correct"
