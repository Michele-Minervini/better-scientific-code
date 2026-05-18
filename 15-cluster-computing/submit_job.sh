# This is the standard template. It asks the cluster for 8 CPU cores, activates a conda environment, and runs a Python script.

#!/bin/bash

# ==============================================================================
# 1. SLURM RESOURCE REQUEST (The "Magic" Comments)
# ==============================================================================

#SBATCH --job-name=quantum_sweep      # Name of your job
#SBATCH --output=logs/output_%j.txt   # Standard output log (%j = Job ID)
#SBATCH --error=logs/error_%j.txt     # Standard error log
#SBATCH --nodes=1                     # How many physical computers to use
#SBATCH --cpus-per-task=8             # How many cores per computer (For multiprocessing!)
#SBATCH --mem=16G                     # Total RAM requested
#SBATCH --time=02:00:00               # Max time (Hours:Minutes:Seconds)
#SBATCH --partition=standard          # Which queue to wait in (depends on your university)

# ==============================================================================
# 2. ENVIRONMENT SETUP
# ==============================================================================

echo "Job started on $(hostname) at $(date)"

# Most clusters use 'modules' to load software. 
module purge
module load python/3.11
# module load cuda/11.8  <-- (Uncomment if using GPUs!)

# Activate your specific Conda environment (from Lesson 07)
# source ~/.bashrc
# conda activate qml_env

# ==============================================================================
# 3. RUN THE CODE
# ==============================================================================

# Ensure the logs directory exists so Slurm doesn't crash trying to save the output
mkdir -p logs

# Run the python script. 
# We use argparse (Lesson 08) to pass variables, and we pass the SLURM_CPUS_PER_TASK variable so Python knows exactly how many cores it is allowed to use (Lesson 14).

python cluster_task.py --beta 1.5 --n_samples 1000 --cores $SLURM_CPUS_PER_TASK

echo "Job finished at $(date)"