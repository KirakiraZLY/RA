# Commands during RA
# Week8

1/31/2024




## Mega PRS New

### Step 1 有了不用跑，直接调用
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh


shuf -n 5000 /home/lezh/dsmwpred/data/ukbb/geno3.fam > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/rand_geno3.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/rand_geno3.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --genefile /home/lezh/snpher/faststorage/highld.txt


" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/step1.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/
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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new/model/finngen_R10_${linenamecleaned}.megaprs.new --allow-ambiguous YES --cors /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/cors_geno3 --high-LD /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/highld_geno3/genes.predictors.used --summary /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak --model bayesr --power -.25 --max-threads 4  --extract /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak 

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
for j in {1..551}; do
echo $j
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred --power 0 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --scorefile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/finngen_R10_${linenamecleaned}.megaprs.new.effects  

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.sh

# I am doing blabla

cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/

done

```

```python

for j in {1..551}; do
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
sbatch finngen_R10_${linenamecleaned}.sh

done


```

### Step 4, jackknife
/home/doug/ldak5.2.linux --jackknife test.asthma.bayesr --profile test.asthma.bayesr.profile --num-blocks 200 --AUC YES --prevalence 0.02

```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do

linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')


echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 16:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

while IFS= read -r path2; do

/home/lezh/snpher/faststorage/ldak5.2.linux --jackknife /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleanedscore} --profile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleanedscore} --num-blocks 200 --AUC YES --prevalence 0.02  --pheno $path2

done < "/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_to_copy.txt"

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleaned}.sh

# I am doing blabla
cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife
sbatch finngen_R10_${linenamecleaned}.sh

done


```


### Step 4, my jackknife
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do
echo $j
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/jackknife_onecolumn_and_theothers.R --scoreFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife  --phenoFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/ukbb_phenotype_948_all.pheno

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife.sh

# I am doing blabla

cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/
sbatch finngen_R10_${linenamecleaned}.megaprs.new.jackknife.sh

done


```

### Combine all traits of UKBB into one table
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_test.txt
```python

conda activate zly2
Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ukbb_icd10_combine.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_to_copy.txt  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/ukbb_phenotype_948_all.pheno  --bfile /home/lezh/dsmwpred/data/ukbb/geno3


```

### Combine all PRS of MegaPRS into one table
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do

linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo $j $linenamecleaned

awk '{print $5}' "/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile" > "/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_${linenamecleaned}.txt"

done
paste /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_*.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/megaprs_new_pred_merged.txt

rm /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_*.txt


```

### Run correlation: one Phenotype with multiple FinnGen ss
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/jackknife_one_ukbb_multiple_finngen.R

" > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/pheno_to_finngen.jackknife.sh

# I am doing blabla

cd /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/
sbatch pheno_to_finngen.jackknife.sh


```