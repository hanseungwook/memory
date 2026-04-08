from __future__ import annotations

from memgen.config import Domain
from memgen.data.base import Problem
from memgen.memory.prompts import Memory

MATH_SYSTEM_PROMPT = (
    "You are an expert mathematician solving competition-level problems. "
    "Show your reasoning step by step, then provide your final answer as a "
    "single integer on the last line in the format: ANSWER: "
)
CODING_SYSTEM_PROMPT = (
    "You are an expert Python programmer. You will be given a question (problem "
    "specification) and will generate a correct Python program that matches the "
    "specification and passes all tests."
)


def format_memory_for_injection(memory: Memory) -> str:
    if not memory.items:
        return ""

    lines = ["Before solving, consider these insights from prior analysis:\n"]
    for i, item in enumerate(memory.items, start=1):
        lines.append(f"  {i}. {item.insight}")
    lines.append("\nApply these insights to the problem below.")

    return "\n".join(lines)


def math_augmented_prompt(problem: Problem, memory: Memory) -> tuple[str, str]:
    system_prompt, user_prompt = get_baseline_prompt_fn(Domain.MATH.value)(problem)
    injected_memory = format_memory_for_injection(memory)
    return system_prompt, f"{injected_memory}\n\n{user_prompt}"


def coding_augmented_prompt(problem: Problem, memory: Memory) -> tuple[str, str]:
    system_prompt, user_prompt = get_baseline_prompt_fn(Domain.CODING.value)(problem)
    injected_memory = format_memory_for_injection(memory)
    return system_prompt, f"{injected_memory}\n\n{user_prompt}"


def get_augmented_prompt_fn(domain: str):
    normalized = _normalize_domain(domain)
    if normalized == Domain.MATH.value:
        return math_augmented_prompt
    if normalized == Domain.CODING.value:
        return coding_augmented_prompt
    raise ValueError(f"Unsupported domain: {domain}")


def get_baseline_prompt_fn(domain: str):
    normalized = _normalize_domain(domain)
    generation_prompts = _load_generation_prompts_module()
    if generation_prompts is not None:
        prompt_fn = _resolve_generation_prompt_fn(generation_prompts, normalized)
        if prompt_fn is not None:
            return prompt_fn

    if normalized == Domain.MATH.value:
        return _fallback_math_prompt
    if normalized == Domain.CODING.value:
        return _fallback_coding_prompt
    raise ValueError(f"Unsupported domain: {domain}")


def _normalize_domain(domain: str) -> str:
    if isinstance(domain, Domain):
        return domain.value
    return str(domain).strip().lower()


def _load_generation_prompts_module():
    try:
        from memgen.generation import prompts as generation_prompts
    except ImportError:
        return None
    return generation_prompts


def _resolve_generation_prompt_fn(generation_prompts, domain: str):
    get_prompt_fn = getattr(generation_prompts, "get_prompt_fn", None)
    if callable(get_prompt_fn):
        try:
            return get_prompt_fn(domain)
        except Exception:
            try:
                return get_prompt_fn(Domain(domain))
            except Exception:
                pass

    fallback_names = {
        Domain.MATH.value: ("math_prompt", "build_math_prompt"),
        Domain.CODING.value: ("coding_prompt", "build_coding_prompt"),
    }
    for name in fallback_names[domain]:
        candidate = getattr(generation_prompts, name, None)
        if callable(candidate):
            return candidate
    return None


def _fallback_math_prompt(problem: Problem) -> tuple[str, str]:
    return MATH_SYSTEM_PROMPT, _format_problem_body(problem)


def _fallback_coding_prompt(problem: Problem) -> tuple[str, str]:
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


def _format_problem_body(problem: Problem) -> str:
    sections = [problem.statement.strip()]

    if problem.starter_code:
        sections.extend(["Starter code:", problem.starter_code.strip()])

    if problem.test_cases:
        test_case_blocks = []
        for index, test_case in enumerate(problem.test_cases, start=1):
            input_text = str(test_case.get("input", "")).strip()
            output_text = str(test_case.get("output", "")).strip()
            test_case_blocks.append(
                f"Test case {index} input:\n{input_text}\n\nExpected output:\n{output_text}"
            )
        sections.extend(["Test cases:", "\n\n".join(test_case_blocks)])

    return "\n\n".join(section for section in sections if section)
