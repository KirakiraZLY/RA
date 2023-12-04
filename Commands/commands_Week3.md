# Commands during RA
## Week 3

12/4/2023

# New MegaPRS
## 1. Pre-pre cor

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-cors ${dir_RA}/megaprs_new/geno_precor --bfile ${dir_data}/geno --window-cm 3


" > ${dir_RA}/scripts/megaprs_new/geno_precor

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/
sbatch geno_precor
```
