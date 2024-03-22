# Commands during RA
## Week 15

3/15/2024


# UKBB GWAS
Divided into train and test sets.   
cov: /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars   
cov without label: /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars   
bfile: /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3    
pheno: /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno   

## geno3 -> .bgen

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/plink2 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --export bgen-1.2 --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/geno3

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_to_bgen.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_to_bgen.sh

```
## Pheno adding label
```python
for file in /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/*; do
    echo ${file}
    if [ -f "$file" ]; then  # 检查是否是文件
        filename=$(basename -- "$file")  # 提取文件名
        extension="${filename##*.}"  # 提取文件扩展名
        filename_no_ext="${filename%.*}"  # 提取文件名（不包含扩展名）

        # 创建新文件名
        new_filename="$filename_no_ext.label.$extension"

        # 在新文件中添加 "FID IID Phenotype" 作为第一行
        echo "FID IID Phenotype" > "$new_filename"

        # 将旧文件内容追加到新文件中
        cat "$file" >> "$new_filename"
    fi
done

```

## 1 snoring
### Regenie snoring
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_snoring_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_snoring_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_snoring_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_snoring_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_snoring_regenie.sh

```

### LDAK run snoring
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_snoring_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_snoring_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_snoring_ldak.sh
```


## 2 sbp
### Regenie sbp
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_sbp_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_sbp_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_sbp_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_sbp_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_sbp_regenie.sh

```

### LDAK run sbp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_sbp_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_sbp_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_sbp_ldak.sh
```


## 3 reaction
### Regenie reaction
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_reaction_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_reaction_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_reaction_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_reaction_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_reaction_regenie.sh

```

### LDAK run reaction
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_reaction_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_reaction_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_reaction_ldak.sh
```


## 4 quals
### Regenie quals
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_quals_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_quals_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_quals_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_quals_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_quals_regenie.sh

```

### LDAK run quals
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_quals_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_quals_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_quals_ldak.sh
```


## 5 pulse
### Regenie pulse
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_pulse_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_pulse_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_pulse_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_pulse_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_pulse_regenie.sh

```

### LDAK run pulse
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_pulse_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_pulse_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_pulse_ldak.sh
```


## 6 neur 
### Regenie neur
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_neur_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_neur_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_neur_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_neur_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_neur_regenie.sh

```
### LDAK run neur
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_neur_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_neur_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_neur_ldak.sh
```



## 7 imp
### Regenie imp
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_imp_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_imp_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_imp_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_imp_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_imp_regenie.sh

```

### LDAK run imp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_imp_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_imp_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_imp_ldak.sh
```


## 8 hyper
### Regenie hyper
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_hyper_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_hyper_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_hyper_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_hyper_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_hyper_regenie.sh

```
### LDAK run hyper
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_hyper_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_hyper_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_hyper_ldak.sh
```



## 9 height
### Regenie height
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_height_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_height_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_height_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_height_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_height_regenie.sh

```

### LDAK run height
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_height_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_height_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_height_ldak.sh
```


## 10 fvc
### Regenie fvc
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_fvc_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_fvc_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_fvc_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_fvc_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_fvc_regenie.sh

```

### LDAK run fvc
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_fvc_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_fvc_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_fvc_ldak.sh
```


## 11 ever
### Regenie ever
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_ever_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_ever_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_ever_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_ever_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_ever_regenie.sh

```

### LDAK run ever
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_ever_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_ever_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_ever_ldak.sh
```


## 12 chron
### Regenie chron
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_chron_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_chron_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_chron_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_chron_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_chron_regenie.sh

```
### LDAK run chron
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_chron_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_chron_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_chron_ldak.sh
```



## 13 bmi
### Regenie bmi
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_bmi_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_bmi_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_bmi_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_bmi_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_bmi_regenie.sh

```

### LDAK run bmi
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_bmi_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_bmi_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_bmi_ldak.sh
```




## 14 awake
### Regenie awake
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate regenie_env

regenie \
  --step 1 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_awake_regenie_step1  


regenie \
  --step 2 \
  --bed /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 \
  --phenoFile /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.train \
  --covarFile /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars \
  --covarColList SEX,PC{1:10} \
  --bsize 1000 \
  --threads 4 \
  --qt \
  --pThresh 0.01 \
  --pred /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step1/geno3_awake_regenie_step1_pred.list \
  --out /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_awake_regenie

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_awake_regenie.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_awake_regenie.sh

```

### LDAK run awake
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.train  --covar /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_awake_ldak.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_awake_ldak.sh
```








# PRS on 14 UKBB
## GWAS -> ldak formatting
LDAK GWAS has it automatically
Only format Regenie

conda activate zly2

### 1. snoring
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_snoring_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_snoring_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_snoring_regenie_Phenotype.formatting.sh


```

### 2. sbp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_sbp_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_sbp_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_sbp_regenie_Phenotype.formatting.sh


```
### 3. reaction
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_reaction_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.prscs.ss
 
awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_reaction_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_reaction_regenie_Phenotype.formatting.sh


```
### 4. quals
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_quals_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_quals_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_quals_regenie_Phenotype.formatting.sh


```
### 5. pulse
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_pulse_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_pulse_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_pulse_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_pulse_regenie_Phenotype.formatting.sh


```
### 6. neur
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_neur_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_neur_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_neur_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_neur_regenie_Phenotype.formatting.sh


```
### 7. imp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_imp_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_imp_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_imp_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_imp_regenie_Phenotype.formatting.sh


```
### 8. hyper
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_hyper_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_hyper_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_hyper_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_hyper_regenie_Phenotype.formatting.sh


```
### 9. height
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_height_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_height_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_height_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_height_regenie_Phenotype.formatting.sh


```
### 10. fvc
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_fvc_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_fvc_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_fvc_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_fvc_regenie_Phenotype.formatting.sh


```
### 11. ever
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_ever_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_ever_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_ever_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_ever_regenie_Phenotype.formatting.sh


```
### 12. chron
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_chron_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_chron_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_chron_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_chron_regenie_Phenotype.formatting.sh


```
### 13. bmi
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_bmi_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_bmi_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_bmi_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_bmi_regenie_Phenotype.formatting.sh


```
### 14. awake
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/regenie_step2/geno3_awake_regenie_Phenotype.regenie  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3  

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.prscs.ss

awk '{print $2, $4, $5, $8, $7}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.assoc > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_awake_regenie_Phenotype.formatting.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/
sbatch geno3_awake_regenie_Phenotype.formatting.sh


```




## Megaprs Bayesr

### 1. snoring
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_snoring_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_snoring_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_snoring_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_snoring_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_snoring_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_snoring_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_sbp_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_sbp_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_sbp_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_sbp_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_sbp_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_sbp_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_reaction_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_reaction_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_reaction_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_reaction_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_reaction_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_reaction_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_quals_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_quals_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_quals_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_quals_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_quals_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_quals_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_pulse_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_pulse_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_pulse_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_pulse_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_pulse_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_pulse_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_neur_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_neur_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_neur_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_neur_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_neur_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_neur_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_imp_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_imp_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_imp_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_imp_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_imp_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_imp_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_hyper_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_hyper_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_hyper_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_hyper_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_hyper_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_hyper_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_height_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_height_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_height_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_height_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_height_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_height_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_fvc_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_fvc_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_fvc_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_fvc_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_fvc_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_fvc_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_ever_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_ever_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_ever_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_ever_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_ever_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_ever_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_chron_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_chron_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_chron_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_chron_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_chron_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_chron_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_bmi_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_bmi_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_bmi_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_bmi_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_bmi_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_bmi_ldak.megaprs.bayesr.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_awake_regenie.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_awake_regenie.megaprs.bayesr.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.summaries --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.bayesr.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.bayesr.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_awake_ldak.megaprs.bayesr.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_awake_ldak.megaprs.bayesr.sh

```


## Megaprs elastic

### 1. snoring
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_snoring_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_snoring_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_snoring_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_snoring_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_snoring_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_snoring_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_snoring_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_sbp_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_sbp_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_sbp_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_sbp_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_sbp_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_sbp_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_sbp_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_reaction_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_reaction_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_reaction_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_reaction_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_reaction_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_reaction_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_reaction_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_quals_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_quals_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_quals_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_quals_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_quals_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_quals_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_quals_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_pulse_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_pulse_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_pulse_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_pulse_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_pulse_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_pulse_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_pulse_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_neur_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_neur_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_neur_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_neur_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_neur_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_neur_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_neur_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_imp_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_imp_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_imp_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_imp_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_imp_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_imp_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_imp_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_hyper_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_hyper_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_hyper_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_hyper_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_hyper_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_hyper_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_hyper_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_height_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_height_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_height_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_height_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_height_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_height_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_height_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_fvc_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_fvc_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_fvc_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_fvc_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_fvc_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_fvc_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_fvc_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_ever_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_ever_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_ever_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_ever_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_ever_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_ever_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_ever_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_chron_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_chron_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_chron_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_chron_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_chron_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_chron_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_chron_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_bmi_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_bmi_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_bmi_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_bmi_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_bmi_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_bmi_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_bmi_ldak.megaprs.elastic.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_regenie.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_awake_regenie.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_awake_regenie.megaprs.elastic.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.summaries --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ldak/geno3_awake_ldak.summaries


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.elastic.effects  --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/geno3_awake_ldak.megaprs.elastic.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/geno3_awake_ldak.megaprs.elastic.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/
sbatch geno3_awake_ldak.megaprs.elastic.sh

```



# PRS CS test
## PRS beta
```python

dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results_pst*

awk '{print $2, $4, $5, "NA", $6}' /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

```




# PRS CS 
### Make bed
```python
/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --make-bed /faststorage/project/dsmwpred/zly/RA/data/geno3_test --extract 
```

### 1. snoring
#### Regenie
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_snoring_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_snoring_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_snoring_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_snoring_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_snoring_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_snoring_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_sbp_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_sbp_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_sbp_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_sbp_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_sbp_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_sbp_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_reaction_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_reaction_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_reaction_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_reaction_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_reaction_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_reaction_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_quals_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_quals_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_quals_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_quals_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_quals_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_quals_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_pulse_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_pulse_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_pulse_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_pulse_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_pulse_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_pulse_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_neur_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_neur_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_neur_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_neur_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_neur_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_neur_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_imp_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_imp_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_imp_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_imp_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_imp_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_imp_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_hyper_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_hyper_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_hyper_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_hyper_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_hyper_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_hyper_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_height_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_height_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3


python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_height_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_height_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_height_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_height_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_fvc_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_fvc_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_fvc_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_fvc_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_fvc_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_fvc_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_ever_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_ever_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_ever_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_ever_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_ever_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_ever_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_chron_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_chron_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_chron_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_chron_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_chron_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_chron_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_bmi_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_bmi_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_bmi_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.combined.effect

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_bmi_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_bmi_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_bmi_ldak.prscs.sh

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
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_regenie_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_regenie_Phenotype.prscs.results.pred.profile  --num-blocks 200

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_awake_regenie.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_awake_regenie.prscs.sh

```


#### LDAK
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno3_awake_ldak_Phenotype.prscs.ss --n_gwas=200000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results

cat /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results* >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.combined

mv /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.combined.1 /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results_pst*

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.combined.effect   --max-threads 4  --pheno /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.test

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/prs_cs_results/geno3_awake_ldak_Phenotype.prscs.results.pred.profile  --num-blocks 200


" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/geno3_awake_ldak.prscs.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/ukbb_prs/scripts/prs_cs_results/
sbatch geno3_awake_ldak.prscs.sh

```

