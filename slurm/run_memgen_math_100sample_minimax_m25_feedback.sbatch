#!/bin/bash
#SBATCH --job-name=memgen-math-100-mm25-feedback
#SBATCH --partition=main
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=48:00:00
#SBATCH --export=ALL
#SBATCH --output=/mnt/weka/home/seungwook.han/memory/slurm/logs/%x-%j.out
#SBATCH --error=/mnt/weka/home/seungwook.han/memory/slurm/logs/%x-%j.err

set -euo pipefail

REPO_ROOT="/mnt/weka/home/seungwook.han/memory"
CONFIG_PATH="$REPO_ROOT/config/slurm/math_aime_100sample_vllm_minimax_m25_feedback.yaml"

cd "$REPO_ROOT"

source /mnt/weka/home/seungwook.han/miniforge3/etc/profile.d/conda.sh
conda activate memory
export PYTHONPATH="$REPO_ROOT/src${PYTHONPATH:+:$PYTHONPATH}"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Starting $SLURM_JOB_NAME on $(hostname)"
echo "Config: $CONFIG_PATH"
echo "Python: $(which python)"
echo "PYTHONPATH: $PYTHONPATH"

python -u -m memgen.cli run -c "$CONFIG_PATH"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Completed $SLURM_JOB_NAME"
