# Commands during RA
## Week 5

17/12/2023

# non-iid problem

## high LD region

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/plink --bfile ${dir_noniid_data}/mhc --r2 --ld-window-r2 0.8 --ld-window 50000 --ld-window-kb 1000 --out ${dir_RA}/proj2_noniid_problem/highld/mhc_highld

" > ${dir_RA}/scripts/proj2_noniid_problem/highld/mhc_highld

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/highld/
sbatch mhc_highld
```

### high ld for a single snp

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/plink --bfile ${dir_noniid_data}/mhc --r2  --ld-snp 6:25279824:G:A  --ld-window-r2 0 --ld-window 99999 --ld-window-kb 1000  --out ${dir_RA}/proj2_noniid_problem/highld/mhc_highld_6:25279824:G:A  

#${dir}/software/plink --bfile ${dir_RA}/proj2_noniid_problem/pseudo_genotype/smallset  --r2   --ld-window-r2 0 --ld-window 99999 --ld-window-kb 1000  --out ${dir_RA}/proj2_noniid_problem/highld/smallset_highld_nomatrix

" > ${dir_RA}/scripts/proj2_noniid_problem/highld/mhc_highld_6:25279824:G:A  

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/highld/
sbatch mhc_highld_6:25279824:G:A  
```


### By calculating Genetic Correlation

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --linear ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_1 --bfile ${dir_noniid_data}/mhc --pheno ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_1.pheno
${dir_LDAK} --linear ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_2 --bfile ${dir_noniid_data}/mhc --pheno ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_2.pheno

${dir_LDAK} --sum-cors ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_gencor --summary ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_1.summaries --summary2 ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_2.summaries --tagfile ${dir_RA}/proj2_noniid_problem/highld/ldak.thin.genotyped.gbr.tagging --allow-ambiguous YES  --cutoff 0.01  --extract ${dir_RA}/proj2_noniid_problem/mhc_phenotype/snps_only_chr6_mhc.txt

" > ${dir_RA}/scripts/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_1and2_geneticcorrelation

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/highld/genetic_correlation/
sbatch mhc_trait_1and2_geneticcorrelation

```



## "make genotype"
```python
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir_LDAK} --make-snps ${dir_RA}/proj2_noniid_problem/pseudo_genotype/medianset --num-samples 500 --num-snps 1000
```

## make phenotype

### 1 Weighting

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

shuf -n 5000 ${dir_noniid_data}/mhc.fam > ${dir_RA}/proj2_noniid_problem/mhc_phenotype/rand.5000 

${dir_LDAK} --bfile ${dir_noniid_data}/mhc  --max-threads 4  --thin ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin  --window-prune 0.98 --window-kb 100 --keep ${dir_RA}/proj2_noniid_problem/mhc_phenotype/rand.5000


" > ${dir_RA}/scripts/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/mhc_phenotype/
sbatch mhc_weighting_thin

```

### 1.5
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
awk < ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin.in '{print $1, 1}' > ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin.thin
```

### 2 SNP extract for mhc, chr == 6
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

conda activate zly2
Rscript ${dir_RA}/proj2_noniid_problem/codes/mhc_snp_extract.R
```

### 3 Simulating 
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} \
  --make-phenos ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_2 \
  --bfile ${dir_noniid_data}/mhc \
  --weights ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin.thin \
  --power -0.25 \
  --her 0.1 \
  --num-phenos 1 \
  --num-causals 5000 \
  --extract ${dir_RA}/proj2_noniid_problem/mhc_phenotype/snps_only_chr6_mhc.txt

" > ${dir_RA}/scripts/proj2_noniid_problem/mhc_phenotype/mhc_trait_2.sh

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/mhc_phenotype/
sbatch mhc_trait_2.sh
```

## Make Summary Statistics
By LDAK
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"
echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --pheno ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_1.pheno --max-threads 4  --bfile ${dir_noniid_data}/mhc  --linear ${dir_RA}/proj2_noniid_problem/summarystatistics/mhc_ldak_trait_1

" > ${dir_RA}/scripts/proj2_noniid_problem/summarystatistics/mhc_ldak_trait_1

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/summarystatistics/
sbatch mhc_ldak_trait_1

```

## Make phenotype by medianset
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

${dir_LDAK} \
  --make-phenos ${dir_RA}/proj2_noniid_problem/pseudo_genotype/medianset_pheno \
  --bfile ${dir_RA}/proj2_noniid_problem/pseudo_genotype/medianset \
  --ignore-weights YES  \
  --power -1 \
  --her 0.5 \
  --num-phenos 1 \
  --num-causals 100

```

## Run PRS on an example data
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python ${dir_RA}/proj2_noniid_problem/codes/Transformer_PRS/main.py --bfile ${dir_RA}/proj2_noniid_problem/pseudo_genotype/medianset  --phenoFile ${dir_RA}/proj2_noniid_problem/pseudo_genotype/medianset_pheno.pheno  --modelSave ${dir_RA}/proj2_noniid_problem/results/model/medianset_trait_1.model  --modelLoad ${dir_RA}/proj2_noniid_problem/results/model/medianset_trait_1.model  --out ${dir_RA}/proj2_noniid_problem/results/medianset_result_1  --epoch 20

" > ${dir_RA}/scripts/proj2_noniid_problem/results/medianset_result_1

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/results/
sbatch medianset_result_1
```

## Run from my local computer

### Small Set
```python

python ./main.py --bfile ./data/smallset  --phenoFile ./data/smallset_pheno.pheno  --modelSave ./model/smallset_trait_1.model  --modelLoad ./model/smallset_trait_1.model  --out ./result/smallset_trait_1  --epoch 20

```

### Median Set
```python

python ./main.py --bfile ./data/medianset  --phenoFile ./data/medianset_pheno.pheno  --modelSave ./model/medianset_trait_1.model  --modelLoad ./model/medianset_trait_1.model  --out ./result/medianset_trait_1  --epoch 20

```

### To test from cluster
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

python ${dir_RA}/proj2_noniid_problem/codes/Transformer_PRS/main.py --bfile ${dir_noniid_data}/mhc  --phenoFile ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_1.pheno  --modelSave ${dir_RA}/proj2_noniid_problem/results/mhc_result/model/mhc_trait_1.model  --modelLoad ${dir_RA}/proj2_noniid_problem/results/mhc_result/model/mhc_trait_1.model  --out ${dir_RA}/proj2_noniid_problem/results/mhc_result_2  --epoch 20

```


# Bolt Predict
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"
echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
${dir_LDAK} --bolt ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/geno_train_Trait1_bolt_prs --LDpred YES --bfile ${dir_RA}/data/geno_train --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.train --LOCO NO  --mpheno 1

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/bolt_pred/geno_train_Trait1_bolt_prs

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/bolt_pred/
sbatch geno_train_Trait1_bolt_prs

```

## Example
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"
echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

${dir_LDAK} --make-snps ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake --num-samples 10000 --num-snps 10000
${dir_LDAK} --make-phenos ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake --num-phenos 1 --her .3 --power -1 --num-causals 100 --bfile ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake

${dir_LDAK}  --bolt ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/ldpred_fake --LDpred YES --bfile ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake --pheno ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake.pheno --LOCO NO

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/bolt_pred/ldpred_fake

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/bolt_pred/
sbatch ldpred_fake
```



# Proj1 Finngen UKBB

## Copy UKBB phenos (from 100 FinnGen)
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ukbb_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_ready_to_copy.txt"

for j in {1..100}; do
    line=$(head -n $j $ukbb_filename | tail -n 1 | sed 's/\\"r"//g; s/\r$//')
    echo -e $line
    cp $line  /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100ukbb/
done


```

## Change pheno files name
```python
fg100_file="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/finngen_100pheno_in_icd10.txt"
target_folder="path/to/target_folder"
while IFS=$'\t' read -r line; do
    # 使用 awk 分隔列
    col1=$(echo "$line" | awk '{print $1}')
    col3=$(echo "$line" | awk '{print $3}')
    # 去掉行尾的 $'\r'
    col3=$(echo "$col3" | tr -d $'\r')
    echo "Column 1: $col1, Column 3: $col3"
done < "$fg100_file"

```

```python
fg100_file="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/finngen_100pheno_in_icd10.txt"
while IFS=$'\t' read -r line; do
    # 使用 awk 分隔列
    col1=$(echo "$line" | awk '{print $1}')
    col3=$(echo "$line" | awk '{print $3}')
    # 去掉行尾的 $'\r'
    col3=$(echo "$col3" | tr -d $'\r')
    #echo "Column 1: $col1, Column 3: $col3"
    target=()
    for p in "$col1"; do target+=("/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/code${p}.pheno"); done
    targetname=()
    for p in "$col3"; do targetname+=("/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/finngen_R8_${p}.pheno"); done
    #echo $targetname
    #mv $target $targetname
    targetname1=()
    for p in "$col3"; do targetname1+=("finngen_R8_${p}.pheno"); done
    echo "$targetname" >> "/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_list.txt"
done < "$fg100_file"

```

## ukbb finngen prs test
### MegaPRS new
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"


for j in {1..100}; do

line=$(head -n $j $ss_filename | tail -n 1)
linename=$(head -n $j $ss_name_filename | tail -n 1)
linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

sumstat=()
for p in $linenamecleaned; do 
sumstat+=("$p.hg19"); done

sumstatout=()
for p in $linenamecleaned; do 
sumstatout+=("$p.newmega"); done

linenamecleanedlift=()
for p in "$linenamecleaned"; do 
a=("finngen_R8_$p");
linenamecleanedlift+=("$a.lifted"); done

excludename=()
for p in "$linenamecleaned"; do 
a=("finngen_R8_$p");
excludename+=("$a.exclu"); done

extractname=()
for p in "$linenamecleaned"; do 
a=("finngen_R8_$p");
extractname+=("$a.ss.extrac"); done


extractnamelist=()
for p in "$linenamecleaned"; do 
a=("finngen_R8_$p");
extractnamelist+=("$a.extract.list"); done

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs ${dir_RA}/proj1_testprs_finngen_ukbb/megaprs_new/prediction/$sumstatout --model bayesr --summary ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractname --cors ${dir_RA}/proj1_testprs_finngen_ukbb/pred_cor/geno2_train_cors --cv-proportion .1 --high-LD ${dir_RA}/proj1_testprs_finngen_ukbb/high_ld/highld_geno2/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25  --fixed-n 300000  --extract ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractnamelist 


" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/finngen_R8_$sumstatout

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/
sbatch finngen_R8_$sumstatout

done



```

### Quick PRS
Quick PRS is an approximate version of MegaPRS.   
MegaPRS requires the user to compute a tagging file, heritability matrix and predictor-predictor correlations;   
Quick PRS uses versions of these files pre-computed using data from the UK Biobank

1   
We first estimate per-predictor heritabilities by running

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
icd10="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_list.txt"
finngen_ss_link="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode_withprefix.txt"
finngen_ss_name="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode.txt"
finngen_42phenos="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/finngen_42phenos.txt"
for j in {1..42}; do
linename=$(head -n $j ${finngen_42phenos} | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
line=()
for p in "$linenamecleaned"; do linecleanedstring+=("/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/finngen_R8_$linenamecleaned"); done
linenameCleanedQuick=()
for p in "$linenamecleaned"; do linenameCleanedQuick+=("$p.bld.ldak"); done
linecleanedStringHG=()
for p in "$linecleanedstring"; do linecleanedStringHG+=("$p.hg19"); done
extractname=()
for p in "$linenamecleaned"; do a=("finngen_R8_$p");  extractname+=("$a.ss.extrac"); done
echo "#"'!'"/bin/bash
#SBATCH --mem 1G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh
${dir_LDAK} --sum-hers ${dir_RA}/proj1_testprs_finngen_ukbb/pheno100/quickprs/$linenameCleanedQuick --summary ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractname --tagfile ${dir_RA}/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.tagging --matrix ${dir_RA}/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.matrix --check-sums NO  --fixed-n 300000

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pheno100/quickprs/$linenameCleanedQuick

cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pheno100/quickprs/
sbatch $linenameCleanedQuick
done

``` 

The estimated per-predictor heritabilities are saved in white_train.bld.ldak.ind.hers   

2   
We then construct a BayesR prediction model by running   
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
icd10="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_list.txt"
finngen_ss_link="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode_withprefix.txt"
finngen_ss_name="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode.txt"
finngen_42phenos="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/finngen_42phenos.txt"
for j in {1..42}; do
linename=$(head -n $j ${finngen_42phenos} | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
line=()
for p in "$linenamecleaned"; do linecleanedstring+=("/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/finngen_R8_$linenamecleaned"); done
linenameCleanedQuick=()
for p in "$linenamecleaned"; do linenameCleanedQuick+=("$p.bld.ldak"); done
linecleanedStringHG=()
for p in "$linecleanedstring"; do linecleanedStringHG+=("$p.hg19"); done
extractnamelist=()
for p in "$linenamecleaned"; do  a=("finngen_R8_$p");  extractnamelist+=("$a.extract.list"); done
extractname=()
for p in "$linenamecleaned"; do a=("finngen_R8_$p");  extractname+=("$a.ss.extrac"); done

echo "#"'!'"/bin/bash
#SBATCH --mem 1G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs ${dir_RA}/proj1_testprs_finngen_ukbb/pheno100/quickprs/${linenameCleanedQuick}.bayesr --summary ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractname --ind-hers ${dir_RA}/proj1_testprs_finngen_ukbb/pheno100/quickprs/${linenameCleanedQuick}.ind.hers --cors ${dir_RA}/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap --high-LD ${dir_RA}/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/highld.snps --model bayesr --cv-proportion .1 --window-cm 1  --fixed-n 300000  --extract ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractnamelist

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pheno100/quickprs/${linenameCleanedQuick}.bayesr

cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pheno100/quickprs/
sbatch ${linenameCleanedQuick}.bayesr
done


``` 

3
Predict Phenotype
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
icd10="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_list.txt"
finngen_ss_link="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode_withprefix.txt"
finngen_ss_name="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode.txt"
finngen_42phenos="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/finngen_42phenos.txt"
for j in {1..42}; do
linename=$(head -n $j ${finngen_42phenos} | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
line=()
for p in "$linenamecleaned"; do linecleanedstring+=("/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/finngen_R8_$linenamecleaned"); done

linenameCleanedQuick=()
for p in "$linenamecleaned"; do linenameCleanedQuick+=("$p.bld.ldak"); done
linecleanedStringHG=()
for p in "$linecleanedstring"; do linecleanedStringHG+=("$p.hg19"); done
extractnamelist=()
for p in "$linenamecleaned"; do   a=("finngen_R8_$p");  extractnamelist+=("$a.extract.list"); done
icdname=$(head -n $j ${icd10} | tail -n 1)
icdnamecleaned=$(echo -n "$icdname" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores ${dir_RA}/proj1_testprs_finngen_ukbb/pheno100/quickprs/scores/${linenamecleaned}.scores --scorefile ${dir_RA}/proj1_testprs_finngen_ukbb/pheno100/quickprs/${linenameCleanedQuick}.bayesr.effects --bfile ${dir_data}/geno2 --power 0 --pheno ${icdnamecleaned}  --extract ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractnamelist

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pheno100/quickprs/scores/${linenamecleaned}.scores

cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pheno100/quickprs/scores/
sbatch ${linenamecleaned}.scores
done

```



3 Try to use 42 traits on one SS   
**AB1_BACT_INTEST_OTH.bld.ldak.bayesr.effects**   
Predict Phenotype
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
icd10="/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_list.txt"
finngen_ss_link="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode_withprefix.txt"
finngen_ss_name="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode.txt"
finngen_42phenos="/faststorage/project/dsmwpred/zly/RA/data/FinnGen/finngen_42phenos.txt"
for j in {1..42}; do
linename=$(head -n $j ${finngen_42phenos} | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
line=()
for p in "$linenamecleaned"; do linecleanedstring+=("/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/finngen_R8_$linenamecleaned"); done

linenameCleanedQuick=()
for p in "$linenamecleaned"; do linenameCleanedQuick+=("$p.bld.ldak"); done
linecleanedStringHG=()
for p in "$linecleanedstring"; do linecleanedStringHG+=("$p.hg19"); done
extractnamelist=()
for p in "$linenamecleaned"; do   a=("finngen_R8_$p");  extractnamelist+=("$a.extract.list"); done
icdname=$(head -n $j ${icd10} | tail -n 1)
icdnamecleaned=$(echo -n "$icdname" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores ${dir_RA}/proj1_testprs_finngen_ukbb/pheno100/quickprs/scores/${linenamecleaned}.scores --scorefile ${dir_RA}/proj1_testprs_finngen_ukbb/pheno100/quickprs/AB1_BACT_INTEST_OTH.bld.ldak.bayesr.effects --bfile ${dir_data}/geno2 --power 0 --pheno ${icdnamecleaned}  --extract ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractnamelist

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pheno100/quickprs/scores/${linenamecleaned}.scores

cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pheno100/quickprs/scores/
sbatch ${linenamecleaned}.scores
done

```

