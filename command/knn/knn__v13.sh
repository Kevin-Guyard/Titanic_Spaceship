#!/bin/sh

#SBATCH --job-name=knn__v13
#SBATCH --output=knn__v13-out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --partition=shared-cpu
#SBATCH --time=04:00:00
#SBATCH --mem-per-cpu=5000

module load GCCcore/11.2.0 Python/3.9.6
pip install -r titanic_spaceship_package/requirements.txt
python script_tuning.py knn__v13