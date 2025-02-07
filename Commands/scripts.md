# PRS comparison

2024.06.07


# UKBB


## LDAK GWAS run: sbp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_sbp_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno4_sbp_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno4_sbp_ldak.sh
```




## GWAS sumstat -> PRS format: sbp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno4_sbp_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_sbp_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_sbp_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_sbp_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_sbp_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_sbp_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_sbp_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno4_sbp_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno4_sbp_regenie_Phenotype.formatting.sh


```