# Commands during RA
## Week 12

2/25/2024

# Get Japan genotype

```python

#########

#find a few snps and check maf - note that finnish pop have names starting with 12_

#get finnish individuals



echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 64:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

grep ^"18_" /faststorage/project/dsmwpred/doug/leyi/hrc.fam > /faststorage/project/dsmwpred/zly/RA/data/33KG/japan/jap.keep

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/doug/leyi/hrc --allow-no-sex --make-bed  --keep /faststorage/project/dsmwpred/zly/RA/data/33KG/japan/jap.keep  --out /faststorage/project/dsmwpred/zly/RA/data/33KG/japan/hrc_geno_jap


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/hrc_geno_jap.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch hrc_geno_jap.sh

```


# MVP

## download
wget -b -r https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs001672/analyses/
