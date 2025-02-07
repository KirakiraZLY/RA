
# Week 18


## GWAS
### LDAK run
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/geno3_height_fullsize_gwas_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts
sbatch geno3_height_fullsize_gwas_ldak.sh


```



## formatting

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3  --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3  --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3   --N 450000 

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3    --N 450000


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/geno3_ukbb_fullsize.formatting.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/
sbatch geno3_ukbb_fullsize.formatting.sh



## BayesR

### Step 2
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_snoring_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_sbp_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_reaction_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_quals_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_pulse_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_neur_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_imp_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_hyper_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_height_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_fvc_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_ever_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_chron_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_bmi_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_awake_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.summaries


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/bayesr_step2.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/
sbatch bayesr_step2.sh

```













































## Elastic

### Step 2
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_snoring_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_sbp_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_reaction_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_quals_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_pulse_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_neur_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_imp_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_hyper_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_height_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_fvc_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_ever_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_chron_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_bmi_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.summaries

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_awake_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.summaries


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/elastic_step2.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/
sbatch elastic_step2.sh

```






## Score

### test -> standardize

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/snoring.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/snoring.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/sbp.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/sbp.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/reaction.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/reaction.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/quals.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/quals.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/pulse.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/pulse.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/neur.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/neur.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/imp.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/imp.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/hyper.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/hyper.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/fvc.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/fvc.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/ever.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/ever.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/chron.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/chron.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/bmi.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/bmi.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/awake.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/awake.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

find /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits -type f -name '*.standard.*' ! -name '*.res' -exec rm -f {} +

for file in *.res; do
    awk '{print $1, $2, $5}' "$file" > "${file%.res}.test"
done


### Bayesr


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_snoring_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_snoring_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/snoring.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_snoring_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_snoring_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_sbp_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_sbp_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/sbp.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_sbp_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_sbp_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_reaction_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_reaction_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/reaction.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_reaction_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_reaction_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_quals_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_quals_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/quals.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_quals_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_quals_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_pulse_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_pulse_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/pulse.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_pulse_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_pulse_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_neur_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_neur_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/neur.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_neur_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_neur_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_imp_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_imp_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/imp.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_imp_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_imp_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_hyper_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_hyper_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/hyper.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_hyper_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_hyper_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_height_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_height_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_height_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_height_ldak.megaprs.bayesr.pred.profile  --num-blocks 200



${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_fvc_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_fvc_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/fvc.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_fvc_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_fvc_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_ever_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_ever_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/ever.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_ever_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_ever_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_chron_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_chron_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/chron.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_chron_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_chron_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_bmi_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_bmi_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/bmi.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_bmi_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_bmi_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_awake_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_awake_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/awake.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_awake_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno3_awake_ldak.megaprs.bayesr.pred.profile  --num-blocks 200



" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/bayesr_score.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/
sbatch bayesr_score.sh



### Elastic


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_snoring_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_snoring_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/snoring.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_snoring_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_snoring_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_sbp_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_sbp_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/sbp.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_sbp_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_sbp_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_reaction_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_reaction_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/reaction.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_reaction_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_reaction_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_quals_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_quals_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/quals.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_quals_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_quals_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_pulse_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_pulse_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/pulse.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_pulse_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_pulse_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_neur_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_neur_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/neur.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_neur_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_neur_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_imp_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_imp_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/imp.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_imp_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_imp_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_hyper_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_hyper_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/hyper.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_hyper_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_hyper_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_height_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_height_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_height_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_height_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_fvc_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_fvc_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/fvc.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_fvc_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_fvc_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_ever_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_ever_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/ever.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_ever_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_ever_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_chron_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_chron_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/chron.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_chron_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_chron_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_bmi_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_bmi_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/bmi.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_bmi_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_bmi_ldak.megaprs.elastic.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_awake_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_awake_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/awake.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_awake_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/elastic/geno3_awake_ldak.megaprs.elastic.pred.profile  --num-blocks 200



" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/elastic_score.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/scripts/
sbatch elastic_score.sh






## Old megaprs


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --cut-weights /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno3
${dir_LDAK} --calc-weights-all /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno3  --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/rand_geno3.5000

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bld_ldak_geno3_1.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size
sbatch bld_ldak_geno3_1.sh


cp /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/weights.short /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/bld65

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/bld_chrpos_to_rsid.R


cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections

${dir_LDAK} --calc-tagging BLD-LDAK --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --power -.25 --annotation-number 65 --annotation-prefix bld  --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/rand_geno3.5000   --save-matrix YES




dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bldldak_geno4
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --cut-weights /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bldldak_geno4/sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno4
${dir_LDAK} --calc-weights-all /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bldldak_geno4/sections --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/rand_geno4.5000

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bld_ldak_geno4_1.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size
sbatch bld_ldak_geno4_1.sh


cp /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bldldak_geno4/sections/weights.short /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bldldak_geno4/sections/bld65


conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bldldak_geno4/sections/bld_chrpos_to_rsid.R

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bldldak_geno4/sections

${dir_LDAK} --calc-tagging BLD-LDAK --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --power -.25 --annotation-number 65 --annotation-prefix bld  --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/rand_geno4.5000  --save-matrix YES






### Run PRS


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_snoring_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_snoring_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_snoring_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_snoring_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_sbp_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_sbp_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_sbp_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_sbp_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_reaction_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_reaction_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_reaction_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_reaction_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_quals_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_quals_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_quals_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_quals_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_pulse_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_pulse_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_pulse_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_pulse_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_neur_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_neur_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_neur_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_neur_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_imp_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_imp_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_imp_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_imp_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_hyper_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_hyper_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_hyper_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_hyper_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_height_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_height_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_height_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_fvc_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_fvc_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_fvc_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_fvc_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_ever_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_ever_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_ever_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_ever_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_chron_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_chron_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_chron_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_chron_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_bmi_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_bmi_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_bmi_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_bmi_ldak.ldak

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_awake_ldak.bld --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/sections/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_awake_ldak.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_awake_ldak.bld.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_awake_ldak.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/oldmegaprs_run_step2.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs
sbatch oldmegaprs_run_step2.sh








### calc score


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_snoring_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_snoring_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/snoring.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_snoring_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_snoring_ldak.bayesr.pred.profile  --num-blocks 200

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_sbp_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_sbp_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/sbp.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_sbp_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_sbp_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_reaction_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_reaction_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/reaction.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_reaction_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_reaction_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_quals_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_quals_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/quals.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_quals_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_quals_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_pulse_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_pulse_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/pulse.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_pulse_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_pulse_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_neur_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_neur_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/neur.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_neur_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_neur_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_imp_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_imp_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/imp.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_imp_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_imp_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_hyper_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_hyper_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/hyper.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_hyper_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_hyper_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_height_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_height_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.standard.standard.test.indi.test.indi.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_height_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_height_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_fvc_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_fvc_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/fvc.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_fvc_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_fvc_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_ever_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_ever_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/ever.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_ever_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_ever_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_chron_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_chron_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/chron.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_chron_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_chron_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_bmi_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_bmi_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/bmi.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_bmi_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_bmi_ldak.bayesr.pred.profile  --num-blocks 200


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_awake_ldak.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_awake_ldak.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/awake.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_awake_ldak.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/results/geno3_awake_ldak.bayesr.pred.profile  --num-blocks 200



" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs/oldmegaprs_run_step3_calcscore.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/oldmegaprs
sbatch oldmegaprs_run_step3_calcscore.sh




## Test geno4

dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno4_height_ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/cors_geno4 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/highld_geno4/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno4_height_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno4_height_ldak.summaries

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak.megaprs.bayesr.pred.profile  --num-blocks 200





# Height fullsize -> 20Wan

cut -d' ' -f1 /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.20Wan.test.list.txt

awk 'NR==FNR{a[$1]; next} $1 in a' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.20Wan.train.list.txt /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.clean > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.20Wan.train


dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.20Wan.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno4_height_ldak_20Wan

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak_20Wan.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/cors_geno4 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/highld_geno4/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno4_height_ldak_20Wan.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno4_height_ldak_20Wan.summaries

${dir_LDAK} --reml /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.20Wan.standard.test --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.20Wan.test --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars  --keep /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak_20Wan.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak_20Wan.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.20Wan.standard.test.indi.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak_20Wan.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/bayesr/geno4_height_ldak_20Wan.megaprs.bayesr.pred.profile  --num-blocks 200










# Make Pheno and test

dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/test/makepheno

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --make-snps snps --num-samples 10000 --num-snps 20000
${dir_LDAK} --make-phenos pseudo_pheno --bfile snps --ignore-weights YES --power -1 --her 1 --num-phenos 1 --num-causals 300
${dir_LDAK} --pheno pseudo_pheno.pheno  --max-threads 4  --bfile snps --linear pseudo_pheno_gwas

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/test/makepheno/pseudo_test.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/test/makepheno/
sbatch pseudo_test.sh



/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/traits/height.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_full_size/ldak/geno3_height_ldak



cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/test/tagging

${dir_LDAK} --calc-tagging HumDef --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/test/makepheno/snps --power -.25