"""Subprocess sandbox for executing code."""

import os
import subprocess
import tempfile


def execute_code(
    code: str, stdin_input: str = "", timeout: int = 30
) -> tuple[str, str, int]:
    """Execute Python code in a subprocess.

    Returns (stdout, stderr, returncode).
    On timeout, returns ("", "TimeoutExpired", -1).
    """
    fd, path = tempfile.mkstemp(suffix=".py")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(code)

        result = subprocess.run(
            ["python", path],
            input=stdin_input,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "TimeoutExpired", -1
    finally:
        os.unlink(path)
