#!/bin/bash
#SBATCH --job-name=memgen-aime-10-mathv2
#SBATCH --partition=cpuonly
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=12:00:00
#SBATCH --export=ALL
#SBATCH --output=/mnt/weka/home/seungwook.han/memory/slurm/logs/%x-%j.out
#SBATCH --error=/mnt/weka/home/seungwook.han/memory/slurm/logs/%x-%j.err

set -euo pipefail

REPO_ROOT="/mnt/weka/home/seungwook.han/memory"
CONFIG_PATH="$REPO_ROOT/config/slurm/math_aime_10sample_math_prompt_v2.yaml"

cd "$REPO_ROOT"

source /mnt/weka/home/seungwook.han/miniforge3/etc/profile.d/conda.sh
conda activate memory

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Starting $SLURM_JOB_NAME on $(hostname)"
echo "Config: $CONFIG_PATH"
echo "Python: $(which python)"
echo "OPENAI_API_KEY_SET=${OPENAI_API_KEY:+yes}"

python -u -m memgen.cli run -c "$CONFIG_PATH"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Completed $SLURM_JOB_NAME"
