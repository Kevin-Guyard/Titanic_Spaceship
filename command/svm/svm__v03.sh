#!/bin/sh

#SBATCH --job-name=svm__v03
#SBATCH --output=svm__v03-out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --partition=public-cpu
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=5000

module load GCCcore/11.2.0 Python/3.9.6
pip install -r titanic_spaceship_package/requirements.txt
python script_tuning.py svm__v03