"""Dual-path code execution sandbox for LiveCodeBench problems.

Supports:
  - Function-based (call-based) execution for LeetCode-style problems
  - Stdin-based execution for Codeforces/AtCoder-style problems

Adapted from the official LiveCodeBench evaluation engine:
  https://github.com/LiveCodeBench/LiveCodeBench
  (Apache 2.0 License)
"""

import ast
import faulthandler
import json
import multiprocessing
import os
import platform
import signal
import sys
from dataclasses import dataclass
from decimal import Decimal
from io import StringIO
from types import ModuleType
from unittest.mock import mock_open, patch

# Large import block prepended to submitted code so common libraries are available.
IMPORT_STRING = (
    "from string import *\nfrom re import *\nfrom datetime import *\n"
    "from collections import *\nfrom heapq import *\nfrom bisect import *\n"
    "from copy import *\nfrom math import *\nfrom random import *\n"
    "from statistics import *\nfrom itertools import *\nfrom functools import *\n"
    "from operator import *\nfrom io import *\nfrom sys import *\n"
    "from json import *\nfrom builtins import *\nfrom typing import *\n"
    "import string\nimport re\nimport datetime\nimport collections\n"
    "import heapq\nimport bisect\nimport copy\nimport math\nimport random\n"
    "import statistics\nimport itertools\nimport functools\nimport operator\n"
    "import io\nimport sys\nimport json\n"
    "sys.setrecursionlimit(50000)\n"
)


@dataclass
class ExecutionResult:
    passed: bool
    actual: str
    error: str | None = None


_TRUNCATION_SUFFIX = "...[truncated]"


def _truncate_text(value: str, max_length: int) -> str:
    if max_length <= 0 or len(value) <= max_length:
        return value
    if max_length <= len(_TRUNCATION_SUFFIX):
        return value[:max_length]
    return value[: max_length - len(_TRUNCATION_SUFFIX)] + _TRUNCATION_SUFFIX


# ---------------------------------------------------------------------------
# Timeout machinery
# ---------------------------------------------------------------------------

class TimeoutException(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TimeoutException("Execution timed out")


# ---------------------------------------------------------------------------
# Reliability guard — disable dangerous builtins/modules
# ---------------------------------------------------------------------------

def reliability_guard(maximum_memory_bytes: int | None = None) -> None:
    """Disable destructive OS/subprocess functions before running untrusted code.

    WARNING: This is NOT a security sandbox.  It reduces accidental damage but
    does not protect against determined adversaries.
    """
    if maximum_memory_bytes is not None:
        import resource
        resource.setrlimit(resource.RLIMIT_AS, (maximum_memory_bytes, maximum_memory_bytes))
        resource.setrlimit(resource.RLIMIT_DATA, (maximum_memory_bytes, maximum_memory_bytes))
        if platform.uname().system != "Darwin":
            resource.setrlimit(resource.RLIMIT_STACK, (maximum_memory_bytes, maximum_memory_bytes))

    faulthandler.disable()

    import builtins
    builtins.quit = None  # type: ignore[assignment]

    os.environ["OMP_NUM_THREADS"] = "1"

    for attr in (
        "kill", "system", "putenv", "remove", "removedirs", "rmdir", "fchdir",
        "setuid", "fork", "forkpty", "killpg", "rename", "renames", "truncate",
        "replace", "unlink", "fchmod", "fchown", "chmod", "chown", "chroot",
        "lchflags", "lchmod", "lchown", "getcwd", "chdir",
    ):
        if hasattr(os, attr):
            setattr(os, attr, None)

    import shutil
    shutil.rmtree = None  # type: ignore[assignment]
    shutil.move = None  # type: ignore[assignment]
    shutil.chown = None  # type: ignore[assignment]

    import subprocess
    subprocess.Popen = None  # type: ignore[assignment]

    if isinstance(__builtins__, dict):
        __builtins__["help"] = None
    else:
        __builtins__.help = None  # type: ignore[union-attr]

    sys.modules["ipdb"] = None  # type: ignore[assignment]
    sys.modules["joblib"] = None  # type: ignore[assignment]
    sys.modules["resource"] = None  # type: ignore[assignment]
    sys.modules["psutil"] = None  # type: ignore[assignment]
    sys.modules["tkinter"] = None  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Stdout capture helper
# ---------------------------------------------------------------------------

class Capturing(list):
    """Context manager that captures everything written to sys.stdout."""

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        self._stringio.close = lambda: None  # type: ignore[method-assign]
        return self

    def __exit__(self, *args):
        self.append(self._stringio.getvalue())
        del self._stringio
        sys.stdout = self._stdout


# ---------------------------------------------------------------------------
# Mock stdin with buffer support (for binary reads)
# ---------------------------------------------------------------------------

class MockStdinWithBuffer:
    def __init__(self, inputs: str):
        self.inputs = inputs
        self._stringio = StringIO(inputs)
        self.buffer = _MockBuffer(inputs)

    def read(self, *args):
        return self.inputs

    def readline(self, *args):
        return self._stringio.readline(*args)

    def readlines(self, *args):
        return self.inputs.split("\n")

    def __getattr__(self, name):
        return getattr(self._stringio, name)


class _MockBuffer:
    def __init__(self, inputs: str):
        self.inputs = inputs.encode("utf-8")

    def read(self, *args):
        return self.inputs

    def readline(self, *args):
        return self.inputs.split(b"\n")[0] + b"\n"


# ---------------------------------------------------------------------------
# AST helpers for stdin-based execution
# ---------------------------------------------------------------------------

def _clean_if_name(code: str) -> str:
    """Strip ``if __name__ == '__main__':`` guard, inlining its body."""
    try:
        tree = ast.parse(code)
        last = tree.body[-1]
        if isinstance(last, ast.If) and ast.unparse(last.test).strip() == "__name__ == '__main__'":
            code = ast.unparse(tree.body[:-1]) + "\n" + ast.unparse(last.body)
    except Exception:
        pass
    return code


def _make_function(code: str) -> str:
    """Wrap non-import statements into ``wrapped_function()`` so we can call it with mocked stdin."""
    try:
        tree = ast.parse(code)
        imports = []
        body = []
        for stmt in tree.body:
            if isinstance(stmt, (ast.Import, ast.ImportFrom)):
                imports.append(stmt)
            else:
                body.append(stmt)
        func = ast.FunctionDef(
            name="wrapped_function",
            args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]),
            body=body,
            decorator_list=[],
            lineno=-1,
        )
        return IMPORT_STRING + "\n" + ast.unparse(imports) + "\n" + ast.unparse(func)
    except Exception:
        return code


# ---------------------------------------------------------------------------
# Code compilation
# ---------------------------------------------------------------------------

def _compile_code(code: str, timeout: int) -> ModuleType | None:
    signal.alarm(timeout)
    try:
        mod = ModuleType("tmp_sol", "")
        exec(code, mod.__dict__)  # noqa: S102
        if "class Solution" in code:
            return mod.Solution()  # type: ignore[return-value]
        return mod
    finally:
        signal.alarm(0)


# ---------------------------------------------------------------------------
# Call stdin-wrapped method with mocked IO
# ---------------------------------------------------------------------------

def _call_method(method, inputs: str):
    if isinstance(inputs, list):
        inputs = "\n".join(inputs)
    inputs_line_iterator = iter(inputs.split("\n"))
    mock_stdin = MockStdinWithBuffer(inputs)

    @patch("builtins.open", mock_open(read_data=inputs))
    @patch("sys.stdin", mock_stdin)
    @patch("sys.stdin.readline", lambda *args: next(inputs_line_iterator))
    @patch("sys.stdin.readlines", lambda *args: inputs.split("\n"))
    @patch("sys.stdin.read", lambda *args: inputs)
    def _inner(fn):
        try:
            return fn()
        except SystemExit:
            pass
    return _inner(method)


# ---------------------------------------------------------------------------
# Decimal-based line comparison (float tolerance)
# ---------------------------------------------------------------------------

def _convert_line_to_decimals(line: str) -> tuple[bool, list[Decimal]]:
    try:
        return True, [Decimal(e) for e in line.split()]
    except Exception:
        return False, []


def _get_stripped_lines(val: str) -> list[str]:
    return [l.strip() for l in val.strip().split("\n")]


def _compare_stdio_output(actual: str, expected: str) -> bool:
    """Compare stdout output with Decimal-based float tolerance, line by line."""
    pred_lines = _get_stripped_lines(actual)
    exp_lines = _get_stripped_lines(expected)
    if len(pred_lines) != len(exp_lines):
        return False
    for p, e in zip(pred_lines, exp_lines):
        if p == e:
            continue
        ok_p, dec_p = _convert_line_to_decimals(p)
        ok_e, dec_e = _convert_line_to_decimals(e)
        if not ok_p or not ok_e:
            return False
        if dec_p != dec_e:
            return False
    return True


# ---------------------------------------------------------------------------
# Worker functions (run inside multiprocessing.Process)
# ---------------------------------------------------------------------------

def _worker_function_based(
    code: str,
    func_name: str,
    all_inputs: list[str],
    all_outputs: list[str],
    timeout: int,
    max_output_length: int,
    result_conn,
) -> None:
    """Run call-based grading inside a child process."""
    signal.signal(signal.SIGALRM, _timeout_handler)
    reliability_guard()

    code = IMPORT_STRING + "\n\n" + code
    try:
        compiled = _compile_code(code, timeout)
    except Exception as exc:
        result_conn.send([
            ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text(f"Compilation error: {exc}", max_output_length),
            )
            for _ in all_inputs
        ])
        result_conn.close()
        return

    if compiled is None:
        result_conn.send([
            ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text("Compilation returned None", max_output_length),
            )
            for _ in all_inputs
        ])
        result_conn.close()
        return

    method = getattr(compiled, func_name, None)
    if method is None:
        result_conn.send([
            ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text(f"Function '{func_name}' not found", max_output_length),
            )
            for _ in all_inputs
        ])
        result_conn.close()
        return

    parsed_inputs = [
        [json.loads(line) for line in inp.split("\n") if line.strip()]
        for inp in all_inputs
    ]
    parsed_outputs = [json.loads(out) for out in all_outputs]

    results: list[ExecutionResult] = []
    for args, expected in zip(parsed_inputs, parsed_outputs):
        signal.alarm(timeout)
        faulthandler.enable()
        try:
            prediction = method(*args)
            signal.alarm(0)
            if isinstance(prediction, tuple):
                prediction = list(prediction)
            ok = prediction == expected
            results.append(
                ExecutionResult(
                    passed=ok,
                    actual=_truncate_text(repr(prediction), max_output_length),
                    error=None if ok else _truncate_text("Wrong Answer", max_output_length),
                )
            )
        except TimeoutException:
            results.append(
                ExecutionResult(
                    passed=False,
                    actual="",
                    error=_truncate_text("Time Limit Exceeded", max_output_length),
                )
            )
            break
        except Exception as exc:
            signal.alarm(0)
            results.append(
                ExecutionResult(
                    passed=False,
                    actual="",
                    error=_truncate_text(f"Runtime Error: {exc}", max_output_length),
                )
            )
            break
        finally:
            signal.alarm(0)
            faulthandler.disable()

    # Pad remaining as not-run if we broke early
    while len(results) < len(all_inputs):
        results.append(
            ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text("Skipped (earlier failure)", max_output_length),
            )
        )

    result_conn.send(results)
    result_conn.close()


def _worker_stdin_based(
    code: str,
    all_inputs: list[str],
    all_outputs: list[str],
    timeout: int,
    max_output_length: int,
    result_conn,
) -> None:
    """Run stdin-based grading inside a child process."""
    signal.signal(signal.SIGALRM, _timeout_handler)
    reliability_guard()

    code = _clean_if_name(code)
    code = _make_function(code)

    try:
        compiled = _compile_code(code, timeout)
    except Exception as exc:
        result_conn.send([
            ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text(f"Compilation error: {exc}", max_output_length),
            )
            for _ in all_inputs
        ])
        result_conn.close()
        return

    if compiled is None:
        result_conn.send([
            ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text("Compilation returned None", max_output_length),
            )
            for _ in all_inputs
        ])
        result_conn.close()
        return

    method = getattr(compiled, "wrapped_function", None)
    if method is None:
        result_conn.send([
            ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text("wrapped_function not found", max_output_length),
            )
            for _ in all_inputs
        ])
        result_conn.close()
        return

    results: list[ExecutionResult] = []
    for inp, expected in zip(all_inputs, all_outputs):
        signal.alarm(timeout)
        faulthandler.enable()
        with Capturing() as captured:
            try:
                _call_method(method, inp)
                signal.alarm(0)
            except TimeoutException:
                signal.alarm(0)
                results.append(
                    ExecutionResult(
                        passed=False,
                        actual="",
                        error=_truncate_text("Time Limit Exceeded", max_output_length),
                    )
                )
                break
            except Exception as exc:
                signal.alarm(0)
                results.append(
                    ExecutionResult(
                        passed=False,
                        actual="",
                        error=_truncate_text(f"Runtime Error: {exc}", max_output_length),
                    )
                )
                break
            finally:
                signal.alarm(0)
                faulthandler.disable()

        actual = captured[0] if captured else ""
        ok = _compare_stdio_output(actual, expected)
        results.append(
            ExecutionResult(
                passed=ok,
                actual=_truncate_text(actual.strip(), max_output_length),
                error=None if ok else _truncate_text("Wrong Answer", max_output_length),
            )
        )

    while len(results) < len(all_inputs):
        results.append(
            ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text("Skipped (earlier failure)", max_output_length),
            )
        )

    result_conn.send(results)
    result_conn.close()


def _worker_assertion_program(
    code: str,
    test_program: str,
    timeout: int,
    max_output_length: int,
    result_conn,
) -> None:
    """Run a Python assertion-based test program inside a child process."""
    signal.signal(signal.SIGALRM, _timeout_handler)
    reliability_guard()

    program = IMPORT_STRING + "\n\n" + code + "\n\n" + test_program

    signal.alarm(timeout)
    faulthandler.enable()
    with Capturing() as captured:
        try:
            _compile_code(program, timeout)
            signal.alarm(0)
            result = ExecutionResult(
                passed=True,
                actual=_truncate_text((captured[0] if captured else "").strip(), max_output_length),
                error=None,
            )
        except TimeoutException:
            signal.alarm(0)
            result = ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text("Time Limit Exceeded", max_output_length),
            )
        except AssertionError as exc:
            signal.alarm(0)
            result = ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text(f"Assertion Error: {exc}", max_output_length),
            )
        except Exception as exc:
            signal.alarm(0)
            result = ExecutionResult(
                passed=False,
                actual="",
                error=_truncate_text(f"Runtime Error: {exc}", max_output_length),
            )
        finally:
            signal.alarm(0)
            faulthandler.disable()

    result_conn.send(result)
    result_conn.close()


def _get_multiprocessing_context():
    """Use a thread-safe process start method on Python 3.12+."""
    available = set(multiprocessing.get_all_start_methods())
    for method in ("forkserver", "spawn"):
        if method in available:
            return multiprocessing.get_context(method)
    return multiprocessing.get_context()


def _run_with_result_conn(
    worker,
    worker_args: tuple,
    wait_timeout: int,
    fallback_count: int,
) -> list[ExecutionResult]:
    ctx = _get_multiprocessing_context()
    recv_conn, send_conn = ctx.Pipe(duplex=False)
    proc = ctx.Process(target=worker, args=(*worker_args, send_conn))
    proc.start()
    send_conn.close()

    try:
        if recv_conn.poll(wait_timeout):
            try:
                results = recv_conn.recv()
            except EOFError:
                results = [
                    ExecutionResult(passed=False, actual="", error="No results returned")
                    for _ in range(fallback_count)
                ]
        else:
            results = [
                ExecutionResult(passed=False, actual="", error="Process timed out")
                for _ in range(fallback_count)
            ]
    finally:
        recv_conn.close()
        proc.join(timeout=0.5)
        if proc.is_alive():
            proc.kill()
            proc.join()

    return results


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def execute_function_based(
    code: str,
    func_name: str,
    all_inputs: list[str],
    all_outputs: list[str],
    timeout: int = 30,
    max_output_length: int = 10000,
) -> list[ExecutionResult]:
    """Execute function-based (LeetCode-style) code against test cases.

    Each input is a newline-separated string of JSON-encoded arguments.
    Each output is a JSON-encoded expected return value.
    Returns one ``ExecutionResult`` per test case.
    """
    return _run_with_result_conn(
        _worker_function_based,
        (
            code,
            func_name,
            all_inputs,
            all_outputs,
            timeout,
            max_output_length,
        ),
        wait_timeout=(timeout + 1) * len(all_inputs) + 5,
        fallback_count=len(all_inputs),
    )


def execute_stdin_based(
    code: str,
    all_inputs: list[str],
    all_outputs: list[str],
    timeout: int = 30,
    max_output_length: int = 10000,
) -> list[ExecutionResult]:
    """Execute stdin-based (Codeforces/AtCoder-style) code against test cases.

    Each input is a raw string piped to stdin.
    Each output is the expected stdout string.
    Returns one ``ExecutionResult`` per test case.
    """
    return _run_with_result_conn(
        _worker_stdin_based,
        (
            code,
            all_inputs,
            all_outputs,
            timeout,
            max_output_length,
        ),
        wait_timeout=(timeout + 1) * len(all_inputs) + 5,
        fallback_count=len(all_inputs),
    )


def execute_python_assertions(
    code: str,
    test_program: str,
    timeout: int = 30,
    max_output_length: int = 10000,
) -> ExecutionResult:
    """Execute Python code plus an assertion-based test harness."""
    results = _run_with_result_conn(
        _worker_assertion_program,
        (
            code,
            test_program,
            timeout,
            max_output_length,
        ),
        wait_timeout=timeout + 5,
        fallback_count=1,
    )
    if isinstance(results, list):
        return results[0]
    return results
