#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shlex
import textwrap
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate sharded memgen launch commands or Slurm scripts."
    )
    parser.add_argument(
        "--config",
        required=True,
        help="Base memgen YAML config to pass to each shard run.",
    )
    parser.add_argument(
        "--num-shards",
        required=True,
        type=int,
        help="Total number of dataset shards to launch.",
    )
    parser.add_argument(
        "--mode",
        choices=("commands", "slurm-array"),
        default="commands",
        help="Emit one command per shard or a single Slurm array script.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional file path to write the generated launcher.",
    )
    parser.add_argument(
        "--run-command",
        default="memgen run",
        help="Command prefix used to start a shard job.",
    )
    parser.add_argument(
        "--extra-args",
        default="",
        help="Extra arguments appended verbatim to each memgen command.",
    )
    parser.add_argument(
        "--bootstrap-vllm",
        action="store_true",
        help="Start a local vLLM instance inside each shard job before memgen.",
    )
    parser.add_argument(
        "--workdir",
        default=str(Path.cwd()),
        help="Working directory used in generated shell scripts.",
    )
    parser.add_argument(
        "--venv-activate",
        default=None,
        help="Optional shell snippet or path to source before both vLLM and memgen when specific hooks are unset.",
    )
    parser.add_argument(
        "--vllm-activate",
        default=None,
        help="Optional shell snippet or path to source before starting vLLM.",
    )
    parser.add_argument(
        "--memgen-activate",
        default=None,
        help="Optional shell snippet or path to source before running memgen.",
    )
    parser.add_argument(
        "--vllm-env-dir",
        default=None,
        help="Optional vLLM environment prefix; emits PATH and LD_LIBRARY_PATH exports for that env.",
    )
    parser.add_argument(
        "--served-model",
        default="MiniMaxAI/MiniMax-M2.7",
        help="Model served by the local vLLM instance and used by memgen.",
    )
    parser.add_argument(
        "--vllm-port",
        type=int,
        default=8000,
        help="Local port for the shard-local vLLM server.",
    )
    parser.add_argument(
        "--vllm-api-key",
        default="token",
        help="API key passed to the local vLLM server and memgen client.",
    )
    parser.add_argument(
        "--vllm-tensor-parallel-size",
        type=int,
        default=8,
        help="tensor_parallel_size passed to vllm serve.",
    )
    parser.add_argument(
        "--vllm-extra-args",
        default="",
        help="Extra arguments appended verbatim to vllm serve.",
    )
    parser.add_argument(
        "--vllm-start-timeout-seconds",
        type=int,
        default=7200,
        help="How long to wait for the local vLLM server to become ready.",
    )
    parser.add_argument(
        "--generation-concurrent-requests",
        type=int,
        default=None,
        help="Override generation.concurrent_requests in the memgen run.",
    )
    parser.add_argument(
        "--concurrent-problems",
        type=int,
        default=None,
        help="Override pipeline concurrent_problems in the memgen run.",
    )
    parser.add_argument(
        "--slurm-job-name",
        default="memgen_shards",
        help="Slurm job name prefix for generated array scripts.",
    )
    parser.add_argument(
        "--slurm-partition",
        default=None,
        help="Optional Slurm partition for generated array scripts.",
    )
    parser.add_argument(
        "--slurm-qos",
        default=None,
        help="Optional Slurm QOS for generated array scripts.",
    )
    parser.add_argument(
        "--slurm-array-concurrency",
        type=int,
        default=None,
        help="Optional max number of simultaneous tasks in the Slurm array, emitted as %%N.",
    )
    parser.add_argument(
        "--slurm-requeue",
        action="store_true",
        help="Emit #SBATCH --requeue for generated Slurm scripts.",
    )
    parser.add_argument(
        "--slurm-cpus-per-task",
        type=int,
        default=64,
        help="cpus-per-task for generated Slurm scripts.",
    )
    parser.add_argument(
        "--slurm-gpus",
        type=int,
        default=8,
        help="Number of GPUs requested per Slurm task.",
    )
    parser.add_argument(
        "--slurm-time",
        default="21-00:00:00",
        help="Wall-clock time for generated Slurm scripts.",
    )
    parser.add_argument(
        "--slurm-log-dir",
        default="slurm_logs",
        help="Directory for Slurm stdout/stderr logs.",
    )
    parser.add_argument(
        "--vllm-log-dir",
        default="vllm_logs",
        help="Directory for per-shard vLLM server logs.",
    )
    return parser.parse_args()


def _quote(value: str | Path) -> str:
    return shlex.quote(str(value))


def _command_suffix(extra_args: str) -> str:
    stripped = extra_args.strip()
    return f" {stripped}" if stripped else ""


def _override_flag(flag: str, value: str | int | None) -> str:
    return _override_flag_with_mode(flag, value, quote_value=True)


def _override_flag_with_mode(
    flag: str,
    value: str | int | None,
    *,
    quote_value: bool,
) -> str:
    if value is None:
        return ""
    rendered = _quote(value) if quote_value else str(value)
    return f" {flag} {rendered}"


def _build_memgen_command(
    *,
    config_path: str,
    num_shards: int,
    shard_index_expr: str,
    run_command: str,
    extra_args: str,
    llm_base_url: str | None = None,
    llm_api_key: str | None = None,
    served_model: str | None = None,
    generation_concurrent_requests: int | None = None,
    concurrent_problems: int | None = None,
) -> str:
    quoted_config = _quote(Path(config_path).resolve())
    suffix = _command_suffix(extra_args)
    command = (
        f"{run_command} -c {quoted_config} "
        f"--num-shards {num_shards} --shard-index {shard_index_expr}"
    )
    if llm_base_url is not None:
        command += " --llm-provider vllm"
        command += _override_flag_with_mode(
            "--llm-base-url",
            llm_base_url,
            quote_value=not str(llm_base_url).startswith("${"),
        )
    command += _override_flag_with_mode(
        "--llm-api-key",
        llm_api_key,
        quote_value=not str(llm_api_key).startswith("${") if llm_api_key is not None else True,
    )
    command += _override_flag("--model", served_model)
    command += _override_flag(
        "--generation-concurrent-requests",
        generation_concurrent_requests,
    )
    command += _override_flag("--concurrent-problems", concurrent_problems)
    return command + suffix


def _build_vllm_launch_command(args: argparse.Namespace) -> str:
    launcher = "vllm"
    if args.vllm_env_dir:
        launcher = '"${VLLM_ENV}/bin/vllm"'

    return (
        f"{launcher} serve {_quote(args.served_model)} "
        f"--host ${'{'}VLLM_HOST{'}'} "
        f"--port ${'{'}VLLM_PORT{'}'} "
        f"--api-key ${'{'}VLLM_API_KEY{'}'} "
        "--generation-config vllm "
        "--trust-remote-code "
        "--enable_expert_parallel "
        f"--tensor-parallel-size {args.vllm_tensor_parallel_size} "
        "--enable-auto-tool-choice "
        "--tool-call-parser minimax_m2 "
        "--reasoning-parser minimax_m2_append_think"
        f"{_command_suffix(args.vllm_extra_args)} "
        '> "$VLLM_LOG_FILE" 2>&1 &'
    )


def _build_commands(args: argparse.Namespace) -> str:
    commands = []
    for shard_index in range(args.num_shards):
        command = _build_memgen_command(
            config_path=args.config,
            num_shards=args.num_shards,
            shard_index_expr=str(shard_index),
            run_command=args.run_command,
            extra_args=args.extra_args,
            llm_base_url=(
                f"http://127.0.0.1:{args.vllm_port}/v1" if args.bootstrap_vllm else None
            ),
            llm_api_key=args.vllm_api_key if args.bootstrap_vllm else None,
            served_model=args.served_model if args.bootstrap_vllm else None,
            generation_concurrent_requests=args.generation_concurrent_requests,
            concurrent_problems=args.concurrent_problems,
        )
        if not args.bootstrap_vllm:
            commands.append(command)
            continue

        workdir = _quote(Path(args.workdir).resolve())
        vllm_activate_line = _build_activation_line(args.vllm_activate, args.venv_activate)
        vllm_env_exports = _build_vllm_env_exports(args.vllm_env_dir)
        memgen_activate_line = _build_activation_line(args.memgen_activate, args.venv_activate)
        vllm_port_exports = _build_vllm_port_exports(args.vllm_port)
        commands.append(
            textwrap.dedent(
                f"""\
                # shard {shard_index}
                (
                  set -euo pipefail
                  cd {workdir}
                {vllm_activate_line}
                {vllm_env_exports}
                {vllm_port_exports}
                  export VLLM_API_KEY={_quote(args.vllm_api_key)}
                  export VLLM_MODEL={_quote(args.served_model)}
                  export SAFETENSORS_FAST_GPU=1
                  mkdir -p {_quote(Path(args.vllm_log_dir))}
                  VLLM_LOG_FILE={_quote(str(Path(args.vllm_log_dir) / f"shard_{shard_index}.log"))}
                  {_build_vllm_launch_command(args)}
                  VLLM_PID=$!
                  trap 'kill "$VLLM_PID" 2>/dev/null || true; wait "$VLLM_PID" || true' EXIT
                  {_readiness_function_body(args.vllm_start_timeout_seconds)}
                {memgen_activate_line}
                  {command}
                )
                """
            ).rstrip()
        )
    return "\n\n".join(commands) + "\n"


def _build_venv_line(venv_activate: str | None) -> str:
    if not venv_activate:
        return ""
    stripped = venv_activate.strip()
    if stripped.startswith("source ") or stripped.startswith(". "):
        return f"  {stripped}\n"
    return f"  source {_quote(stripped)}\n"


def _build_activation_line(primary: str | None, fallback: str | None = None) -> str:
    if primary:
        return _build_venv_line(primary)
    return _build_venv_line(fallback)


def _resolve_python_site_dir(env_dir: str | None) -> Path | None:
    if not env_dir:
        return None
    root = Path(env_dir).expanduser().resolve()
    candidates = sorted(root.glob("lib/python*/site-packages"), key=_python_site_sort_key)
    if candidates:
        return candidates[-1]
    return None


def _python_site_sort_key(path: Path) -> tuple[int, ...]:
    version_name = path.parent.name
    try:
        version = version_name.removeprefix("python")
        return tuple(int(part) for part in version.split("."))
    except Exception:
        return (0,)


def _build_vllm_env_exports(env_dir: str | None) -> str:
    site_dir = _resolve_python_site_dir(env_dir)
    if not env_dir or site_dir is None:
        return ""

    env_root = _quote(Path(env_dir).expanduser().resolve())
    site_root = _quote(site_dir)
    return textwrap.dedent(
        f"""\
          export VLLM_ENV={env_root}
          export PYTHON_SITE={site_root}
          export PATH="${{VLLM_ENV}}/bin:$PATH"
          export LD_LIBRARY_PATH="${{VLLM_ENV}}/lib:${{PYTHON_SITE}}/nvidia/nvjitlink/lib:${{PYTHON_SITE}}/nvidia/cusparse/lib:${{PYTHON_SITE}}/nvidia/cublas/lib:${{PYTHON_SITE}}/nvidia/cuda_runtime/lib:${{LD_LIBRARY_PATH:-}}"
        """
    )


def _build_vllm_port_exports(preferred_port: int) -> str:
    return textwrap.dedent(
        f"""\
          export VLLM_PORT_START={preferred_port}
          export VLLM_HOST=127.0.0.1
          export VLLM_PORT=$(python - <<'PY'
        import os
        import socket

        host = os.environ.get("VLLM_HOST", "127.0.0.1")
        start = int(os.environ.get("VLLM_PORT_START", "8000"))
        for port in range(start, start + 1000):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    sock.bind((host, port))
                except OSError:
                    continue
            print(port)
            break
        else:
            raise SystemExit("no free localhost port available for vLLM")
        PY
          )
          export VLLM_ROOT_URL="http://${{VLLM_HOST}}:${{VLLM_PORT}}"
          export VLLM_BASE_URL="http://${{VLLM_HOST}}:${{VLLM_PORT}}/v1"
          echo "Using shard-local vLLM port ${{VLLM_PORT}}"
        """
    ).rstrip()


def _readiness_function_body(timeout_seconds: int) -> str:
    return textwrap.dedent(
        f"""\
        DEADLINE=$(( $(date +%s) + {timeout_seconds} ))
        until python - <<'PY'; do
        import json
        import os
        import urllib.request

        root_url = os.environ["VLLM_ROOT_URL"]
        base_url = os.environ["VLLM_BASE_URL"]
        model = os.environ["VLLM_MODEL"]
        api_key = os.environ.get("VLLM_API_KEY", "")
        headers = {{}}
        if api_key:
            headers["Authorization"] = f"Bearer {{api_key}}"

        health_request = urllib.request.Request(f"{{root_url}}/health", headers=headers)
        with urllib.request.urlopen(health_request, timeout=10) as response:
            if response.status != 200:
                raise SystemExit(1)

        models_request = urllib.request.Request(f"{{base_url}}/models", headers=headers)
        with urllib.request.urlopen(models_request, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
        model_ids = [item.get("id") for item in payload.get("data", []) if isinstance(item, dict)]
        if model not in model_ids:
            raise SystemExit(1)
        PY
          if ! kill -0 "$VLLM_PID" 2>/dev/null; then
            echo "vLLM exited before becoming ready" >&2
            tail -n 200 "$VLLM_LOG_FILE" || true
            exit 1
          fi
          if [ "$(date +%s)" -ge "$DEADLINE" ]; then
            echo "Timed out waiting for vLLM readiness" >&2
            tail -n 200 "$VLLM_LOG_FILE" || true
            exit 1
          fi
          sleep 10
        done
        """
    ).rstrip()


def _build_slurm_array(args: argparse.Namespace) -> str:
    workdir = Path(args.workdir).resolve()
    slurm_log_dir = (workdir / args.slurm_log_dir).resolve()
    array_spec = f"0-{args.num_shards - 1}"
    if args.slurm_array_concurrency is not None:
        array_spec += f"%{args.slurm_array_concurrency}"
    lines = [
        "#!/bin/bash",
        f"#SBATCH --job-name={args.slurm_job_name}",
        f"#SBATCH --array={array_spec}",
        "#SBATCH --ntasks=1",
        f"#SBATCH --cpus-per-task={args.slurm_cpus_per_task}",
        f"#SBATCH --gres=gpu:{args.slurm_gpus}",
        "#SBATCH --exclusive",
        "#SBATCH --mem=0",
        f"#SBATCH --time={args.slurm_time}",
        f"#SBATCH -o {slurm_log_dir}/%A_%a.out",
        f"#SBATCH -e {slurm_log_dir}/%A_%a.err",
        "",
        "set -euo pipefail",
        f"mkdir -p {_quote(slurm_log_dir)}",
        f"cd {_quote(workdir)}",
    ]
    if args.slurm_partition:
        lines.insert(3, f"#SBATCH --partition={args.slurm_partition}")
    if args.slurm_qos:
        insert_index = 4 if args.slurm_partition else 3
        lines.insert(insert_index, f"#SBATCH --qos={args.slurm_qos}")
    if args.slurm_requeue:
        insert_index = 5 if args.slurm_partition and args.slurm_qos else 4 if (args.slurm_partition or args.slurm_qos) else 3
        lines.insert(insert_index, "#SBATCH --requeue")

    vllm_activate_line = _build_activation_line(args.vllm_activate, args.venv_activate).rstrip()
    vllm_env_exports = _build_vllm_env_exports(args.vllm_env_dir).rstrip()
    if vllm_activate_line:
        lines.append(vllm_activate_line)
    if vllm_env_exports:
        lines.append(vllm_env_exports)

    shard_expr = "${SLURM_ARRAY_TASK_ID}"
    if not args.bootstrap_vllm:
        memgen_activate_line = _build_activation_line(args.memgen_activate, args.venv_activate).rstrip()
        if memgen_activate_line and memgen_activate_line != vllm_activate_line:
            lines.append(memgen_activate_line)
        lines.extend(
            [
                "",
                _build_memgen_command(
                    config_path=args.config,
                    num_shards=args.num_shards,
                    shard_index_expr=shard_expr,
                    run_command=args.run_command,
                    extra_args=args.extra_args,
                    generation_concurrent_requests=args.generation_concurrent_requests,
                    concurrent_problems=args.concurrent_problems,
                ),
                "",
            ]
        )
        return "\n".join(lines)

    vllm_log_dir = (workdir / args.vllm_log_dir).resolve()
    vllm_port_exports = _build_vllm_port_exports(args.vllm_port)
    lines.extend(
        [
            f"mkdir -p {_quote(vllm_log_dir)}",
            vllm_port_exports,
            f"export VLLM_API_KEY={_quote(args.vllm_api_key)}",
            f"export VLLM_MODEL={_quote(args.served_model)}",
            "export SAFETENSORS_FAST_GPU=1",
            f'VLLM_LOG_FILE="{vllm_log_dir}/${{SLURM_JOB_ID}}_${{SLURM_ARRAY_TASK_ID}}_vllm.log"',
            'echo "Starting shard ${SLURM_ARRAY_TASK_ID} on $(hostname) at $(date)"',
            "",
            _build_vllm_launch_command(args),
            "VLLM_PID=$!",
            'cleanup() {',
            '  if kill -0 "$VLLM_PID" 2>/dev/null; then',
            '    kill "$VLLM_PID" 2>/dev/null || true',
            '    wait "$VLLM_PID" || true',
            "  fi",
            "}",
            "trap cleanup EXIT",
            "",
            _readiness_function_body(args.vllm_start_timeout_seconds),
            "",
            _build_activation_line(args.memgen_activate, args.venv_activate).rstrip(),
            "",
            _build_memgen_command(
                config_path=args.config,
                num_shards=args.num_shards,
                shard_index_expr=shard_expr,
                run_command=args.run_command,
                extra_args=args.extra_args,
                llm_base_url="${VLLM_BASE_URL}",
                llm_api_key="${VLLM_API_KEY}",
                served_model=args.served_model,
                generation_concurrent_requests=args.generation_concurrent_requests,
                concurrent_problems=args.concurrent_problems,
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    if args.num_shards < 1:
        raise SystemExit("--num-shards must be at least 1")
    if args.bootstrap_vllm and args.mode != "slurm-array":
        raise SystemExit("--bootstrap-vllm is currently supported only with --mode slurm-array")

    if args.mode == "commands":
        output_text = _build_commands(args)
    else:
        output_text = _build_slurm_array(args)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_text)
    else:
        print(output_text, end="")


if __name__ == "__main__":
    main()
