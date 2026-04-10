#!/bin/bash
#SBATCH --job-name=vllm-qwen35-397b-tp8
#SBATCH --partition=main
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:8
#SBATCH --cpus-per-task=32
#SBATCH --mem=256G
#SBATCH --time=72:00:00
#SBATCH --export=ALL
#SBATCH --output=/mnt/weka/home/seungwook.han/memory/slurm/logs_vllm/%x-%j.out
#SBATCH --error=/mnt/weka/home/seungwook.han/memory/slurm/logs_vllm/%x-%j.err

set -euo pipefail

REPO_ROOT="/mnt/weka/home/seungwook.han/memory"
VLLM_VENV="/mnt/weka/home/seungwook.han/LLM360-vllm/.venv"
VLLM_BIN="$VLLM_VENV/bin/vllm"
LOG_DIR="$REPO_ROOT/slurm/logs_vllm"
HOST_FILE="$LOG_DIR/qwen35_397b_a17b_fp8_host.txt"
PORT_FILE="$LOG_DIR/qwen35_397b_a17b_fp8_port.txt"
ENDPOINT_FILE="$LOG_DIR/qwen35_397b_a17b_fp8_endpoint.txt"
PORT="${PORT:-8000}"
MODEL="${MODEL:-Qwen/Qwen3.5-397B-A17B-FP8}"

mkdir -p "$LOG_DIR"
cd "$REPO_ROOT"

if [[ ! -x "$VLLM_BIN" ]]; then
    echo "vLLM binary not found at $VLLM_BIN" >&2
    exit 1
fi

source "$VLLM_VENV/bin/activate"

export HF_HOME="${HF_HOME:-/mnt/weka/home/seungwook.han/.cache/huggingface}"
export VLLM_LOGGING_LEVEL="${VLLM_LOGGING_LEVEL:-INFO}"

HOSTNAME_FQDN="$(hostname -s)"
echo "$HOSTNAME_FQDN" > "$HOST_FILE"
echo "$PORT" > "$PORT_FILE"
echo "http://${HOSTNAME_FQDN}:${PORT}/v1" > "$ENDPOINT_FILE"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Starting $SLURM_JOB_NAME on $(hostname)"
echo "Model: $MODEL"
echo "vLLM: $VLLM_BIN"
echo "Host file: $HOST_FILE"
echo "Endpoint: $(cat "$ENDPOINT_FILE")"
echo "HF_HOME: $HF_HOME"
echo "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-unset}"
nvidia-smi -L

CMD=(
    "$VLLM_BIN" serve "$MODEL"
    --host 0.0.0.0
    --port "$PORT"
    --tensor-parallel-size 8
    --max-model-len 262144
    --reasoning-parser qwen3
    --language-model-only
)

if [[ -n "${VLLM_API_KEY:-}" ]]; then
    CMD+=(--api-key "$VLLM_API_KEY")
fi

if [[ -n "${VLLM_EXTRA_ARGS:-}" ]]; then
    # shellcheck disable=SC2206
    EXTRA_ARGS=( $VLLM_EXTRA_ARGS )
    CMD+=("${EXTRA_ARGS[@]}")
fi

printf 'Command:'
printf ' %q' "${CMD[@]}"
printf '\n'

exec srun --ntasks=1 "${CMD[@]}"
