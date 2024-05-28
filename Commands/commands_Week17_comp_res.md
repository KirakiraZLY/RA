
# Old Megaprs


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


shuf -n 5000 /faststorage/project/dsmwpred/data/ukbb/geno4.fam > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/oldmega/rand_geno4.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/oldmega/cors_geno4 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/rand_geno4.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/oldmega/highld_geno4 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --genefile /home/lezh/snpher/faststorage/highld.txt

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/oldmega/geno4_height_regenie_Phenotype.thin --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldak --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/bld_ldak/BLD-LDAK.matrix --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldak

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/oldmega/geno4_height_regenie_Phenotype.bayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/oldmega/geno4_height_regenie_Phenotype.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldak --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_old_megaprs/HER/cors_geno4_total --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/highld_geno4/genes.predictors.used --window-kb 1000 --allow-ambiguous YES --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/geno4_height_regenie.oldmega.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/
sbatch geno4_height_regenie.oldmega.sh





# Bayesr

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

shuf -n 5000 /faststorage/project/dsmwpred/data/ukbb/geno4.fam > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/bayesr/rand_geno4.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/bayesr/cors_geno4 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/rand_geno4.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/bayesr/highld_geno4 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --genefile /home/lezh/snpher/faststorage/highld.txt

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/bayesr/geno4_height_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/cors_geno4 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/highld_geno4/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/geno4_height_regenie.bayesr.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/
sbatch geno4_height_regenie.bayesr.sh






# Elastic

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

shuf -n 5000 /faststorage/project/dsmwpred/data/ukbb/geno4.fam > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/elastic/rand_geno4.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/elastic/cors_geno4 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/rand_geno4.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/elastic/highld_geno4 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --genefile /home/lezh/snpher/faststorage/highld.txt

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/elastic/geno4_height_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/cors_geno4 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/highld_geno4/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/geno4_height_regenie.elastic.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/
sbatch geno4_height_regenie.elastic.sh



## her 0.01
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_awake_ldak.megaprs.bayesr.001 --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/cors_geno4 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/highld_geno4/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_awake_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_awake_ldak.summaries --her 0.01


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_awake_ldak.megaprs.bayesr.001.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_awake_ldak.megaprs.bayesr.001.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_awake_ldak.megaprs.bayesr.001.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno4_awake_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno4_awake_ldak.megaprs.bayesr.001.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno4_awake_ldak.megaprs.bayesr.001.sh

```













# PRS-CS

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

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/data/ukbb/geno4 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/prscs/geno4_height_regenie_Phenotype.prscs.results

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/geno4_height_regenie.prscs.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/
sbatch geno4_height_regenie.prscs.sh







# Classical
## Step 1

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

file_bfile="/faststorage/project/dsmwpred/data/ukbb/geno4"
file_sumstat="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldpred.ss"
file_outname="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/results/classical/geno4_height_regenie_Phenotype"
file_pheno="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/MDD_F32.pheno"
file_sh="geno4_height_regenie_Phenotype.classical"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/plink \
    --bfile ${file_bfile} \
    --clump-p1 1 \
    --clump-r2 0.1 \
    --clump-kb 250 \
    --clump ${file_sumstat} \
    --clump-snp-field Predictor \
    --clump-field P \
    --out ${file_outname}.classicalprs

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/${file_sh}.Step1.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/computation_resources/scripts/
sbatch ${file_sh}.Step1.sh


awk 'NR!=1{print $3}' ${file_outname}.classicalprs.clumped  >  ${file_outname}.classicalprs.valid.snp
awk '{print $1,$10}' ${file_sumstat} > ${file_outname}.SNP.pvalue



# LDpred2 auto

## TEST

software_dir="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub"
file_pheno="/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test"
file_sumstats="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldpred.ss"
file_output="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_height_regenie_Phenotype"
name_sh="geno4_height_regenie_Phenotype"

echo "#"'!'"/bin/bash
#SBATCH --mem 160G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_grid_fv.R --pheno ${file_pheno}  --sumstats  ${file_sumstats}  --outputFile  ${file_output}

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/${name_sh}.ldpred.grid.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts
sbatch ${name_sh}.ldpred.grid.sh





## Step 1 Generate PGS using LDPRED2-auto

software_dir="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub"
fileGenoRDS="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4.rds"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript ${software_dir}/createBackingFile.R --file-input /faststorage/project/dsmwpred/data/ukbb/geno4.bed --file-output /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4.rds

Rscript ${software_dir}/imputeGenotypes.R --impute-simple mean0 --geno-file-rds /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4.rds


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/ldpred2.rds.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/
sbatch ldpred2.rds.sh


## Calculate LD
```python

software_dir="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub"
fileGenoRDS="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4.rds"
fileSumstats="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldpred.ss"
fileOut="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4_height_regenie_Phenotype.ldpred2"
fileHapmap="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/map_hm3_plus.rds"

# point to input/output files
export fileGeno=/faststorage/project/dsmwpred/data/ukbb/geno4.bed
export fileGenoRDS=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4.rds
export filePheno=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test
export fileSumstats=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_ldak_Phenotype.ldpred.ss
export fileOutLD=ld-chr-@.rds
export fileOutLDMap=ld-map.rds

# set environmental variables. Replace "<path/to/comorment>" with 
# the full path to the folder containing cloned "containers" and "ldpred2_ref" repositories
export COMORMENT=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/highld
export SIF=$COMORMENT/containers/singularity
export REFERENCE=$COMORMENT/containers/reference
export LDPRED2_REF=$COMORMENT/ldpred2_ref
export SINGULARITY_BIND=$REFERENCE:/REF,${LDPRED2_REF}:/ldpred2_ref

export RSCRIPT="singularity exec --home=$PWD:/home $SIF/r.sif Rscript"

# convert genotype to LDpred2 format
# $RSCRIPT ${software_dir}/createBackingFile.R --file-input $fileGeno --file-output $fileGenoRDS

# create genetics maps directory, download and process

conda activate zly2
Rscript ${software_dir}/calculateLD.R --geno-file-rds $fileGenoRDS \
 --dir-genetic-maps /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/interpolated_from_hapmap \
 --sumstats $fileSumstats Predictor \
 --file-ld-blocks $fileOutLD \
 --file-ld-map $fileOutLDMap

```


## Step2 Running model

software_dir="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub"
fileGenoRDS="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4.rds"
fileSumstats="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldpred.ss"
fileOut="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4_height_regenie_Phenotype.ldpred2"
fileHapmap="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/map_hm3_plus.rds"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate zly2

Rscript ${software_dir}/ldpred2.R \
 --geno-impute-zero \
 --ldpred-mode auto \
 --merge-by-rsid \
 --col-chr Chr \
 --col-snp-id Predictor \
 --col-A1 A1 \
 --col-A2 A2 \
 --ld-meta-file ${fileHapmap} \
 --geno-file-rds ${fileGenoRDS} \
 --sumstats ${fileSumstats} \
 --out ${fileOut}.auto

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/geno4_height_regenie_Phenotype.ldpred2.auto.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub/test/
sbatch geno4_height_regenie_Phenotype.ldpred2.auto.sh



# SBayesRC

```python

ma_file="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_ldak_Phenotype.sbayesrc.cojo"               # GWAS summary in COJO format (the only input)
ld_folder="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/sbayesrc/ld_ukbEUR_HM3"        # LD reference (download from "Resources")
annot="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/sbayesrc/annot_baseline2.2.txt"         # Functional
out_prefix="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/sbayesrc/result/geno4_height_ldak_Phenotype.sbayesrc" 
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
pheno_file="/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test"
threads=4 # Number of CPU cores
export OMP_NUM_THREADS=$threads # Revise the threads`

conda activate zly2

Rscript -e "SBayesRC::tidy(mafile='$ma_file', LDdir='$ld_folder',output='${out_prefix}_tidy.ma', log2file=TRUE)"
Rscript -e "SBayesRC::impute(mafile='${out_prefix}_tidy.ma', LDdir='$ld_folder',output='${out_prefix}_imp.ma', log2file=TRUE)"
Rscript -e "SBayesRC::sbayesrc(mafile='${out_prefix}_imp.ma', LDdir='$ld_folder',outPrefix='${out_prefix}_sbrc', annot='$annot', log2file=TRUE)"

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/bayesrc_formatting.R --inputFile ${out_prefix}_sbrc.txt  --outputFile ${out_prefix}_sbrc.effect


${dir_LDAK} --calc-scores ${out_prefix}_sbrc.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --scorefile ${out_prefix}_sbrc.effect   --max-threads 4  --pheno ${pheno_file}


${dir_LDAK} --jackknife ${out_prefix}_sbrc.jackknife --profile ${out_prefix}_sbrc.pred.profile  --num-blocks 200


```






# LDpred2 grid
## UKBB

### height
software_dir="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub"
file_pheno="/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test"
file_sumstats="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_ldak_Phenotype.ldpred.ss"
file_output="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_height_ldak_Phenotype"
name_sh="geno4_height_ldak_Phenotype"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

echo "#"'!'"/bin/bash
#SBATCH --mem 160G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_grid_fv.R --pheno ${file_pheno}  --sumstats  ${file_sumstats}  --outputFile  ${file_output}


${dir_LDAK} --calc-scores ${file_output}.ldpred.grid.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4   --scorefile ${file_output}.effects  --max-threads 4  --pheno ${file_pheno}

${dir_LDAK} --jackknife ${file_output}.ldpred.grid.pred.jackknife --profile /${file_output}.ldpred.grid.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/${name_sh}.ldpred.grid.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts
sbatch ${name_sh}.ldpred.grid.sh


### best model

for file in *.ldpred.grid.pred.jackknife.jack; do
    awk '$2 == "Squared_correlation" {print $0}' "$file" | sort -k3,3nr | head -n 1 > "${file%.ldpred.grid.pred.jackknife.jack}.bestmodel"
done


## PGC


software_dir="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub"
file_pheno="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/MDD_F32.pheno"
file_sumstats="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.geno4.ldpred.ss"
file_output="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.geno4"
name_sh="daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.geno4"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

echo "#"'!'"/bin/bash
#SBATCH --mem 160G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_grid_fv.R --pheno ${file_pheno}  --sumstats  ${file_sumstats}  --outputFile  ${file_output}


${dir_LDAK} --calc-scores ${file_output}.ldpred.grid.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4   --scorefile ${file_output}.effects  --max-threads 4  --pheno ${file_pheno}

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/${name_sh}.ldpred.grid.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts
sbatch ${name_sh}.ldpred.grid.sh


prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' ${file_output}.ldpred.grid.pred.profile)

${dir_LDAK} --jackknife ${file_output}.ldpred.grid.pred.jackknife --profile ${file_output}.ldpred.grid.pred.profile  --num-blocks 200  --prevalence ${prev}


for file in *.ldpred.grid.pred.jackknife.jack; do
    awk '$2 == "Squared_correlation" {print $0}' "$file" | sort -k3,3nr | head -n 1 > "${file%.ldpred.grid.pred.jackknife.jack}.bestmodel"
done






software_dir="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub"
file_pheno="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/BIP_F31.pheno"
file_sumstats="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/daner_bip_pgc3_nm_noukbiobank.geno4.ldpred.ss"
file_output="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/daner_bip_pgc3_nm_noukbiobank.geno4"
name_sh="daner_bip_pgc3_nm_noukbiobank.geno4"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

echo "#"'!'"/bin/bash
#SBATCH --mem 160G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_grid_fv.R --pheno ${file_pheno}  --sumstats  ${file_sumstats}  --outputFile  ${file_output}


${dir_LDAK} --calc-scores ${file_output}.ldpred.grid.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4   --scorefile ${file_output}.effects  --max-threads 4  --pheno ${file_pheno}

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/${name_sh}.ldpred.grid.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts
sbatch ${name_sh}.ldpred.grid.sh


prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' ${file_output}.ldpred.grid.pred.profile)

${dir_LDAK} --jackknife ${file_output}.ldpred.grid.pred.jackknife --profile ${file_output}.ldpred.grid.pred.profile  --num-blocks 200  --prevalence ${prev}


for file in *.ldpred.grid.pred.jackknife.jack; do
    awk '$2 == "Squared_correlation" {print $0}' "$file" | sort -k3,3nr | head -n 1 > "${file%.ldpred.grid.pred.jackknife.jack}.bestmodel"
done



## FinnGen

### chr:pos -> rsid hg38 -> hg19

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.chrpos.list

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF.chrpos.list

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS.chrpos.list

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS.chrpos.list

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE.chrpos.list

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB.chrpos.list

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.chrpos.list

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.chrpos.list

awk 'NR >= 3 {print $1, $2, $2, $3, $4}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.chrpos.list

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh


/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/finngen_hg38_to_hg19.sh

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/
sbatch finngen_hg38_to_hg19.sh

### rsid -> chr:pos （用这个）


awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.rsid.list

awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF.rsid.list

awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS.rsid.list

awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS.rsid.list

awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE.rsid.list

awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB.rsid.list

awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.rsid.list

awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.rsid.list

awk 'NR >= 3 {print $5}' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.rsid.list

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.rsid.list.tochrpos

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF.rsid.list.tochrpos

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS.rsid.list.tochrpos

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS.rsid.list.tochrpos

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE.rsid.list.tochrpos

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB.rsid.list.tochrpos

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.rsid.list.tochrpos

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.rsid.list.tochrpos

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/convert2annovar.pl -format rsid /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.rsid.list -dbsnpfile /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/hg19_snp138.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.rsid.list.tochrpos

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/finngen_hg38_to_hg19.sh

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/
sbatch finngen_hg38_to_hg19.sh

#### Update .addn

for file in *.tochrpos; do
  if [ -e "$file" ]; then
    # 使用 awk 处理文件并重定向输出到临时文件，然后覆盖原文件
    awk 'NF == 6' "$file" > temp.txt && mv temp.txt "$file"
    echo "Processed $file"
  else
    echo "No .tochrpos files found"
  fi
done

#### convert sumstat

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.rsid.list.tochrpos

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF.rsid.list.tochrpos

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS.rsid.list.tochrpos

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS.rsid.list.tochrpos

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE.rsid.list.tochrpos

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB.rsid.list.tochrpos

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.rsid.list.tochrpos

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.rsid.list.tochrpos

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_rsid_to_chrpos.R --inputFileSS /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.addn --inputFileChrPos /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.rsid.list.tochrpos

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/finngen_convert_addn1.sh

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/
sbatch finngen_convert_addn1.sh

### Make SS

echo "#"'!'"/bin/bash
#SBATCH --mem 160G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_AF  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENSESS  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_VARICVE  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_K11_MALABSORB  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.addn.1  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/finngen_ss.sh

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/
sbatch finngen_ss.sh

### Run LDpred2


software_dir="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/fromGithub"
file_pheno="/home/lezh/snpher/faststorage/biobank/newphens/icdphens/code2356.pheno"
file_sumstats="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.ldpred.ss"
file_output="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/finngen/finngen_R10_T2D_WIDE.geno4"
name_sh="finngen_R10_T2D_WIDE.geno4"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

echo "#"'!'"/bin/bash
#SBATCH --mem 160G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_grid_fv.R --pheno ${file_pheno}  --sumstats  ${file_sumstats}  --outputFile  ${file_output}

${dir_LDAK} --calc-scores ${file_output}.ldpred.grid.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4   --scorefile ${file_output}.effects  --max-threads 4  --pheno ${file_pheno}

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/${name_sh}.ldpred.grid.sh

cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts
sbatch ${name_sh}.ldpred.grid.sh


















## MVP

### Make SS
