# Commands during RA
## Week 16

## Missing values

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/eur/EUR.QC --geno 0 --mind 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/eur/EUR.QC



/faststorage/project/dsmwpred/zly/software/plink  --make-bed --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4  --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4_30wan.snplist  --out  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4_30wan


## UKBB test

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
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



# UKBB

## Regenie

### 1. snoring
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_snoring_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_snoring_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_snoring_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_snoring_regenie_Phenotype.ldpred.inf.sh

```

### 2. sbp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_sbp_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_sbp_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_sbp_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_sbp_regenie_Phenotype.ldpred.inf.sh

```
### 3. reaction
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_reaction_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_reaction_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_reaction_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_reaction_regenie_Phenotype.ldpred.inf.sh

```
### 4. quals
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_quals_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_quals_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_quals_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_quals_regenie_Phenotype.ldpred.inf.sh

```
### 5. pulse
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_pulse_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_pulse_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_pulse_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_pulse_regenie_Phenotype.ldpred.inf.sh

```
### 6. neur
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_neur_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_neur_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_neur_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_neur_regenie_Phenotype.ldpred.inf.sh

```
### 7. imp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_imp_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_imp_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_imp_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_imp_regenie_Phenotype.ldpred.inf.sh

```
### 8. hyper
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_hyper_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_hyper_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_hyper_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_hyper_regenie_Phenotype.ldpred.inf.sh

```
### 9. height
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
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
### 10. fvc
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_fvc_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_fvc_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_fvc_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_fvc_regenie_Phenotype.ldpred.inf.sh

```
### 11. ever
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_ever_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_ever_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_ever_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_ever_regenie_Phenotype.ldpred.inf.sh

```
### 12. chron
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_chron_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_chron_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_chron_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_chron_regenie_Phenotype.ldpred.inf.sh

```
### 13. bmi
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_bmi_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_bmi_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_bmi_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_bmi_regenie_Phenotype.ldpred.inf.sh

```
### 14. awake
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_awake_regenie_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_awake_regenie_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_awake_regenie_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_awake_regenie_Phenotype.ldpred.inf.sh

```

## LDAK assoc -> .ldak
### 14
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_awake_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_awake_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000

### 13 bmi
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_bmi_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_bmi_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000

### 12 chron
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_chron_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_chron_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000

### 11 ever
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_ever_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_ever_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000

### 10 fvc
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_fvc_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_fvc_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000

### 9 height
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_height_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


### 8 hyper
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_hyper_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_hyper_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


### 7 imp
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_imp_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_imp_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


### 6 neur
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_neur_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_neur_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


### 5 pulse
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_pulse_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_pulse_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


### 4 quals
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_quals_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_quals_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


### 3 reaction
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_reaction_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_reaction_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


### 2 sbp
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_sbp_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_sbp_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


### 1 snoring
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno4_snoring_ldak.assoc  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_snoring_ldak_Phenotype  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  --N 200000


## LDAK

### 1. snoring
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_snoring_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_snoring_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_snoring_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_snoring_ldak_Phenotype.ldpred.inf.sh

```

### 2. sbp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_sbp_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_sbp_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_sbp_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_sbp_ldak_Phenotype.ldpred.inf.sh

```
### 3. reaction
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_reaction_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_reaction_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_reaction_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_reaction_ldak_Phenotype.ldpred.inf.sh

```
### 4. quals
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_quals_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_quals_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_quals_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_quals_ldak_Phenotype.ldpred.inf.sh

```
### 5. pulse
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_pulse_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_pulse_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_pulse_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_pulse_ldak_Phenotype.ldpred.inf.sh

```
### 6. neur
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_neur_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_neur_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_neur_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_neur_ldak_Phenotype.ldpred.inf.sh

```
### 7. imp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_imp_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_imp_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_imp_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_imp_ldak_Phenotype.ldpred.inf.sh

```
### 8. hyper
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_hyper_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_hyper_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_hyper_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_hyper_ldak_Phenotype.ldpred.inf.sh

```
### 9. height
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_height_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_height_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_height_ldak_Phenotype.ldpred.inf.sh

```
### 10. fvc
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_fvc_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_fvc_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_fvc_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_fvc_ldak_Phenotype.ldpred.inf.sh

```
### 11. ever
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_ever_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_ever_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_ever_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_ever_ldak_Phenotype.ldpred.inf.sh

```
### 12. chron
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_chron_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_chron_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_chron_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_chron_ldak_Phenotype.ldpred.inf.sh

```
### 13. bmi
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_bmi_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_bmi_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_bmi_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_bmi_ldak_Phenotype.ldpred.inf.sh

```
### 14. bmi
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_awake_ldak_Phenotype.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/ukbb/geno4_awake_ldak_Phenotype.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/geno4_awake_ldak_Phenotype.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch geno4_awake_ldak_Phenotype.ldpred.inf.sh

```



# PGC
## BIP
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/BIP_F31.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/daner_bip_pgc3_nm_noukbiobank.geno4.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/daner_bip_pgc3_nm_noukbiobank.geno4.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/pgc_daner_bip_pgc3_nm_noukbiobank.geno4.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch pgc_daner_bip_pgc3_nm_noukbiobank.geno4.ldpred.inf.sh

```



## SCZ
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/SCZ_F20.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno4.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno4.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno4.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno4.ldpred.inf.sh

```


## MDD
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

# /faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4 --geno 0 --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/geno4_nomissing

# Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 
Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/MDD_F32.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/pgc/PGC_UKB_depression_genome-wide.geno4.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/PGC_UKB_depression_genome-wide.geno4.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/PGC_UKB_depression_genome-wide.geno4.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch PGC_UKB_depression_genome-wide.geno4.ldpred.inf.sh

```

## Step 4 Jackknife

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/daner_bip_pgc3_nm_noukbiobank.geno4.ldpred.inf.prs)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/daner_bip_pgc3_nm_noukbiobank.geno4.ldpred.inf.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/daner_bip_pgc3_nm_noukbiobank.geno4.ldpred.inf.prs  --num-blocks 200 --AUC YES --prevalence ${prev}

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno4.ldpred.inf.prs)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno4.ldpred.inf.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/PGC3_SCZ_wave3.european.autosome.public.v3.vcf.geno4.ldpred.inf.prs  --num-blocks 200 --AUC YES --prevalence ${prev}

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/PGC_UKB_depression_genome-wide.geno4.ldpred.inf.prs)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/PGC_UKB_depression_genome-wide.geno4.ldpred.inf.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/pgc/PGC_UKB_depression_genome-wide.geno4.ldpred.inf.prs  --num-blocks 200 --AUC YES --prevalence ${prev}



















































# MVP

## HDL

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker29.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/mvp/MVP.EUR.HDL.gwas.dbGAP.geno4.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/MVP.EUR.HDL.gwas.dbGAP.geno4.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch MVP.EUR.HDL.gwas.dbGAP.geno4.ldpred.inf.sh

```


## SBP

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /home/lezh/snpher/faststorage/biobank/phenotypes/sbp.clean  --sumstats /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/SBP_MVP_White.results.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/mvp/SBP_MVP_White.results.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/SBP_MVP_White.results.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch SBP_MVP_White.results.ldpred.inf.sh

```

## T2D


```python

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker19.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno4.ss.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/mvp/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno4.ss.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno4.ss.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno4.ss.ldpred.inf.sh

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



```python

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_first_step.R
 

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_inf.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code2356.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/finngen/finngen_R10_T2D_WIDE.ldpred.inf --ss_type ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/finngen_R10_T2D_WIDE.ldpred.inf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch finngen_R10_T2D_WIDE.ldpred.inf.sh


```






echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/LDpred2_auto.R

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/TEST.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ldpred2/output/scripts/
sbatch TEST.sh

