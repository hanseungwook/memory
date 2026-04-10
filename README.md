# Memory from Generations

Experiment pipeline for creating reusable problem-solving memories from contrastive analysis of LLM generations.

Core idea: for each problem, the pipeline generates multiple attempts, scores them, groups successful and unsuccessful solutions, extracts transferable memory items from the contrast, and then checks whether injecting those memories improves performance on the same problem.

## Pipeline Overview

```text
Load Data -> Generate K Solutions -> Score -> Create Memories -> Evaluate -> Report
```

Each stage persists JSONL outputs under `results/<domain>/`, so runs can resume at per-problem granularity.

| Stage | What the current implementation does | Relevant files |
| --- | --- | --- |
| Load data | Lazily loads problems once per run. Math uses a HuggingFace AIME dataset loader; coding uses a HuggingFace loader that also decodes compressed test cases. | [`src/memgen/pipeline.py`](src/memgen/pipeline.py), [`src/memgen/data/math_loader.py`](src/memgen/data/math_loader.py), [`src/memgen/data/coding_loader.py`](src/memgen/data/coding_loader.py), [`src/memgen/data/base.py`](src/memgen/data/base.py) |
| Generate | Builds a domain-specific prompt and issues `K` async Chat Completions calls through the OpenAI SDK. | [`src/memgen/pipeline.py`](src/memgen/pipeline.py), [`src/memgen/generation/prompts.py`](src/memgen/generation/prompts.py), [`src/memgen/generation/generator.py`](src/memgen/generation/generator.py), [`src/memgen/openai_compat.py`](src/memgen/openai_compat.py) |
| Score | Math expects a final `ANSWER: <integer>` line and scores exact integer correctness. Coding extracts the last fenced code block, runs it against all tests, and assigns `fail` / `partial` / `full`. | [`src/memgen/pipeline.py`](src/memgen/pipeline.py), [`src/memgen/scoring/base.py`](src/memgen/scoring/base.py), [`src/memgen/scoring/math_scorer.py`](src/memgen/scoring/math_scorer.py), [`src/memgen/scoring/coding_scorer.py`](src/memgen/scoring/coding_scorer.py), [`src/memgen/scoring/sandbox.py`](src/memgen/scoring/sandbox.py) |
| Create memories | Groups solutions by tier, builds a contrastive prompt over all solutions in each non-empty tier, requests a memory response, and parses `<reasoning>` / `<memory>` tags. If fewer than two tiers are populated, memory creation is skipped. | [`src/memgen/pipeline.py`](src/memgen/pipeline.py), [`src/memgen/memory/creator.py`](src/memgen/memory/creator.py), [`src/memgen/memory/prompts.py`](src/memgen/memory/prompts.py) |
| Evaluate | Regenerates baseline samples, then regenerates augmented samples with memory injection when memory exists. `avg@k` is computed by binarizing each sample score to `1.0` only when it earns full credit, then averaging across the `K` samples. | [`src/memgen/pipeline.py`](src/memgen/pipeline.py), [`src/memgen/evaluation/evaluator.py`](src/memgen/evaluation/evaluator.py), [`src/memgen/evaluation/prompts.py`](src/memgen/evaluation/prompts.py) |
| Persist and inspect | Appends stage results to JSONL files and also writes per-problem artifact bundles as both JSON and Markdown. | [`src/memgen/persistence/store.py`](src/memgen/persistence/store.py) |
| CLI entrypoints | Runs the pipeline by stage and prints aggregate evaluation stats. | [`src/memgen/cli.py`](src/memgen/cli.py) |

## Setup

```bash
pip install -e ".[dev]"
```

Environment:

```bash
export OPENAI_API_KEY=sk-...
```

For a local vLLM server, add an explicit `llm` block to your config and point it at the OpenAI-compatible endpoint:

```yaml
llm:
  provider: "vllm"
  base_url: "http://localhost:8000/v1"
  api_key: "token"
```

The package requires Python 3.12+ and installs its runtime dependencies from [`pyproject.toml`](pyproject.toml).

## Usage

### Run the full pipeline

```bash
# Math
memgen run -c config/math_aime.yaml

# Coding
memgen run -c config/coding_lcb.yaml
```

### Run a smaller slice

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

### Print aggregate results

```bash
memgen report -c config/math_aime.yaml
```

### Build an interactive viewer for one result set

```bash
# Writes results/slurm_20260408_10sample/math/visualization.html
memgen visualize results/slurm_20260408_10sample/math

# Write somewhere else and open it immediately
memgen visualize results/slurm_20260408_10sample/math \
  --output /tmp/memgen-math-view.html \
  --open
```

`memgen visualize` is scoped to one result-set directory at a time. Point it at a path like `results/<run>/<domain>` or `results/<domain>`, and the generated page lets you switch across problem details, generation, scoring, memory, and evaluation views for that specific set.

The CLI surface is implemented in [`src/memgen/cli.py`](src/memgen/cli.py), and stage dispatch lives in [`src/memgen/pipeline.py`](src/memgen/pipeline.py).

## Configuration

Configuration loading is defined in [`src/memgen/config.py`](src/memgen/config.py).

Important implementation detail: `load_config()` loads exactly one YAML file and then lets the Pydantic models fill in missing fields from code defaults. It does not merge `config/math_aime.yaml` or `config/coding_lcb.yaml` with [`config/default.yaml`](config/default.yaml).

- [`config/math_aime.yaml`](config/math_aime.yaml) only defines the math dataset.
- [`config/coding_lcb.yaml`](config/coding_lcb.yaml) only defines the coding dataset.
- [`config/default.yaml`](config/default.yaml) is a reference preset, not an automatically applied base config, and it is not runnable by itself because it has no `dataset` block.

So when you run `memgen run -c config/math_aime.yaml`, the effective fallback values come from the code defaults in [`src/memgen/config.py`](src/memgen/config.py), not from [`config/default.yaml`](config/default.yaml).

### Code defaults used for unspecified fields

| Parameter | Default in code | Where it lives |
| --- | --- | --- |
| `llm.provider` | `openai` | [`src/memgen/config.py`](src/memgen/config.py) |
| `llm.base_url` | `null` | [`src/memgen/config.py`](src/memgen/config.py) |
| `llm.api_key` | `null` | [`src/memgen/config.py`](src/memgen/config.py) |
| `llm.timeout_seconds` | `null` | [`src/memgen/config.py`](src/memgen/config.py) |
| `llm.max_retries` | `2` | [`src/memgen/config.py`](src/memgen/config.py) |
| `generation.model` | `gpt-5-mini` | [`src/memgen/config.py`](src/memgen/config.py) |
| `generation.k` | `16` | [`src/memgen/config.py`](src/memgen/config.py) |
| `generation.temperature` | `0.7` | [`src/memgen/config.py`](src/memgen/config.py) |
| `generation.max_tokens` | `4096` | [`src/memgen/config.py`](src/memgen/config.py) |
| `generation.extra_body` | `{}` | [`src/memgen/config.py`](src/memgen/config.py) |
| `generation.concurrent_requests` | `16` | [`src/memgen/config.py`](src/memgen/config.py) |
| `memory.model` | `gpt-5-mini` | [`src/memgen/config.py`](src/memgen/config.py) |
| `memory.temperature` | `0.3` | [`src/memgen/config.py`](src/memgen/config.py) |
| `memory.max_tokens` | `2048` | [`src/memgen/config.py`](src/memgen/config.py) |
| `memory.extra_body` | `{}` | [`src/memgen/config.py`](src/memgen/config.py) |
| `evaluation.model` | `gpt-5-mini` | [`src/memgen/config.py`](src/memgen/config.py) |
| `evaluation.k` | `16` | [`src/memgen/config.py`](src/memgen/config.py) |
| `evaluation.temperature` | `0.7` | [`src/memgen/config.py`](src/memgen/config.py) |
| `evaluation.max_tokens` | `4096` | [`src/memgen/config.py`](src/memgen/config.py) |
| `evaluation.extra_body` | `{}` | [`src/memgen/config.py`](src/memgen/config.py) |
| `scoring.timeout_seconds` | `30` | [`src/memgen/config.py`](src/memgen/config.py) |
| `scoring.max_output_length` | `10000` | [`src/memgen/config.py`](src/memgen/config.py) |
| `concurrent_problems` | `1` | [`src/memgen/config.py`](src/memgen/config.py) |
| `results_dir` | `results` | [`src/memgen/config.py`](src/memgen/config.py) |
| `resume` | `true` | [`src/memgen/config.py`](src/memgen/config.py) |

### LLM provider compatibility

Request shaping is handled by [`src/memgen/openai_compat.py`](src/memgen/openai_compat.py).

- `llm.provider: openai` sends `max_completion_tokens`.
- `llm.provider: vllm` currently sends `max_tokens` and preserves configured sampling parameters such as `temperature`. Current vLLM chat-completions docs also accept `max_completion_tokens` and mark `max_tokens` as deprecated.
- For OpenAI GPT-5 chat models, custom `temperature` values are intentionally omitted because the API only supports the default temperature.
- `generation.extra_body`, `memory.extra_body`, and `evaluation.extra_body` are passed through to the OpenAI SDK as `extra_body`, which is useful for vLLM-only request options such as `top_k`.

Example vLLM override:

```yaml
llm:
  provider: "vllm"
  base_url: "http://localhost:8000/v1"
  api_key: "token"
generation:
  model: "Qwen/Qwen3-32B"
  extra_body:
    top_k: 20
memory:
  model: "Qwen/Qwen3-32B"
evaluation:
  model: "Qwen/Qwen3-32B"
```

If you launch vLLM locally, prefer a command like this so request-time sampling settings from the pipeline win over model repository defaults:

```bash
vllm serve Qwen/Qwen3-32B --api-key token --generation-config vllm
```

The served model must expose a chat template for `/v1/chat/completions`. If it does not, start vLLM with `--chat-template ./path/to/template.jinja`.

## Datasets

| Domain | Default dataset config | Loader |
| --- | --- | --- |
| Math | `gneubig/aime-1983-2024` / `train` | [`src/memgen/data/math_loader.py`](src/memgen/data/math_loader.py) |
| Coding | `hanseungwook/code_generation_lite` / `train` | [`src/memgen/data/coding_loader.py`](src/memgen/data/coding_loader.py) |

Implementation notes:

- The math loader supports multiple AIME-like schemas by checking alternate column names such as `ID`/`id` and `Question`/`Problem`.
- The coding loader decodes both plain JSON test cases and base64 + zlib + pickle encoded payloads.
- Coding metadata is preserved on the `Problem` object, including `func_name`, platform, difficulty, and title.

## Stage Details

### 1. Load data

The pipeline caches the loaded `Problem` objects in memory and chooses the loader from the configured domain in [`src/memgen/pipeline.py`](src/memgen/pipeline.py).

Relevant files:

- [`src/memgen/data/base.py`](src/memgen/data/base.py)
- [`src/memgen/data/math_loader.py`](src/memgen/data/math_loader.py)
- [`src/memgen/data/coding_loader.py`](src/memgen/data/coding_loader.py)

### 2. Generate

Prompt selection is domain-specific:

- Math generation uses [`src/memgen/generation/prompts.py`](src/memgen/generation/prompts.py) and reuses the competition-style math system prompt defined in [`src/memgen/evaluation/prompts.py`](src/memgen/evaluation/prompts.py).
- Coding generation uses the coding prompt builder in [`src/memgen/generation/prompts.py`](src/memgen/generation/prompts.py), including starter code when available.

The async generation engine is [`src/memgen/generation/generator.py`](src/memgen/generation/generator.py). It:

- lazily creates one shared `AsyncOpenAI` client for that generator instance,
- enforces a semaphore using `generation.concurrent_requests`,
- retries failed requests with exponential backoff,
- gathers `K` independent samples concurrently.

In `memory_mode: single`, the pipeline can also process multiple problems concurrently by setting `concurrent_problems`. That stage-level concurrency is separate from `generation.concurrent_requests`: the former controls how many problems are in flight, while the latter caps the shared generator's chat-completions concurrency.

### 3. Score

Scorer selection happens in [`src/memgen/scoring/coding_scorer.py`](src/memgen/scoring/coding_scorer.py) via `get_scorer()`.

Math scoring in [`src/memgen/scoring/math_scorer.py`](src/memgen/scoring/math_scorer.py):

- looks for a final `ANSWER:` line,
- parses boxed or plain arithmetic expressions with `math-verify`,
- canonicalizes the result to an exact integer,
- returns `score=1.0` / `tier=correct` or `score=0.0` / `tier=incorrect`.

Coding scoring in [`src/memgen/scoring/coding_scorer.py`](src/memgen/scoring/coding_scorer.py):

- extracts the last fenced code block from the model output,
- runs function-based grading when `problem.metadata["func_name"]` is present,
- otherwise runs stdin/stdout grading,
- computes a per-generation fractional score `passed / total`,
- maps that ratio to `fail`, `partial`, or `full`.

Execution lives in [`src/memgen/scoring/sandbox.py`](src/memgen/scoring/sandbox.py). Despite the module name, it is only a lightweight reliability guard and explicitly not a security sandbox.

### 4. Create memories

Memory grouping and request logic live in [`src/memgen/memory/creator.py`](src/memgen/memory/creator.py), with prompt construction and parsing in [`src/memgen/memory/prompts.py`](src/memgen/memory/prompts.py).

Current behavior:

1. Solutions are grouped by score tier in generation order.
2. If fewer than two tiers are populated, the pipeline writes `{"skipped": true}` for that problem and does not call the memory model.
3. Otherwise, the prompt includes the problem statement plus all solutions from each populated tier.
4. The response parser extracts one shared `<reasoning>` block and zero or more structured `<memory>` items containing `<title>`, `<description>`, and `<content>`.

The grouped tiers are:

- Math: `correct`, `incorrect`
- Coding: `full`, `partial`, `fail`

### 5. Evaluate

Evaluation is implemented in [`src/memgen/evaluation/evaluator.py`](src/memgen/evaluation/evaluator.py), and prompt injection lives in [`src/memgen/evaluation/prompts.py`](src/memgen/evaluation/prompts.py).

Current behavior:

1. Generate `evaluation.k` baseline samples using the same domain prompt family as the generation stage.
2. Score those samples with the same scorer used earlier in the pipeline.
3. If memory exists, prepend the memory items to the user prompt and generate a second augmented batch.
4. If memory was skipped, reuse the baseline generations and mark `used_baseline_for_augmented = true`.
5. Compute `avg@k` by binarizing each sample score to `1.0` only when it earns full credit, then averaging across the `K` samples.

That last point matters for coding: `partial` generations are still stored in the per-sample scores, but they contribute `0.0` to `avg@k`.

## Output Structure

Persistence is implemented in [`src/memgen/persistence/store.py`](src/memgen/persistence/store.py).

```text
results/
├── math/
│   ├── generations/generations.jsonl
│   ├── scores/scores.jsonl
│   ├── memories/memories.jsonl
│   ├── evaluations/evaluations.jsonl
│   └── artifacts/
│       ├── index.json
│       ├── index.md
│       └── <problem-slug>-<hash>/
│           ├── artifact.json
│           └── artifact.md
└── coding/
    └── ...
```

Per-stage JSONL payloads:

- `generations.jsonl`: `{"problem_id", "solutions"}`
- `scores.jsonl`: `{"problem_id", "scores"}`
- `memories.jsonl`: `{"problem_id", "items": [{"title", "description", "content", ...}], ...memory fields...}`
- `evaluations.jsonl`: `{"problem_id", ...evaluation fields...}`

Per-problem artifacts include the original problem plus accumulated stage payloads:

- `artifact.json`: machine-readable merged view of all completed stages
- `artifact.md`: human-readable report with prompts, outputs, grouped memory inputs, parsed memories, and evaluation results
- `artifacts/index.json` and `artifacts/index.md`: cross-problem index over saved artifacts

## Important Notes

- Resume support is implemented by checking completed problem IDs in the corresponding JSONL files. See `ResultStore.get_completed_ids()` in [`src/memgen/persistence/store.py`](src/memgen/persistence/store.py).
- The coding executor reduces accidental damage but is not suitable for securely running adversarial code. The warning is documented directly in [`src/memgen/scoring/sandbox.py`](src/memgen/scoring/sandbox.py).
- Memory creation only runs when at least two score tiers are present for a problem.
- If a memory response parses zero `<memory>` items, evaluation still treats that problem as having a memory object and will run an augmented pass with effectively no injected advice beyond blank separation.
- `memgen report` only summarizes completed evaluation outputs; it does not rerun any stage.
