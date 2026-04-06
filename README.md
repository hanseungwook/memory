# Memory from Generations

Experiment pipeline for creating generalizable problem-solving memories from contrastive analysis of LLM generations.

**Core idea:** Given a problem, generate K solutions with an LLM, score them, group by correctness, then create *memories* — generalizable insights extracted by comparing what successful vs unsuccessful attempts did differently. Then verify whether injecting these memories improves performance on the same tasks.

## Pipeline

```
Load Data → Generate (K=16) → Score → Create Memories → Evaluate (baseline vs augmented)
```

| Stage | What it does |
|-------|-------------|
| **Generate** | Produce K=16 solutions per problem using gpt-5-mini |
| **Score** | Math: binary exact-match (AIME answers are integers). Coding: tiered (fail/partial/full) via subprocess execution against test cases |
| **Memory** | Group solutions by score tier, send correct vs incorrect groups to gpt-5-mini with a contrastive prompt, extract multiple generalizable memory items |
| **Evaluate** | For each problem, generate 16 baseline solutions (no memory) and 16 augmented solutions (with memory injected), compare averaged pass@1 |

Each stage writes JSONL to `results/`, enabling crash-safe resume at per-problem granularity.

## Setup

```bash
pip install -e ".[dev]"
```

Set your OpenAI API key in `.env`:

```
OPENAI_API_KEY=sk-...
```

## Usage

### Full pipeline

```bash
# Math (AIME)
memgen run -c config/math_aime.yaml

# Coding (LiveCodeBench)
memgen run -c config/coding_lcb.yaml
```

### Quick test (limit problems)

```bash
memgen run -c config/math_aime.yaml --max-problems 3
```

### Run individual stages

```bash
memgen run -c config/math_aime.yaml --stage generate
memgen run -c config/math_aime.yaml --stage score
memgen run -c config/math_aime.yaml --stage memory
memgen run -c config/math_aime.yaml --stage evaluate
```

### View results

```bash
memgen report -c config/math_aime.yaml
```

## Datasets

| Domain | Dataset | Split | Problems |
|--------|---------|-------|----------|
| Math | `gneubig/aime-1983-2024` | train | ~933 AIME problems (1983-2024) |
| Coding | `hanseungwook/code_generation_lite` | train | 880 problems (LeetCode, Codeforces) |

## Configuration

Config files are in `config/`. The domain-specific YAML (`math_aime.yaml`, `coding_lcb.yaml`) is merged with `default.yaml` defaults.

Key parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `generation.model` | `gpt-5-mini` | Model for solution generation |
| `generation.k` | `16` | Number of generations per problem |
| `generation.temperature` | `0.7` | Sampling temperature for diversity |
| `memory.model` | `gpt-5-mini` | Model for memory creation |
| `memory.temperature` | `0.3` | Lower temperature for analytical task |
| `evaluation.k` | `16` | Number of generations for pass@1 averaging |
| `scoring.timeout_seconds` | `30` | Timeout per code execution |
| `resume` | `true` | Skip already-processed problems on restart |

## How memory creation works

For each problem, after generating and scoring K=16 solutions:

1. **Group** solutions by score tier (correct/incorrect for math, full/partial/fail for coding)
2. **Contrastive prompt** sends up to 5 solutions per tier to gpt-5-mini, asking it to:
   - First reason about *why* certain attempts succeeded and others failed (`<reasoning>` tag)
   - Then extract multiple independent, generalizable memory items (`<memory>` tags)
3. Each memory item is a self-contained problem-solving principle — no problem-specific details, only transferable techniques

**Key constraint:** Memories must be generalizable and transferable across different problems. The prompt reinforces this in the system message, guidelines, instructions, and response format.

### Memory creation prompt structure

```
System: Extract generalizable, transferable insights from comparing
        successful and unsuccessful solution attempts.

User:
  ## Guidelines
  [Extract insights that are GENERALIZABLE and TRANSFERABLE]

  ## Important notes
  [Think first, extract multiple items, no problem-specific details]

  <problem>...</problem>
  <solution_attempts>
    <tier name="correct">
      <attempt>...</attempt>
    </tier>
    <tier name="incorrect">
      <attempt>...</attempt>
    </tier>
  </solution_attempts>

  ## Response format
  <reasoning>Why did some attempts succeed and others fail?</reasoning>
  <memories>
    <memory>Generalizable insight 1</memory>
    <memory>Generalizable insight 2</memory>
  </memories>
```

### Memory injection during evaluation

Memories are prepended to the problem prompt as a numbered list:

```
Before solving, consider these insights from prior analysis:

  1. [insight from memory item 1]
  2. [insight from memory item 2]

Apply these insights to the problem below.

[original problem prompt]
```

## Output structure

```
results/
├── math/
│   ├── generations/generations.jsonl   # {problem_id, solutions: [...]}
│   ├── scores/scores.jsonl             # {problem_id, scores: [{score, tier, ...}]}
│   ├── memories/memories.jsonl         # {problem_id, items: [{insight, reasoning}]}
│   └── evaluations/evaluations.jsonl   # {problem_id, baseline_pass_rate, augmented_pass_rate, improvement}
└── coding/
    └── ...
```

## Important notes

- **API cost:** A full run generates 16 solutions x ~900 problems x 3 stages (generation, memory, evaluation) = ~43K+ API calls. Use `--max-problems` to test incrementally.
- **Resume:** The pipeline resumes from where it left off. Each problem is checkpointed independently. Safe to interrupt and restart.
- **Code execution:** Coding problems run generated code in a subprocess with a 30-second timeout. This is suitable for research but not sandboxed for untrusted code.
- **Scoring:** Math uses exact integer match. Coding compares stdout against expected output after stripping whitespace.
- **No memory = skip:** If all K generations fall in the same tier (e.g., all correct), there's nothing to contrast, so no memory is created and evaluation uses the baseline score for both.
- **Verification first:** This pipeline tests memories on the *same* tasks they were created from. This is an intentional verification step before later generalizing to unseen tasks via embedding-based retrieval.
