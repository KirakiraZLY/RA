# Commands during RA
## Week 15

3/15/2024


# UKBB GWAS
Divided into train and test sets
cov: /faststorage/project/dsmwpred/zly/RA/data/geno.sex.townsend.age.pcs_label.covars
bfile: /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 
pheno: /faststorage/project/dsmwpred/data/ukbb

## 1 snoring

## 2 sbp

## 3 reaction

## 4 quals

## 5 pulse

## 6 neur 

## imp

## hyper

## height

## fvc

## ever

## chron

## bmi
### Bolt bmi
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"


source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/BOLT-LMM_v2.4/bolt --bfile=${dir}/data_White --phenoFile=${dir}/Phenotype_UKBB/bmi_label.pheno  --phenoCol=Phenotype  --covarFile=${dir}/covar_White_PC_10.covars --qCovarCol=Paternal --qCovarCol=Sex --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=${dir}/Real_Traits/bmi/data_White_Bolt_bmi

" > ${dir}/scripts/Real_Traits/bmi/data_White_Bolt_bmi


# I am doing blabla
cd ${dir}/scripts/Real_Traits/bmi/

sbatch data_White_Bolt_bmi
```




## awake


