"""Prompt templates for generation."""

from memgen.data.base import Problem
from memgen.evaluation.prompts import MATH_SYSTEM_PROMPT


def math_generation_prompt(problem: Problem) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for AIME math problems."""
    user = f"Solve the following AIME problem:\n\n{problem.statement}"
    return MATH_SYSTEM_PROMPT, user


def coding_generation_prompt(problem: Problem) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for competitive programming problems."""
    system = (
        "You are an expert competitive programmer. Write a complete, correct "
        "Python solution. Output ONLY the code, no explanations."
    )
    user = problem.statement
    if problem.starter_code:
        user += f"\n\nStarter code:\n```python\n{problem.starter_code}\n```"
    return system, user


def get_prompt_fn(domain: str):
    """Factory returning the prompt function for the given domain."""
    if domain == "math":
        return math_generation_prompt
    elif domain == "coding":
        return coding_generation_prompt
    else:
        raise ValueError(f"Unknown domain: {domain}")
