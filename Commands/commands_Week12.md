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

## get summary statistics names

grep -oP '(?i)pha.*'  /faststorage/project/dsmwpred/zly/RA/data/mvp/links.txt > /faststorage/project/dsmwpred/zly/RA/data/mvp/mvp_names.txt


## delete first 20 lines
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/faststorage/project/dsmwpred/zly/RA/data/mvp/mvp_names.txt"

total_lines=$(awk 'END {print NR}' /faststorage/project/dsmwpred/zly/RA/data/mvp/mvp_names.txt)

for ((j=1; j<=${total_lines}; j++)); do
#for j in {1..30}; do


my_variable=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/data/mvp/mvp_names.txt)
echo $j ${my_variable} 

tail -n +22 /faststorage/project/dsmwpred/zly/RA/data/mvp/phs001672.${my_variable} > /faststorage/project/dsmwpred/zly/RA/data/mvp/phs001672.${my_variable}.summary

done


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

## Try with height, ldpred2
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_1.R

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_2.R --pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/height.test  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19/finngen_R10_HEIGHT_IRN.hg19  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/result/finngen_R10_HEIGHT_IRN.r2

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/finngen_R10_HEIGHT_IRN_ldpred2.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/
sbatch finngen_R10_HEIGHT_IRN_ldpred2.sh


```

## Try with M13_SACROILIITIS, code156, ldpred2
## Try with one trait
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_1.R

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_2.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code156.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19_addn/finngen_R10_M13_SACROILIITIS.hg19.addn  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/result/finngen_R10_M13_SACROILIITIS.ldpred2.r2.test

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/script/finngen_R10_M13_SACROILIITIS.ldpred2.test.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/script/
sbatch finngen_R10_M13_SACROILIITIS.ldpred2.test.sh


```



## ldpred2 run all 2409
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

total_lines=$(awk 'END {print NR}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

for ((j=1; j<=${total_lines}; j++)); do
#for j in {1..30}; do
echo $j

my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_1.R

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/LDpred2_2.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code${my_variable}.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19_addn/finngen_R10_${linenamecleaned}.hg19.addn  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/result/finngen_R10_${linenamecleaned}.ldpred2

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/script/finngen_R10_${linenamecleaned}.ldpred2.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/script/
sbatch finngen_R10_${linenamecleaned}.ldpred2.sh

done


```


### Step 4, LDAK jackknife
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

total_lines=$(awk 'END {print NR}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

for ((j=1; j<=${total_lines}; j++)); do

#for j in {1..1}; do
echo $j
my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
#echo ${my_variable}
#done
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

# Count proportion of pheno = 1
prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new_elastic/prediction/combine/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.pred.profile.combined)


echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 1:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/jackknife/finngen_R10_${linenamecleaned}.code${my_variable}.ldpred2.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/result/finngen_R10_${linenamecleaned}.ldpred2.prs --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/script/jackknife/finngen_R10_${linenamecleaned}.code${my_variable}.ldpred2.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/script/jackknife/
sbatch finngen_R10_${linenamecleaned}.code${my_variable}.ldpred2.jackknife.sh

done

```




## Results
```
#!/bin/bash

for file in /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/result/*.r2; do
    data=$(awk 'NR==2 {print $1}' "$file")
    echo "${data} ${file}"
done | sort -n -k1,1gr > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/r2_results.txt

```

### Statistic .jack
```python

#!/bin/bash

for file in /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/jackknife/*.jack; do
    data=$(awk 'NR==7 {print $3}' "$file")
    echo "${data} ${file}"
done | sort -n -k1,1gr > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/ldpred2/liability_results.txt


```


# Lassosum on FinnGen 2409

## RUN
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

total_lines=$(awk 'END {print NR}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

#for ((j=1; j<=${total_lines}; j++)); do
for j in {1..30}; do
echo $j

my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/lassosum.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code${my_variable}.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/hg19_addn/finngen_R10_${linenamecleaned}.hg19.addn  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/result/finngen_R10_${linenamecleaned}.lassosum  --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/geno3_nomissing

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/script/finngen_R10_${linenamecleaned}.lassosum.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/script/
sbatch finngen_R10_${linenamecleaned}.lassosum.sh

done

```

## Results
```
#!/bin/bash

for file in /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/result/*.r2; do
    data=$(awk 'NR==2 {print $1}' "$file")
    echo "${data} ${file}"
done | sort -n -k1,1gr > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/lassosum/r2_results.txt

```


# Result visualization of 4 PRS tools

```python
conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/res_vis.R

```






# Step 4, LDAK jackknife, MegaPRS
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

total_lines=$(awk 'END {print NR}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

for ((j=1; j<=${total_lines}; j++)); do

#for j in {1..1}; do
echo $j
my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
#echo ${my_variable}
#done
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

# Count proportion of pheno = 1
prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new/prediction/combine/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.pred.profile.combined)


echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 1:0:0
#SBATCH -c 1
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new/jackknife/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new/prediction/combine/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.pred.profile.combined --num-blocks 200 --AUC YES --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new/jackknife/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new/jackknife
sbatch finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.jackknife.sh

done

```

