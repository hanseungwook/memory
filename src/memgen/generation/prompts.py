"""Prompt templates for generation."""

from memgen.data.base import Problem
from memgen.evaluation.prompts import (
    CODING_SYSTEM_PROMPT,
    LEGACY_MATH_SYSTEM_PROMPT,
    reasoning_system_prompt,
)

MATH_SYSTEM_PROMPT = LEGACY_MATH_SYSTEM_PROMPT


def math_generation_prompt(problem: Problem) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for math problems."""
    if problem.metadata.get("data_source"):
        return reasoning_system_prompt("math"), problem.statement

    user = f"Solve the following AIME problem:\n\n{problem.statement}"
    return LEGACY_MATH_SYSTEM_PROMPT, user


def coding_generation_prompt(problem: Problem) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for competitive programming problems."""
    if problem.starter_code:
        format_instruction = (
            "You will use the following starter code to write the solution to the problem "
            "and enclose your code within delimiters."
        )
        code_block = f"```python\n{problem.starter_code}\n```"
    else:
        format_instruction = (
            "Read the inputs from stdin solve the problem and write the answer to stdout "
            "(do not directly test on the sample inputs). Enclose your code within delimiters "
            "as follows. Ensure that when the python program runs, it reads the inputs, runs "
            "the algorithm and writes output to STDOUT."
        )
        code_block = "```python\n# YOUR CODE HERE\n```"

    user = (
        f"### Question:\n{problem.statement}\n\n"
        f"### Format: {format_instruction}\n{code_block}\n\n"
        f"### Answer: (use the provided format with backticks)\n"
    )
    return CODING_SYSTEM_PROMPT, user


def science_generation_prompt(problem: Problem) -> tuple[str, str]:
    return reasoning_system_prompt("science"), problem.statement


def logic_generation_prompt(problem: Problem) -> tuple[str, str]:
    return reasoning_system_prompt("logic"), problem.statement


def simulation_generation_prompt(problem: Problem) -> tuple[str, str]:
    return reasoning_system_prompt("simulation"), problem.statement


def table_generation_prompt(problem: Problem) -> tuple[str, str]:
    return reasoning_system_prompt("table"), problem.statement


def get_prompt_fn(domain: str):
    """Factory returning the prompt function for the given domain."""
    normalized = str(domain).strip().lower()
    if normalized == "math":
        return math_generation_prompt
    if normalized == "coding":
        return coding_generation_prompt
    if normalized == "science":
        return science_generation_prompt
    if normalized == "logic":
        return logic_generation_prompt
    if normalized == "simulation":
        return simulation_generation_prompt
    if normalized in {"table", "tabular"}:
        return table_generation_prompt
    raise ValueError(f"Unknown domain: {domain}")
