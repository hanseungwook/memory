"""Tests for CodingScorer routing between function-based and stdin-based execution."""

import pytest

from memgen.config import ScoringConfig
from memgen.data.base import Problem
from memgen.scoring.coding_scorer import CodingScorer, _is_function_based


class TestIsFunctionBased:
    def test_function_based_with_func_name_and_starter(self):
        p = Problem(
            id="1",
            domain="coding",
            statement="",
            metadata={"func_name": "twoSum"},
            starter_code="class Solution:",
        )
        assert _is_function_based(p)

    def test_stdin_based_no_func_name(self):
        p = Problem(id="2", domain="coding", statement="", metadata={})
        assert not _is_function_based(p)

    def test_stdin_based_func_name_but_no_starter(self):
        p = Problem(
            id="3",
            domain="coding",
            statement="",
            metadata={"func_name": "solve"},
            starter_code=None,
        )
        assert _is_function_based(p)


class TestCodingScorerStdin:
    def setup_method(self):
        self.scorer = CodingScorer(ScoringConfig(timeout_seconds=10))

    def test_score_all_pass(self):
        problem = Problem(
            id="p1",
            domain="coding",
            statement="Print input doubled",
            test_cases=[
                {"input": "3", "output": "6"},
                {"input": "5", "output": "10"},
            ],
        )
        gen = "```python\nn = int(input())\nprint(n * 2)\n```"
        result = self.scorer.score(problem, gen, 0)
        assert result.score == 1.0
        assert result.tier == "full"

    def test_score_partial(self):
        problem = Problem(
            id="p2",
            domain="coding",
            statement="",
            test_cases=[
                {"input": "3", "output": "6"},
                {"input": "5", "output": "10"},
            ],
        )
        # Always prints 6 — passes first case, fails second
        gen = '```python\nprint("6")\n```'
        result = self.scorer.score(problem, gen, 0)
        assert result.score == 0.5
        assert result.tier == "partial"

    def test_score_no_test_cases(self):
        problem = Problem(id="p3", domain="coding", statement="", test_cases=[])
        result = self.scorer.score(problem, "print(1)", 0)
        assert result.score == 0.0
        assert result.tier == "fail"


class TestCodingScorerFunctionBased:
    def setup_method(self):
        self.scorer = CodingScorer(ScoringConfig(timeout_seconds=10))

    def test_score_function_based(self):
        problem = Problem(
            id="lc1",
            domain="coding",
            statement="Return x+1",
            test_cases=[
                {"input": "5", "output": "6"},
                {"input": "0", "output": "1"},
            ],
            starter_code="class Solution:\n    def addOne(self, x: int) -> int:",
            metadata={"func_name": "addOne"},
        )
        gen = (
            "```python\n"
            "class Solution:\n"
            "    def addOne(self, x: int) -> int:\n"
            "        return x + 1\n"
            "```"
        )
        result = self.scorer.score(problem, gen, 0)
        assert result.score == 1.0
        assert result.tier == "full"


class TestExtractCode:
    def setup_method(self):
        self.scorer = CodingScorer(ScoringConfig())

    def test_python_fence(self):
        text = "Here is the code:\n```python\nprint(1)\n```"
        assert self.scorer._extract_code(text) == "print(1)"

    def test_bare_fence(self):
        text = "```\nprint(2)\n```"
        assert self.scorer._extract_code(text) == "print(2)"

    def test_raw_text(self):
        assert self.scorer._extract_code("print(3)") == ""
