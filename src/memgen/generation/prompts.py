"""Prompt templates for generation."""

from memgen.data.base import Problem


def math_generation_prompt(problem: Problem) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for AIME math problems."""
    system = (
        "You are an expert mathematician solving competition-level problems. "
        "Show your reasoning step by step, then provide your final answer "
        "as a single integer on the last line in the format: ANSWER: "
    )
    user = f"Solve the following AIME problem:\n\n{problem.statement}"
    return system, user


def coding_generation_prompt(problem: Problem) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for competitive programming problems."""
    system = (
        "You are an expert Python programmer. You will be given a question (problem "
        "specification) and will generate a correct Python program that matches the "
        "specification and passes all tests."
    )

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
        f"### Format:\n{format_instruction}\n{code_block}\n\n"
        f"### Answer:\n(using the provided format with backticks)\n\n[BEGIN]"
    )
    return system, user


def get_prompt_fn(domain: str):
    """Factory returning the prompt function for the given domain."""
    if domain == "math":
        return math_generation_prompt
    elif domain == "coding":
        return coding_generation_prompt
    else:
        raise ValueError(f"Unknown domain: {domain}")
