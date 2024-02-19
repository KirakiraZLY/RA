# Commands during RA
# Week 11

2/18/2024

# Run LDpred2

## Change SS from hg38 to hg37

### Make BED
```python
awk 'NR>1 && $5 ~ /^rs/ {print "chr"$1, ($2-1), $2, $5}'  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/finngen_R10_I9_HYPTENS.bed
```
### Liftover
```python

/home/lezh/dsmwpred/zly/RA/data/liftover/liftOver /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/finngen_R10_I9_HYPTENS.bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/liftover/finngen_R10_I9_HYPTENS.lifted /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/liftover/finngen_R10_I9_HYPTENS.unlifted


```

## Make Bed
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 100:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/LDpred2_readbed.R

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/readbed.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/
sbatch readbed.sh


```