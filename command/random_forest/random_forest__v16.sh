#!/bin/sh

#SBATCH --job-name=random_forest__v16
#SBATCH --output=random_forest__v16-out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --partition=shared-cpu
#SBATCH --time=04:00:00
#SBATCH --mem-per-cpu=5000

module load GCCcore/11.2.0 Python/3.9.6
pip install -r titanic_spaceship_package/requirements.txt
python script_tuning.py random_forest__v16