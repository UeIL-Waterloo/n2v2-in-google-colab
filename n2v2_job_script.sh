#!/bin/bash
#SBATCH --mem=128G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --gpus-per-node=1
#SBATCH --time=0:30:0    
#SBATCH --mail-user=<##your email here##>
#SBATCH --mail-type=ALL

cd ~/$projects/##username
module purge
module load python/3.10 scipy-stack
virtualenv --no-download ~/n2v2
source ~/n2v2/bin/activate

pip install --no-index tensorflow==2.12
pip install n2v

python n2v2_training.py
