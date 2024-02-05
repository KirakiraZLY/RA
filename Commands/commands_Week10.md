# Commands during RA
# Week10

2/5/2024


# Megaprs New Elastic


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

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new_elastic/model/finngen_R10_${linenamecleaned}.megaprs.new --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/cors_geno3 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/highld_geno3/genes.predictors.used --summary /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak --model elastic --power -.25 --max-threads 4  --extract /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak 

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new_elastic/model/finngen_R10_${linenamecleaned}.sh

# I am doing blabla 
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new_elastic/model
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

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new_elastic/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred --power 0 --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new_elastic/model/finngen_R10_${linenamecleaned}.megaprs.new.effects  --max-threads 4

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new_elastic/prediction/finngen_R10_${linenamecleaned}.prediction.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new_elastic/prediction
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

total_lines=$(awk 'END {print NR}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)

for ((j=1; j<=${total_lines}; j++)); do

#for j in {1..1}; do
echo $j
my_variable=$(awk -v k=$j 'NR == k {print $4}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)
#echo ${my_variable}
#done
linenamecleaned=$(awk -v k=$j 'NR == k {print $1}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/finngen_ukbb_mapping_combined.txt)


awk 'NR==FNR {a[NR]=$3; next} FNR>1 {if ((FNR-1) in a) $3=a[FNR-1]} 1' /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code${my_variable}.pheno /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new_elastic/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new_elastic/prediction/combine/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.pred.profile.combined

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

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new_elastic/jackknife/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/megaprs_new_elastic/prediction/combine/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.pred.profile.combined --num-blocks 200 --AUC YES --prevalence 0.02

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new_elastic/jackknife/finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.jackknife.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno3_as_reference_panel/scripts/megaprs_new_elastic/jackknife
sbatch finngen_R10_${linenamecleaned}.code${my_variable}.megaprs.new.jackknife.sh

done

```

