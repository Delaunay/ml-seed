#!/bin/bash
set -evx

# Usage:
#   sbatch --gres=gpu:1 --cpus-per-gpu=4 --mem=16G scripts/single-gpu.sh {{cookiecutter.project_name}}/train_normal.py
#

# Slurm configuration
# ===================
#SBATCH --exclude=kepler4,kepler3


# Python
# ===================

module load miniconda/3
conda activate py39


# Environment
# ===================

export {{cookiecutter.PROJECT_NAME}}_DATASET_DEST=$SLURM_TMPDIR/dataset
export {{cookiecutter.PROJECT_NAME}}_CHECKPOINT_PATH=~/scratch/checkpoint


# Run
# ===================

cmd="$@"

echo $cmd

python $cmd

