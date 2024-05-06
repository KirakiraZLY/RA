# Commands during RA
## Week 16

# Estimate per-predictor h2, BLD-LDAK model
```
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

${dir_LDAK} --cut-weights /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno3  --no-thin DONE


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/Step1_her_bld_ldak.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch Step1_her_bld_ldak.sh



${dir_LDAK} --calc-weights-all /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno3
mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/sections/weights.short /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld65

${dir_LDAK} --calc-tagging /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld.ldak   --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power -.25 --annotation-number 65 --annotation-prefix bld --save-matrix YES

```


## Step 1
```
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

shuf -n 5000 /faststorage/project/dsmwpred/data/ukbb/geno3.fam > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/rand_geno3.5000

for j in {1..22}; do
${dir_LDAK} --calc-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_$j --bfile /faststorage/project/dsmwpred/data/ukbb/geno3  --chr $j --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/rand_geno3.5000  --max-threads 4
done

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/list.txt; for j in {1..22}; do echo "cors_geno3_$j" >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/list.txt; done

${dir_LDAK} --join-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --corslist /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/list.txt

### Estimate per-predictor heritabilities assuming the LDAK-Thin Model
${dir_LDAK} --thin /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/geno3_thin --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --window-prune .98 --window-kb 100 --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/rand_geno3.5000  --max-threads 4

awk < /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/geno3_thin.in '{print $1, 1}' > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/geno3_thin_weights.thin

${dir_LDAK} --calc-tagging /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/geno3_thin.thin --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --weights /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/geno3_thin_weights.thin --power -.25 --window-kb 1000 --save-matrix YES --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/rand_geno3.5000  --max-threads 4

```



## Summary Statistics Test

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_snoring_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_snoring_regenie.bayesr.sh







# BLD-LDAK
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

${dir_LDAK} --cut-weights sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno3
${dir_LDAK} --calc-weights-all sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno3  --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/rand_geno3.5000
mv sections/weights.short bld65

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/bld_chrpos_to_rsid.R

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/bld_chrpos_to_rsid.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/
sbatch bld_chrpos_to_rsid.sh

==============================================================================================================

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-tagging BLD-LDAK --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power -.25 --annotation-number 65 --annotation-prefix bld  --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/rand_geno3.5000   --save-matrix YES

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/bld_ldak.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/
sbatch bld_ldak.sh








# UKBB


### 1. snoring
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_snoring_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_snoring_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_snoring_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_snoring_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_snoring_ldak.bayesr.sh



```


### 2. sbp

#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_sbp_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_sbp_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_sbp_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_sbp_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_sbp_ldak.bayesr.sh



```


### 3. reaction
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_reaction_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_reaction_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_reaction_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_reaction_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_reaction_ldak.bayesr.sh



```


### 4. quals
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_quals_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_quals_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_quals_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_quals_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_quals_ldak.bayesr.sh



```


### 5. pulse
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_pulse_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_pulse_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_pulse_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_pulse_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_pulse_ldak.bayesr.sh



```


### 6. neur
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_neur_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_neur_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_neur_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_neur_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_neur_ldak.bayesr.sh



```


### 7. imp
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_imp_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_imp_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_imp_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_imp_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_imp_ldak.bayesr.sh



```


### 8. hyper
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_hyper_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_hyper_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_hyper_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_hyper_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_hyper_ldak.bayesr.sh



```


### 9. height
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_height_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_height_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_height_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_height_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_height_ldak.bayesr.sh



```


### 10. fvc
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_fvc_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_fvc_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_fvc_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_fvc_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_fvc_ldak.bayesr.sh



```


### 11. ever
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_ever_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_ever_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_ever_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_ever_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_ever_ldak.bayesr.sh



```


### 12. chron
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_chron_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_chron_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_chron_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_chron_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_chron_ldak.bayesr.sh



```


### 13. bmi
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_bmi_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_bmi_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_bmi_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_bmi_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_bmi_ldak.bayesr.sh



```


### 14. awake
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_regenie_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_regenie_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_regenie_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_regenie_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_awake_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_awake_regenie.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_ldak_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_ldak_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_ldak_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_ldak_Phenotype.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_ldak_Phenotype.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_ldak_Phenotype.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/ukbb/geno3_awake_ldak_Phenotype.bayesr.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/geno3_awake_ldak.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch geno3_awake_ldak.bayesr.sh



```



# FinnGen

1 finngen_R10_E4_THYROID 68
2 finngen_R10_I9_AF 4231
3 finngen_R10_I9_HYPTENS 4052
4 finngen_R10_I9_HYPTENSESS 4052
5 finngen_R10_I9_VARICVE 4425
6 finngen_R10_K11_MALABSORB 5257
7 finngen_R10_M13_DUPUTRYEN 8528
8 finngen_R10_M13_FIBROBLASTIC 8528
9 finngen_R10_T2D_WIDE 2356

## MegaPRS
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/finngen/finngen_R10_E4_THYROID.geno3.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/finngen/finngen_R10_E4_THYROID.geno3.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/finngen/finngen_R10_E4_THYROID.geno3.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/finngen/finngen_R10_E4_THYROID.geno3.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/finngen/finngen_R10_E4_THYROID.geno3.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code68.pheno

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/finngen/finngen_R10_E4_THYROID.geno3.bayesr.profile)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/finngen/finngen_R10_E4_THYROID.geno3.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/finngen/finngen_R10_E4_THYROID.geno3.bayesr.profile  --num-blocks 200 --prevalence ${prev}


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/finngen_R10_E4_THYROID.geno3.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch finngen_R10_E4_THYROID.geno3.bayesr.sh



```



# PGC

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC_UKB_depression_genome-wide.geno3.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC_UKB_depression_genome-wide.geno3.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC_UKB_depression_genome-wide.geno3.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC_UKB_depression_genome-wide.geno3.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC_UKB_depression_genome-wide.geno3.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC_UKB_depression_genome-wide.geno3.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC_UKB_depression_genome-wide.geno3.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC_UKB_depression_genome-wide.geno3.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC_UKB_depression_genome-wide.geno3.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/MDD_F32.pheno

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC_UKB_depression_genome-wide.geno3.bayesr.profile)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC_UKB_depression_genome-wide.geno3.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC_UKB_depression_genome-wide.geno3.bayesr.profile  --num-blocks 200 --prevalence ${prev}




${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/BIP_F31.pheno

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.bayesr.profile)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/daner_bip_pgc3_nm_noukbiobank.geno3.bayesr.profile  --num-blocks 200  --prevalence ${prev}





${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/SCZ_F20.pheno

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.bayesr.profile)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno3.bayesr.profile  --num-blocks 200 --prevalence ${prev}






" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/PGC.geno3.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch PGC.geno3.bayesr.sh

```


# MVP

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.EUR.HDL.gwas.dbGAP.geno3.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.EUR.HDL.gwas.dbGAP.geno3.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.EUR.HDL.gwas.dbGAP.geno3.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.EUR.HDL.gwas.dbGAP.geno3.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.EUR.HDL.gwas.dbGAP.geno3.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker29.pheno

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.EUR.HDL.gwas.dbGAP.geno3.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.EUR.HDL.gwas.dbGAP.geno3.bayesr.profile  --num-blocks 200





${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/SBP_MVP_White.results.geno3.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/SBP_MVP_White.results.geno3.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/SBP_MVP_White.results.geno3.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/SBP_MVP_White.results.geno3.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/SBP_MVP_White.results.geno3.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /home/lezh/snpher/faststorage/biobank/phenotypes/sbp.clean

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/SBP_MVP_White.results.geno3.bayesr.profile)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/SBP_MVP_White.results.geno3.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/SBP_MVP_White.results.geno3.bayesr.profile  --num-blocks 200




${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.ss.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.ss.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.ss.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno3_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno3_cor_ld/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.ss.ldak

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.bayesr --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.bayesr.effects --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power 0 --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker19.pheno

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.bayesr.profile)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno3.bayesr.profile  --num-blocks 200



" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/MVP.geno3.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch MVP.geno3.bayesr.sh
