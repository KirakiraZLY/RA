# Commands during RA
## Week 15

3/15/2024


# UKBB GWAS
Divided into train and test sets.   
cov: /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars   
cov without label: /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs.covars   
bfile: /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3    
pheno: /faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno   

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
### Bolt snoring
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/snoring.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_snoring_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_snoring_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_snoring_bolt.sh
```

## 2 sbp
### Bolt sbp
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/sbp.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_sbp_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_sbp_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_sbp_bolt.sh
```

## 3 reaction
### Bolt reaction
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/reaction.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_reaction_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_reaction_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_reaction_bolt.sh
```

## 4 quals
### Bolt quals
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/quals.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_quals_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_quals_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_quals_bolt.sh
```

## 5 pulse
### Bolt pulse
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/pulse.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_pulse_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_pulse_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_pulse_bolt.sh
```

## 6 neur 
### Bolt neur
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/neur.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_neur_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_neur_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_neur_bolt.sh
```

## 7 imp
### Bolt imp
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/imp.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_imp_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_imp_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_imp_bolt.sh
```

## 8 hyper
### Bolt hyper
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/hyper.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_hyper_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_hyper_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_hyper_bolt.sh
```

## 9 height
### Bolt height
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_height_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_height_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_height_bolt.sh
```

## 10 fvc
### Bolt fvc
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/fvc.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_fvc_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_fvc_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_fvc_bolt.sh
```

## 11 ever
### Bolt ever
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/ever.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_ever_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_ever_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_ever_bolt.sh
```

## 12 chron
### Bolt chron
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/chron.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_chron_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_chron_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_chron_bolt.sh
```

## 13 bmi
### Bolt bmi
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/bmi.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_bmi_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_bmi_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_bmi_bolt.sh


```




## 14 awake
### Bolt awake
```python
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/BOLT-LMM_v2.4/bolt --bfile=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --phenoFile=/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/awake.label.train  --phenoCol=Phenotype  --covarFile=/faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=SEX --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/geno3_awake_bolt

" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/geno3_awake_bolt.sh


# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/script/

sbatch geno3_awake_bolt.sh
```

