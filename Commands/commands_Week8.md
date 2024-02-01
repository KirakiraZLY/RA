# Commands during RA
# Week8

1/22/2024


# 33KG with 1000 Genome
## MAF comparison
### 33KG MAF
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1 --freq --out /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_maf


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/33kg_geno_fin_1_maf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch 33kg_geno_fin_1_maf.sh

```


### 1000G MAF
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/1KG/1000G.99FIN.rs --freq --out /faststorage/project/dsmwpred/zly/RA/data/33KG/1000g99fin_maf


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/1000g99fin_maf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch 1000g99fin_maf.sh

```


## ggplot

```python
conda activate zly2
R
```

```python
library(tidyverse)

print("Data Loading")
df <- read_table("/faststorage/project/dsmwpred/zly/RA/data/33KG/maf_frq/33kg_geno_fin_1_maf.frq")
df_sampled <- df[sample(nrow(df), 10000, replace = FALSE), ]

print("Plotting")
p <- ggplot(df_sampled, aes(x = SNP, y = MAF)) +
  geom_point() +
  labs(title = "Minor Allele Frequency (MAF) for SNPs",
       x = "SNP ID",
       y = "MAF") +
  theme_minimal()

print("Data Saving")
ggsave("/faststorage/project/dsmwpred/zly/RA/data/33KG/maf_frq/33kg_geno_fin_1_maf_plot.png", plot = p)
```

### Run MAF.R
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/data/33KG/maf_frq/MAF.R


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/maf_plot.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch maf_plot.sh

```

### Run MAF_compar.R
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/data/33KG/maf_frq/MAF_compar.R


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/maf_plot.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch maf_plot.sh

```

### update 33kg_geno_fin_1_qc that deletes inconsistent alleles
Exclude inconsistent alleles and inner join with geno3

```python


echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh


/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_qc --extract /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_qc_snps_to_delete.txt  --geno 0.1 --mind 0.1 --maf 0.05 --mac 100  --make-bed --out /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_qc_geno3 

" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/plink_delete_inconsistent.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch plink_delete_inconsistent.sh


```


# fg ukbb
## MegaPRS_new
### Step 1 有了不用跑，直接调用
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

shuf -n 5000 /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_qc_geno3.fam > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/rand_33kg_geno_fin_1_qc.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/cors_33kg_geno_fin_1_qc --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_qc_geno3 --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/rand_33kg_geno_fin_1_qc.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/highld_33kg_geno_fin_1_qc --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_qc_geno3 --genefile /home/lezh/snpher/faststorage/highld.txt --max-threads 4 

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/step1.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/
sbatch step1.sh


```


### Step 2 Make Model
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..2409}; do
#for j in {1..20}; do
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
echo $j ${linenamecleaned}

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/model/finngen_R10_${linenamecleaned}.megaprs.new --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/cors_33kg_geno_fin_1_qc --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/highld_33kg_geno_fin_1_qc/genes.predictors.used --summary /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak --model bayesr --power -.25 --max-threads 4  --extract /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak 

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/model/finngen_R10_${linenamecleaned}.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/model/
sbatch finngen_R10_${linenamecleaned}.sh

done


```


### Step 3 Predicting, without checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..2409}; do
echo $j
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/model/finngen_R10_${linenamecleaned}.megaprs.new.effects  --max-threads 4

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/finngen_R10_${linenamecleaned}.prediction.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/
sbatch finngen_R10_${linenamecleaned}.prediction.sh
done

```



### Step 3.5 Combine profile and phenotype
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..281}; do

#for j in {1..1}; do
echo $j
my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
#echo ${my_variable}
#done
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)


awk 'NR==FNR {a[NR]=$3; next} FNR>1 {if ((FNR-1) in a) $3=a[FNR-1]} 1' /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code${my_variable}.pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/combine/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile.combined

done


```


### Step 4, LDAK jackknife
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..281}; do
#for j in {1..5}; do
echo $j
my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
#echo ${my_variable}
#done
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/combine/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile.combined --num-blocks 200 --AUC YES --prevalence 0.02

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/jackknife/
sbatch finngen_R10_${linenamecleaned}.megaprs.new.jackknife.sh

done

```


# MegaPRS SS Demo

## Make a 1000 SNP plink file
```python

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --extract /faststorage/project/dsmwpred/zly/RA/MegaPRS_demo/ss/finngen_R10_Z21_TOBAC_USE.ldak.1ksubset.rsid  --make-bed --out /faststorage/project/dsmwpred/zly/RA/MegaPRS_demo/ss/geno3_1000

```






























# Mega PRS New on FinnGen and UKBB, with geno3 as Reference Panel

### Make bed geno3
```python

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_bim_to_remain.txt  --make-bed --out /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3

```

### Step 1 有了不用跑，直接调用
```python
shuf -n 5000 /home/lezh/dsmwpred/data/ukbb/geno3.fam > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/rand_geno3.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/rand_geno3.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --genefile /home/lezh/snpher/faststorage/highld.txt


```
### Step 2 Make Model
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
#for j in {1..2409}; do
for j in {1..20}; do
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
echo $j ${linenamecleaned}

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new/model/finngen_R10_${linenamecleaned}.megaprs.new --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak --model bayesr --power -.25 --max-threads 4  --extract /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak 

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new/model/finngen_R10_${linenamecleaned}.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new/model/
sbatch finngen_R10_${linenamecleaned}.sh

done


```


### Step 3 Predicting, without checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..2409}; do
echo $j
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/model/finngen_R10_${linenamecleaned}.megaprs.new.effects  --max-threads 4

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/finngen_R10_${linenamecleaned}.prediction.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/
sbatch finngen_R10_${linenamecleaned}.prediction.sh
done

```



### Step 3.5 Combine profile and phenotype
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..281}; do

#for j in {1..1}; do
echo $j
my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
#echo ${my_variable}
#done
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)


awk 'NR==FNR {a[NR]=$3; next} FNR>1 {if ((FNR-1) in a) $3=a[FNR-1]} 1' /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code${my_variable}.pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/combine/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile.combined

done


```


### Step 4, LDAK jackknife
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..281}; do
#for j in {1..5}; do
echo $j
my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
#echo ${my_variable}
#done
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/prediction/combine/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile.combined --num-blocks 200 --AUC YES --prevalence 0.02

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/jackknife/
sbatch finngen_R10_${linenamecleaned}.megaprs.new.jackknife.sh

done

```