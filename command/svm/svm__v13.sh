#!/bin/sh

#SBATCH --job-name=svm__v13
#SBATCH --output=svm__v13-out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --partition=shared-cpu
#SBATCH --time=10:00:00
#SBATCH --mem-per-cpu=5000

module load GCCcore/11.2.0 Python/3.9.6
pip install -r titanic_spaceship_package/requirements.txt
python script_tuning.py svm__v13