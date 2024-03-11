# Commands during RA
## Week 14

3/11/2024


# MVP ss
HDL, T2D, AAA, GAD, eGFR

ICD 10 disease against HDL: E78.5 Hyperlipidemia; E78.6 Lipoprotein deficiency
ICD 10 disease against T2D: E11.9 Type 2 diabetes mellitus
ICD 10 disease against AAA: I71.40 Abdominal aortic aneurysm, without rupture, unspecified
ICD 10 disease against GAD: F41.1 Generalized anxiety disorder
ICD 10 disease against eGFR: R94.4 Abnormal results of kidney function studies

## ANNOVAR
chr:pos -> rsid
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.chrpos.list /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150


" > /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.chrpos.list.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/
sbatch MVP.T2D.EUR.MAF001.dbGaP.checked.chrpos.list.sh

```


## LDAK formatting
```python

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results  --outputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak  --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

```

## Megaprs BayesR
### Step 2 Make Model 1 
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/dbGAP_hyperarousal_eur.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/dbGAP_hyperarousal_eur.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step2_dbGAP_hyperarousal_eur.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step2_dbGAP_hyperarousal_eur.megaprs.bayesr.sh

```
### Step 2 Make Model 2
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.AAA.fordbGaP.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.AAA.fordbGaP.txt.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.AAA.fordbGaP.txt.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step2_MVP.EUR.AAA.fordbGaP.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step2_MVP.EUR.AAA.fordbGaP.megaprs.bayesr.sh

```
### Step 2 Make Model 3
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.eGFR.dbGAP.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.eGFR.dbGAP.txt.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.eGFR.dbGAP.txt.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step2_MVP.EUR.eGFR.dbGAP.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step2_MVP.EUR.eGFR.dbGAP.megaprs.bayesr.sh

```

### Step 2 Make Model 4
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.txt.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.txt.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step2_MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step2_MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.sh

```

### Step 2 Make Model 5
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/SBP_MVP_White.results.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step2_SBP_MVP_White.results.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step2_SBP_MVP_White.results.megaprs.bayesr.sh

```


### Step 3 1 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/MDD_F32.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/step3_daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/
sbatch step3_daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.bayesr.sh

```


### Step 4, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.bayesr.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.bayesr.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/
sbatch daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.bayesr.pred.jackknife.sh

```


