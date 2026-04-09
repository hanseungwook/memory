"""Tests for the dual-path code execution sandbox."""

import json

from memgen.scoring.sandbox import (
    _compare_stdio_output,
    execute_function_based,
    execute_stdin_based,
)


# ---------------------------------------------------------------------------
# Stdin-based execution
# ---------------------------------------------------------------------------

class TestStdinExecution:
    def test_simple_print(self):
        code = 'print("hello")'
        results = execute_stdin_based(code, [""], ["hello"], timeout=10)
        assert len(results) == 1
        assert results[0].passed

    def test_read_input_and_echo(self):
        code = "x = input()\nprint(x)"
        results = execute_stdin_based(code, ["42"], ["42"], timeout=10)
        assert len(results) == 1
        assert results[0].passed

    def test_multiple_test_cases(self):
        code = "n = int(input())\nprint(n * 2)"
        results = execute_stdin_based(
            code,
            ["3", "5", "10"],
            ["6", "10", "20"],
            timeout=10,
        )
        assert len(results) == 3
        assert all(r.passed for r in results)

    def test_wrong_answer(self):
        code = 'print("wrong")'
        results = execute_stdin_based(code, [""], ["right"], timeout=10)
        assert len(results) == 1
        assert not results[0].passed
        assert results[0].error == "Wrong Answer"

    def test_runtime_error(self):
        code = "raise ValueError('boom')"
        results = execute_stdin_based(code, [""], [""], timeout=10)
        assert len(results) == 1
        assert not results[0].passed
        assert "Runtime Error" in (results[0].error or "")

    def test_timeout(self):
        code = "import time\ntime.sleep(30)"
        results = execute_stdin_based(code, [""], [""], timeout=2)
        assert len(results) == 1
        assert not results[0].passed
        assert results[0].error is not None

    def test_if_name_main_stripped(self):
        code = (
            "import sys\n"
            "def solve():\n"
            "    print('ok')\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )
        results = execute_stdin_based(code, [""], ["ok"], timeout=10)
        assert len(results) == 1
        assert results[0].passed

    def test_multiline_output(self):
        code = "print('a')\nprint('b')\nprint('c')"
        results = execute_stdin_based(code, [""], ["a\nb\nc"], timeout=10)
        assert len(results) == 1
        assert results[0].passed

    def test_large_output_is_truncated(self):
        code = "print('x' * 20000)"
        expected = "x" * 20000
        results = execute_stdin_based(
            code,
            [""],
            [expected],
            timeout=10,
            max_output_length=128,
        )
        assert len(results) == 1
        assert results[0].passed
        assert len(results[0].actual) <= 128
        assert results[0].actual.endswith("[truncated]")


# ---------------------------------------------------------------------------
# Function-based execution
# ---------------------------------------------------------------------------

class TestFunctionExecution:
    def test_class_solution(self):
        code = (
            "class Solution:\n"
            "    def twoSum(self, nums, target):\n"
            "        for i in range(len(nums)):\n"
            "            for j in range(i+1, len(nums)):\n"
            "                if nums[i]+nums[j]==target:\n"
            "                    return [i,j]\n"
        )
        # inputs: each line is a JSON arg; output: JSON expected
        results = execute_function_based(
            code,
            func_name="twoSum",
            all_inputs=["[2,7,11,15]\n9"],
            all_outputs=["[0, 1]"],
            timeout=10,
        )
        assert len(results) == 1
        assert results[0].passed

    def test_standalone_function(self):
        code = "def addOne(x):\n    return x + 1\n"
        results = execute_function_based(
            code,
            func_name="addOne",
            all_inputs=["5"],
            all_outputs=["6"],
            timeout=10,
        )
        assert len(results) == 1
        assert results[0].passed

    def test_wrong_answer_function(self):
        code = "def addOne(x):\n    return x + 2\n"
        results = execute_function_based(
            code,
            func_name="addOne",
            all_inputs=["5"],
            all_outputs=["6"],
            timeout=10,
        )
        assert len(results) == 1
        assert not results[0].passed

    def test_missing_function(self):
        code = "def foo():\n    pass\n"
        results = execute_function_based(
            code,
            func_name="bar",
            all_inputs=["1"],
            all_outputs=["1"],
            timeout=10,
        )
        assert len(results) == 1
        assert not results[0].passed
        assert "not found" in (results[0].error or "")

    def test_tuple_coercion(self):
        """Tuples returned by the solution should compare equal to list expectations."""
        code = "def getCoords():\n    return (1, 2)\n"
        results = execute_function_based(
            code,
            func_name="getCoords",
            all_inputs=[""],
            all_outputs=["[1, 2]"],
            timeout=10,
        )
        assert len(results) == 1
        assert results[0].passed

    def test_timeout_function(self):
        code = (
            "def spin():\n"
            "    while True:\n"
            "        pass\n"
        )
        results = execute_function_based(
            code,
            func_name="spin",
            all_inputs=[""],
            all_outputs=["null"],
            timeout=2,
        )
        assert len(results) == 1
        assert not results[0].passed

    def test_large_function_output_is_truncated(self):
        code = "def emit():\n    return 'x' * 20000\n"
        results = execute_function_based(
            code,
            func_name="emit",
            all_inputs=[""],
            all_outputs=[json.dumps("x" * 20000)],
            timeout=10,
            max_output_length=128,
        )
        assert len(results) == 1
        assert results[0].passed
        assert len(results[0].actual) <= 128
        assert results[0].actual.endswith("[truncated]")


# ---------------------------------------------------------------------------
# Float-tolerant comparison
# ---------------------------------------------------------------------------

class TestCompareStdioOutput:
    def test_exact_match(self):
        assert _compare_stdio_output("42", "42")

    def test_whitespace_tolerance(self):
        assert _compare_stdio_output("  42  \n", "42")

    def test_float_decimal_match(self):
        assert _compare_stdio_output("3.14", "3.14")

    def test_float_mismatch(self):
        assert not _compare_stdio_output("3.14", "3.15")

    def test_multiline_decimal(self):
        assert _compare_stdio_output("1.0 2.0\n3.0", "1.0 2.0\n3.0")

    def test_line_count_mismatch(self):
        assert not _compare_stdio_output("1\n2", "1\n2\n3")

    def test_non_numeric_mismatch(self):
        assert not _compare_stdio_output("abc", "def")

    def test_integer_as_decimal(self):
        # "10" and "10" should match through decimal path too
        assert _compare_stdio_output("10", "10")
