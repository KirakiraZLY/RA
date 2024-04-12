# Commands during RA
## Week 16

# Estimate per-predictor h2, BLD-LDAK model

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 12:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --cut-weights /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno4
${dir_LDAK} --calc-weights-all /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno4
mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/sections/weights.short /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld65

${dir_LDAK} --calc-tagging /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld.ldak   --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --power -.25 --annotation-number 65 --annotation-prefix bld --save-matrix YES


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/Step1_her_bld_ldak.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/scripts/
sbatch Step1_her_bld_ldak.sh



# Run Megaprs

## UKBB

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

./ldak.out --sum-hers bld.ldak --tagfile bld.ldak.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_snoring_regenie_Phenotype.ldak --matrix bld.ldak.matrix


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_snoring_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_snoring_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_snoring_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_snoring_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno4_snoring_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno4_snoring_regenie.megaprs.bayesr.sh

```

