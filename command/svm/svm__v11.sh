#!/bin/sh

#SBATCH --job-name=svm__v11
#SBATCH --output=svm__v11-out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --partition=shared-cpu
#SBATCH --time=12:00:00
#SBATCH --mem-per-cpu=5000

module load GCCcore/11.2.0 Python/3.9.6
pip install -r titanic_spaceship_package/requirements.txt
python script_tuning.py svm__v11