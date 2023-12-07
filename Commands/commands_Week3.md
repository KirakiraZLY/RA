# Commands during RA
## Week 3

12/4/2023

# New MegaPRS
## 1. Pre-pre cor

```python
dir_data="/home/lezh/dsmwpred/data/ukbb"
shuf -n 5000 ${dir_data}/geno.fam > ${dir_RA}/megaprs_new/pred_cor/rand.5000 
```

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash

#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-cors ${dir_RA}/megaprs_new/pred_cor/geno_train_cors --bfile ${dir_data}/geno --window-cm 3  --keep ${dir_RA}/scripts/megaprs_new/pred_cor/rand.5000

" > ${dir_RA}/scripts/megaprs_new/pred_cor/geno_train_cors

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/pred_cor/
sbatch geno_train_cors
done
``` 

## 2. Prediction Model


```python

for j in list
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh
$j
${dir_LDAK} --mega-prs ${dir_RA}/megaprs_new/geno_train_megabayesr --model bayesr --summary ${dir_RA}/megaprs/white_train.summaries --cors ${dir_RA}/megaprs/pred_cor/cors_white_total --cv-proportion .1 --high-LD ${dir_RA}/megaprs/highld_white/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25


" > ${dir_RA}/scripts/megaprs_new/geno_train_megabayesr

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/
sbatch geno_train_megabayesr
```

## 3. Predict Phenotype

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh
${dir_LDAK} --calc-scores ${dir_RA}/megaprs_new/prediction/geno_test_scores_megaprs_new --scorefile ${dir_RA}/megaprs_new/geno_train_megabayesr.effects --bfile ${dir_data}/geno --power 0 --pheno ${dir_data}/height.test

" > ${dir_RA}/scripts/megaprs_new/prediction/geno_test_scores_megaprs_new

cd ${dir_RA}/scripts/megaprs_new/prediction
sbatch geno_test_scores_megaprs_new


```



# On 100 phenotypes from FinnGen

## Download
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh

wget -i ${dir_RA}/data/FinnGen/list_100_ss_links.txt -P ${dir_RA}/data/FinnGen/summarystatistics/

" > ${dir_RA}/scripts/data/FinnGen/ss_100_download

cd ${dir_RA}/scripts/data/FinnGen/
sbatch ss_100_download


```

## Unzip
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh

gunzip ${dir_RA}/data/FinnGen/summarystatistics/*

" > ${dir_RA}/scripts/data/FinnGen/ss_100_gunzip

cd ${dir_RA}/scripts/data/FinnGen/
sbatch ss_100_gunzip


```


### Try to make a loop in the list.

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_3_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_3_ss_phenocode.txt"
for j in {1..3}; do
    line=$(head -n $j $ss_filename | tail -n 1)
    linename=$(head -n $j $ss_name_filename | tail -n 1)
    linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
    linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
    a=()
    for p in "$linenamecleaned"; do a+=("$p.bed"); done
    echo -e $line
    echo -e $a
done
```


### Construct the prediction model.

Using 100 SS in the list.

```python


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_3_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_3_ss_phenocode.txt"


for j in {1..3}; do

    line=$(head -n $j $ss_filename | tail -n 1)
    linename=$(head -n $j $ss_name_filename | tail -n 1)
    linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
    linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

    echo "#"'!'"/bin/bash
    #SBATCH --mem 16G
    #SBATCH -t 8:0:0
    #SBATCH -c 4
    #SBATCH -A dsmwpred
    #SBATCH --constraint \"s05\"
    source /home/lezh/miniconda3/etc/profile.d/conda.sh



    ${dir_LDAK} --mega-prs ${dir_RA}/proj1_testprs_finngen_ukbb/megaprs_new/prediction/megabayesr_$linename --model bayesr --summary $linecleanedstring --cors ${dir_RA}/megaprs/pred_cor/cors_white_total --cv-proportion .1 --high-LD ${dir_RA}/megaprs/highld_white/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25

    " > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/megabayesr_$linename

    cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/
    sbatch megabayesr_$linename

done
``` 


## Delete the title of SS files
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_3_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_3_ss_phenocode.txt"
for j in {1..100}; do

    line=$(head -n $j $ss_filename | tail -n 1)
    linename=$(head -n $j $ss_name_filename | tail -n 1)
    linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
    linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
    linecleanedstring_withouttitle=()
    for p in "$linecleanedstring"; do linecleanedstring_withouttitle+=("$p.notitle"); done

    tail -n +2 $linecleanedstring > $linecleanedstring_withouttitle

done
```

## Liftover, hg38 to hg19
https://www.biostars.org/p/9476954/

```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_3_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_3_ss_phenocode.txt"


for j in {1..3}; do

    line=$(head -n $j $ss_filename | tail -n 1)
    linename=$(head -n $j $ss_name_filename | tail -n 1)
    linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
    linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
    
    linecleanedstring_withouttitle=()
    for p in "$linecleanedstring"; do linecleanedstring_withouttitle+=("$p.notitle"); done
    linenamecleaned_bed=()
    for p in "$linenamecleaned"; do linenamecleaned_bed+=("$p.bed"); done
    linenamecleaned_bed_script=()
    for p in "$linenamecleaned_bed"; do linenamecleaned_bed_script+=("$p.sh"); done

    echo "#"'!'"/bin/bash
    #SBATCH --mem 16G
    #SBATCH -t 8:0:0
    #SBATCH -c 4
    #SBATCH -A dsmwpred
    #SBATCH --constraint \"s05\"
    source /home/lezh/miniconda3/etc/profile.d/conda.sh



    #awk '{print "chr"$1, ($2-1), $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13}' $linecleanedstring > ${dir_RA}/data/FinnGen/summarystatistics/liftover_hg19/$linenamecleaned_bed
    awk '{print chr$1,$2-1}'  $linecleanedstring_withouttitle > ${dir_RA}/data/FinnGen/summarystatistics/liftover_hg19/$linenamecleaned_bed

    " > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/liftover_hg19/$linenamecleaned_bed_script

    cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/liftover_hg19/
    sbatch $linenamecleaned_bed_script

done
```