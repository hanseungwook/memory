#!/bin/bash
#SBATCH --job-name=memgen_shards
#SBATCH --array=0-199%100
#SBATCH --partition=lowprio
#SBATCH --qos=lowprio
#SBATCH --requeue
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --gres=gpu:8
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --time=21-00:00:00
#SBATCH -o /mnt/weka/home/seungwook.han/memory/slurm_logs/%A_%a.out
#SBATCH -e /mnt/weka/home/seungwook.han/memory/slurm_logs/%A_%a.err

set -euo pipefail
mkdir -p /mnt/weka/home/seungwook.han/memory/slurm_logs
cd /mnt/weka/home/seungwook.han/memory
  source /mnt/weka/home/seungwook.han/miniforge3/bin/activate /mnt/weka/home/seungwook.han/miniforge3/envs/harbor
export VLLM_ENV=/mnt/weka/home/seungwook.han/miniforge3/envs/harbor
export PYTHON_SITE=/mnt/weka/home/seungwook.han/miniforge3/envs/harbor/lib/python3.12/site-packages
export PATH="${VLLM_ENV}/bin:$PATH"
export LD_LIBRARY_PATH="${VLLM_ENV}/lib:${PYTHON_SITE}/nvidia/nvjitlink/lib:${PYTHON_SITE}/nvidia/cusparse/lib:${PYTHON_SITE}/nvidia/cublas/lib:${PYTHON_SITE}/nvidia/cuda_runtime/lib:${LD_LIBRARY_PATH:-}"
mkdir -p /mnt/weka/home/seungwook.han/memory/vllm_logs
export VLLM_PORT_START=8000
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
export VLLM_ROOT_URL="http://${VLLM_HOST}:${VLLM_PORT}"
export VLLM_BASE_URL="http://${VLLM_HOST}:${VLLM_PORT}/v1"
echo "Using shard-local vLLM port ${VLLM_PORT}"
export VLLM_API_KEY=token
export VLLM_MODEL=MiniMaxAI/MiniMax-M2.7
export SAFETENSORS_FAST_GPU=1
VLLM_LOG_FILE="/mnt/weka/home/seungwook.han/memory/vllm_logs/${SLURM_JOB_ID}_${SLURM_ARRAY_TASK_ID}_vllm.log"
echo "Starting shard ${SLURM_ARRAY_TASK_ID} on $(hostname) at $(date)"

"${VLLM_ENV}/bin/vllm" serve MiniMaxAI/MiniMax-M2.7 --host ${VLLM_HOST} --port ${VLLM_PORT} --api-key ${VLLM_API_KEY} --generation-config vllm --trust-remote-code --enable_expert_parallel --tensor-parallel-size 8 --enable-auto-tool-choice --tool-call-parser minimax_m2 --reasoning-parser minimax_m2_append_think > "$VLLM_LOG_FILE" 2>&1 &
VLLM_PID=$!
cleanup() {
  if kill -0 "$VLLM_PID" 2>/dev/null; then
    kill "$VLLM_PID" 2>/dev/null || true
    wait "$VLLM_PID" || true
  fi
}
trap cleanup EXIT

DEADLINE=$(( $(date +%s) + 7200 ))
until python - <<'PY'; do
import json
import os
import urllib.request

root_url = os.environ["VLLM_ROOT_URL"]
base_url = os.environ["VLLM_BASE_URL"]
model = os.environ["VLLM_MODEL"]
api_key = os.environ.get("VLLM_API_KEY", "")
headers = {}
if api_key:
    headers["Authorization"] = f"Bearer {api_key}"

health_request = urllib.request.Request(f"{root_url}/health", headers=headers)
with urllib.request.urlopen(health_request, timeout=10) as response:
    if response.status != 200:
        raise SystemExit(1)

models_request = urllib.request.Request(f"{base_url}/models", headers=headers)
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

  source /mnt/weka/home/seungwook.han/miniforge3/bin/activate /mnt/weka/home/seungwook.han/miniforge3/envs/memory

memgen run -c /mnt/weka/home/seungwook.han/memory/config/slurm/guru_full_vllm_minimax_m27_feedback.yaml --num-shards 200 --shard-index ${SLURM_ARRAY_TASK_ID} --llm-provider vllm --llm-base-url ${VLLM_BASE_URL} --llm-api-key ${VLLM_API_KEY} --model MiniMaxAI/MiniMax-M2.7 --generation-concurrent-requests 128 --concurrent-problems 16
