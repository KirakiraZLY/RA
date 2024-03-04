# Commands during RA
## Week 13

3/4/2024


# LDpred2 auto
## Try with one trait
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_1.R

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_2_auto.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code156.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19_addn/finngen_R10_M13_SACROILIITIS.hg19.addn  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/result/finngen_R10_M13_SACROILIITIS.auto.ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/script/finngen_R10_M13_SACROILIITIS.auto.ldpred2.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/script/
sbatch finngen_R10_M13_SACROILIITIS.auto.ldpred2.sh


```


