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


# PGC ldak format
## Make PGC schiz by /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R
```python

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.tsv  --outputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.tsv.ldak  --bfile /home/lezh/dsmwpred/data/ukbb/geno3  

```

## Make PGC MDD by /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R
### N = 500199
```python

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC_UKB_depression_genome-wide.txt  --outputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC_UKB_depression_genome-wide.txt.ldak  --bfile /home/lezh/dsmwpred/data/ukbb/geno3  --N 500199

```


# PGC PRS
## SCZ by Megaprs Bayesr
### Step 2 Make Model
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.tsv.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.tsv.ldak 

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/step2_PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/
sbatch step2_PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.sh

```


### Step 3 Predicting, with checking
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

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/SCZ_F20.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/step3_PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/
sbatch step3_PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.sh

```


### Step 3.5 Combine profile and phenotype
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/profile_combine.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/SCZ_F20.pheno --prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile --outputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile.combined

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile.combined.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/
sbatch PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile.combined.sh

```


### Step 4, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile  --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_bayesr/
sbatch PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.jackknife.sh

```



## By Elastic Net

### Step 2 Make Model
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.tsv.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.tsv.ldak 

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_elastic/step2_PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_elastic/
sbatch step2_PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.sh

```


### Step 3 Predicting, with checking
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

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/SCZ_F20.pheno

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_elastic/step3_PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_elastic/
sbatch step3_PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.sh

```



### Step 3.5 Combine profile and phenotype
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/profile_combine.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/SCZ_F20.pheno --prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile --outputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile.combined

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile.combined.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_elastic/
sbatch PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile.combined.sh

```


### Step 4, LDAK jackknife
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.pred.profile --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_elastic/PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/megaprs_elastic/
sbatch PGC3_SCZ_wave3.european.autosome.megaprs.bayesr.jackknife.sh

```



## SCZ, By LDpred2

conda activate zly2   
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/ldpred2/LDpred2_1.R

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/ldpred2/LDpred2_2.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/SCZ_F20.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.tsv  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/ldpred2/PGC3_SCZ_wave3.european.autosome.ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/ldpred2/PGC3_SCZ_wave3.european.autosome.ldpred2

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pgc_ukbb_prs/scripts/ldpred2/
sbatch PGC3_SCZ_wave3.european.autosome.ldpred2

```