# Commands during RA
## Week 16

## Missing values

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/eur/EUR.QC --geno 0 --mind 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/eur/EUR.QC



/faststorage/project/dsmwpred/zly/software/plink  --make-bed --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4  --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4_30wan.snplist  --out  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4_30wan


## UKBB test

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_height_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_height_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_height_regenie_Phenotype.ldpred.inf.sh

```
