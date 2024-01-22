# Commands during RA
# Week8

1/22/2024


# 33KG with 1000 Genome
## MAF comparison
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1 --freq --out /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_maf


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/33kg_geno_fin_1_maf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch 33kg_geno_fin_1_maf.sh

```