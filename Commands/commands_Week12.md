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
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/height.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss_liftover/hg19/finngen_R10_HEIGHT_IRN.hg19  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/cor_output/finngen_R10_HEIGHT_IRN.r2

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/scripts/finngen_R10_HEIGHT_IRN_ldpred2.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/scripts/
sbatch finngen_R10_HEIGHT_IRN_ldpred2.sh


```
