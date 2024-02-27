# Commands during RA
## Week 12

2/25/2024

# Get Japan genotype

```python

#########

#find a few snps and check maf - note that finnish pop have names starting with 12_

#get finnish individuals



echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 64:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

grep ^"18_" /faststorage/project/dsmwpred/doug/leyi/hrc.fam > /faststorage/project/dsmwpred/zly/RA/data/33KG/japan/jap.keep

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/doug/leyi/hrc --allow-no-sex --make-bed  --keep /faststorage/project/dsmwpred/zly/RA/data/33KG/japan/jap.keep  --out /faststorage/project/dsmwpred/zly/RA/data/33KG/japan/hrc_geno_jap


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/hrc_geno_jap.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch hrc_geno_jap.sh

```


# MVP

## download
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

wget -i /faststorage/project/dsmwpred/zly/RA/data/mvp/links.txt

" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/hrc_geno_jap.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch hrc_geno_jap.sh

```


# LDpred2 on FinnGen 2409 SS

## hg19 add n
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

for j in {1..2409}; do
#for j in {1..1}; do
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
echo $j ${linenamecleaned}

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 3:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/finngen_ss_add_n.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19/finngen_R10_${linenamecleaned}.hg19  --fileName  ${linenamecleaned}  --outputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19_addn/finngen_R10_${linenamecleaned}.hg19.addn

echo $j ${linenamecleaned}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/hg19_addn/finngen_R10_${linenamecleaned}.hg19.addn.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/hg19_addn/
sbatch finngen_R10_${linenamecleaned}.hg19.addn.sh

done


```

## Make Bed
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 100:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_readbed.R

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/readbed_fin.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2
sbatch readbed_fin.sh


```

## PCA on finngen

```python
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/plink \
  --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/fin/hrc_geno_fin \
  --double-id --allow-extra-chr \
  --set-missing-var-ids @:# \
  --pca 6 \
  --out /faststorage/project/dsmwpred/zly/RA/data/33KG/fin/hrc_geno_fin   

" > /faststorage/project/dsmwpred/zly/RA/data/33KG/fin/fin_pca.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/fin/
sbatch fin_pca.sh
```

## Try with height
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/height.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19/finngen_R10_HEIGHT_IRN.hg19  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/result/finngen_R10_HEIGHT_IRN.r2

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/finngen_R10_HEIGHT_IRN_ldpred2.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/
sbatch finngen_R10_HEIGHT_IRN_ldpred2.sh


```


# Lassosum on FinnGen 2409

## Try with height
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/lassosum.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/height.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19/finngen_R10_HEIGHT_IRN.hg19  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/result/finngen_R10_HEIGHT_IRN.r2  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/geno3_nomissing

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/script/finngen_R10_HEIGHT_IRN_lasso.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/script/
sbatch finngen_R10_HEIGHT_IRN_lasso.sh


```