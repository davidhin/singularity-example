#!/bin/bash
#SBATCH -p batch
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --time=00:10:00
#SBATCH --mem=1GB
#SBATCH --array=1-10
#SBATCH --gres=gpu:1
#SBATCH --err="logs/main_%a.err"
#SBATCH --output="logs/main_%a.out"
#SBATCH --job-name="main_job"

# Setup Python Environment
module load arch/haswell
module load Anaconda3/2020.07
module load CUDA/10.2.89
module load Singularity
module load git/2.21.0-foss-2016b

# Echo job id into results file
echo "array_job_index: $SLURM_ARRAY_TASK_ID"

# Start singularity instance
singularity run main.simg -p main -r $SLURM_ARRAY_TASK_ID
