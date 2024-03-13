# Commands during RA
## Week 14

3/11/2024


# MVP ss
HDL, T2D, AAA, hyperarouse, eGFR

ICD 10 disease against HDL: E78.5 code2640 Hyperlipidemia; E78.6 Lipoprotein deficiency
    /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker29.pheno
ICD 10 disease against T2D: E11.9 code2366 Type 2 diabetes mellitus
ICD 10 disease against AAA: I71.40 code4356 I71 Abdominal aortic aneurysm, without rupture, unspecified
ICD 10 disease against hyperarouse: F41.1 code2942 Generalized anxiety disorder
ICD 10 disease against eGFR: R94.4 code 12653 R94 Abnormal results of kidney function studies

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
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.txt  --outputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ss  --outputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results  --outputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.txt  --outputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.eGFR.dbGAP.txt  --outputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.eGFR.dbGAP --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.AAA.fordbGaP.txt  --outputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.AAA.fordbGaP --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/dbGAP_hyperarousal_eur  --outputFile /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/dbGAP_hyperarousal_eur --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

" > /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/mvp_formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/
sbatch mvp_formatting.sh
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


### Step 2 Make Model 6
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ss.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ss.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step2_MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step2_MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.sh

```




HDL, T2D, AAA, hyperarouse, eGFR

ICD 10 disease against HDL: E78.5 code2640 Hyperlipidemia; E78.6 Lipoprotein deficiency
    /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker29.pheno
ICD 10 disease against T2D: E11.9 code2366 Type 2 diabetes mellitus
ICD 10 disease against AAA: I71.40 code4356 I71 Abdominal aortic aneurysm, without rupture, unspecified
ICD 10 disease against hyperarouse: F41.1 code2942 Generalized anxiety disorder
ICD 10 disease against eGFR: R94.4 code 12653 R94 Abnormal results of kidney function studies

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
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code2620.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step3_dbGAP_hyperarousal_eur.megaprs.bayesr.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step3_dbGAP_hyperarousal_eur.megaprs.bayesr.pred.sh

```
### Step 3 2 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.AAA.fordbGaP.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.AAA.fordbGaP.megaprs.bayesr.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code2366.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step3_MVP.EUR.AAA.fordbGaP.megaprs.bayesr.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step3_MVP.EUR.AAA.fordbGaP.megaprs.bayesr.pred.sh

```

### Step 3 3 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.eGFR.dbGAP.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.eGFR.dbGAP.megaprs.bayesr.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code4356.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step3_MVP.EUR.eGFR.dbGAP.megaprs.bayesr.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step3_MVP.EUR.eGFR.dbGAP.megaprs.bayesr.pred.sh

```


### Step 3 4 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker29.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step3_MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step3_MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.pred.sh

```


### Step 3 5 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/SBP_MVP_White.results.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/SBP_MVP_White.results.megaprs.bayesr.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code12653.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step3_SBP_MVP_White.results.megaprs.bayesr.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step3_SBP_MVP_White.results.megaprs.bayesr.pred.sh

```



### Step 3 6 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code2366.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/step3_MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch step3_MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.pred.sh

```




### Step 4 1, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/dbGAP_hyperarousal_eur.megaprs.bayesr.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch dbGAP_hyperarousal_eur.megaprs.bayesr.pred.jackknife.sh

```


### Step 4 2, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.AAA.fordbGaP.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.AAA.fordbGaP.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.AAA.fordbGaP.megaprs.bayesr.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/MVP.EUR.AAA.fordbGaP.megaprs.bayesr.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch MVP.EUR.AAA.fordbGaP.megaprs.bayesr.pred.jackknife.sh

```


### Step 4 3, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.eGFR.dbGAP.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.eGFR.dbGAP.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.eGFR.dbGAP.megaprs.bayesr.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/MVP.EUR.eGFR.dbGAP.megaprs.bayesr.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch MVP.EUR.eGFR.dbGAP.megaprs.bayesr.pred.jackknife.sh

```


### Step 4 4, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

#prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.pred.profile.1  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch MVP.EUR.HDL.gwas.dbGAP.megaprs.bayesr.pred.jackknife.sh

```


### Step 4 5, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/SBP_MVP_White.results.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/SBP_MVP_White.results.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/SBP_MVP_White.results.megaprs.bayesr.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/SBP_MVP_White.results.megaprs.bayesr.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch SBP_MVP_White.results.megaprs.bayesr.pred.jackknife.sh

```


### Step 4 6, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/bayesr/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/bayesr/
sbatch MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.bayesr.pred.jackknife.sh

```


## Megaprs Elastic
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/dbGAP_hyperarousal_eur.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/dbGAP_hyperarousal_eur.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/dbGAP_hyperarousal_eur.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step2_dbGAP_hyperarousal_eur.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step2_dbGAP_hyperarousal_eur.megaprs.elastic.sh

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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.AAA.fordbGaP.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.AAA.fordbGaP.txt.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.AAA.fordbGaP.txt.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step2_MVP.EUR.AAA.fordbGaP.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step2_MVP.EUR.AAA.fordbGaP.megaprs.elastic.sh

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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.eGFR.dbGAP.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.eGFR.dbGAP.txt.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.eGFR.dbGAP.txt.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step2_MVP.EUR.eGFR.dbGAP.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step2_MVP.EUR.eGFR.dbGAP.megaprs.elastic.sh

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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.txt.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.txt.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step2_MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step2_MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.sh

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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/SBP_MVP_White.results.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step2_SBP_MVP_White.results.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step2_SBP_MVP_White.results.megaprs.elastic.sh

```


### Step 2 Make Model 6
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ss.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ss.ldak

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step2_MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step2_MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.sh

```



HDL, T2D, AAA, hyperarouse, eGFR

ICD 10 disease against HDL: E78.5 code2640 Hyperlipidemia; E78.6 Lipoprotein deficiency
ICD 10 disease against T2D: E11.9 code2366 Type 2 diabetes mellitus
ICD 10 disease against AAA: I71.40 code4356 I71 Abdominal aortic aneurysm, without rupture, unspecified
ICD 10 disease against hyperarouse: F41.1 code2942 Generalized anxiety disorder
ICD 10 disease against eGFR: R94.4 code 12653 R94 Abnormal results of kidney function studies

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
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/dbGAP_hyperarousal_eur.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/dbGAP_hyperarousal_eur.megaprs.elastic.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code2620.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step3_dbGAP_hyperarousal_eur.megaprs.elastic.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step3_dbGAP_hyperarousal_eur.megaprs.elastic.pred.sh

```
### Step 3 2 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.AAA.fordbGaP.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.AAA.fordbGaP.megaprs.elastic.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code2366.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step3_MVP.EUR.AAA.fordbGaP.megaprs.elastic.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step3_MVP.EUR.AAA.fordbGaP.megaprs.elastic.pred.sh

```

### Step 3 3 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.eGFR.dbGAP.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.eGFR.dbGAP.megaprs.elastic.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code4356.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step3_MVP.EUR.eGFR.dbGAP.megaprs.elastic.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step3_MVP.EUR.eGFR.dbGAP.megaprs.elastic.pred.sh

```


### Step 3 4 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker29.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step3_MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step3_MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.pred.sh

```


### Step 3 5 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/SBP_MVP_White.results.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/SBP_MVP_White.results.megaprs.elastic.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code12653.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step3_SBP_MVP_White.results.megaprs.elastic.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step3_SBP_MVP_White.results.megaprs.elastic.pred.sh

```


### Step 3 6 Predicting, with checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code2366.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/step3_MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.pred.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch step3_MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.pred.sh

```





### Step 4 1, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/dbGAP_hyperarousal_eur.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/dbGAP_hyperarousal_eur.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/dbGAP_hyperarousal_eur.megaprs.elastic.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/dbGAP_hyperarousal_eur.megaprs.elastic.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch dbGAP_hyperarousal_eur.megaprs.elastic.pred.jackknife.sh

```


### Step 4 2, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.AAA.fordbGaP.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.AAA.fordbGaP.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.AAA.fordbGaP.megaprs.elastic.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/MVP.EUR.AAA.fordbGaP.megaprs.elastic.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch MVP.EUR.AAA.fordbGaP.megaprs.elastic.pred.jackknife.sh

```


### Step 4 3, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.eGFR.dbGAP.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.eGFR.dbGAP.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.eGFR.dbGAP.megaprs.elastic.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/MVP.EUR.eGFR.dbGAP.megaprs.elastic.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch MVP.EUR.eGFR.dbGAP.megaprs.elastic.pred.jackknife.sh

```


### Step 4 4, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

#prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch MVP.EUR.HDL.gwas.dbGAP.megaprs.elastic.pred.jackknife.sh

```


### Step 4 5, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/SBP_MVP_White.results.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/SBP_MVP_White.results.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/SBP_MVP_White.results.megaprs.elastic.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/SBP_MVP_White.results.megaprs.elastic.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch SBP_MVP_White.results.megaprs.elastic.pred.jackknife.sh

```


### Step 4 6, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/elastic/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.pred.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/elastic/
sbatch MVP.T2D.EUR.MAF001.dbGaP.checked.megaprs.elastic.pred.jackknife.sh

```



## LDpred2 4 HDL 

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/LDpred2_2.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker29.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/MVP.EUR.HDL.gwas.dbGAP.ldpred2 --ss_type MVP

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/MVP.EUR.HDL.gwas.dbGAP.ldpred2.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/
sbatch MVP.EUR.HDL.gwas.dbGAP.ldpred2.sh

```

### Step 4, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

#prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/MVP.EUR.HDL.gwas.dbGAP.ldpred2.prs.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/MVP.EUR.HDL.gwas.dbGAP.ldpred2.prs --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/MVP.EUR.HDL.gwas.dbGAP.ldpred2.prs.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/
sbatch MVP.EUR.HDL.gwas.dbGAP.ldpred2.prs.jackknife.sh

```



## LDpred2 4 SBP 

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/LDpred2_2.R --pheno /home/lezh/snpher/faststorage/biobank/phenotypes/sbp.clean  --sumstats /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/SBP_MVP_White.results.ldpred2 --ss_type MVP

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/SBP_MVP_White.results.ldpred2.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/
sbatch SBP_MVP_White.results.ldpred2.sh

```

### Step 4, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/ldpred2/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.ldpred2.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/ldpred2/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.ldpred2.prs --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/ldpred2/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.ldpred2.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/ldpred2/
sbatch daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.ldpred2.jackknife.sh

```



## LDpred2 4 T2D 
triglycerides
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/LDpred2_2.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker19.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ldpred2 --ss_type MVP

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ldpred2.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/
sbatch MVP.T2D.EUR.MAF001.dbGaP.checked.rsids.ldpred2.sh

```

### Step 4, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

#prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB.megaprs.elastic.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/MVP.EUR.HDL.gwas.dbGAP.ldpred2.prs.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/ldpred2/MVP.EUR.HDL.gwas.dbGAP.ldpred2.prs --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/MVP.EUR.HDL.gwas.dbGAP.ldpred2.prs.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/mvp_ukbb_prs/scripts/ldpred2/
sbatch MVP.EUR.HDL.gwas.dbGAP.ldpred2.prs.jackknife.sh

```


