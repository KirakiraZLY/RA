# Commands during RA
## Week 4

12/11/2023

# Pre pre Cor

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
shuf -n 5000 ${dir_data}/geno2.fam > ${dir_RA}/proj1_testprs_finngen_ukbb/pred_cor/rand.5000 
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
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-cors ${dir_RA}/proj1_testprs_finngen_ukbb/pred_cor/geno2_train_cors --bfile ${dir_data}/geno2 --window-cm 3  --keep ${dir_RA}/proj1_testprs_finngen_ukbb/pred_cor/rand.5000

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pred_cor/geno2_train_cors

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pred_cor/
sbatch geno2_train_cors

``` 

### Identify high LD region
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --cut-genes ${dir_RA}/proj1_testprs_finngen_ukbb/high_ld/highld_geno2 --bfile ${dir_data}/geno2 --genefile ${dir_RA}/data/highld.txt

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/high_ld/highld_geno2

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/high_ld/
sbatch highld_geno2
``` 



# New Megaprs

## 2.1 Making exclude list for Prediction Model
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"


for j in {1..3}; do
    
    echo "#"'!'"/bin/bash
    #SBATCH --mem 16G
    #SBATCH -t 8:0:0
    #SBATCH -c 4
    #SBATCH -A dsmwpred
    source /home/lezh/miniconda3/etc/profile.d/conda.sh

    conda activate zly2
    Rscript ${dir_RA}/proj1_testprs_finngen_ukbb/code/finn_gen_hg19_cor_exclude.R $j
    echo -e $j "done"

    " > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pred_cor/exclude/finn_gen_hg19_cor_exclude_$j

    # I am doing blabla
    cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pred_cor/exclude/
    sbatch finn_gen_hg19_cor_exclude_$j

done


```

## 2 Prediction Model

```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"


for j in {1..3}; do

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



    echo "#"'!'"/bin/bash
    #SBATCH --mem 16G
    #SBATCH -t 8:0:0
    #SBATCH -c 4
    #SBATCH -A dsmwpred
    source /home/lezh/miniconda3/etc/profile.d/conda.sh



    ${dir_LDAK} --mega-prs ${dir_RA}/proj1_testprs_finngen_ukbb/megaprs_new/prediction/$sumstatout --model bayesr --summary ${dir_RA}/data/FinnGen/summarystatistics/finngen_R8_$sumstat --cors ${dir_RA}/proj1_testprs_finngen_ukbb/pred_cor/geno2_train_cors --cv-proportion .1 --high-LD ${dir_RA}/proj1_testprs_finngen_ukbb/high_ld/highld_geno2/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25  --fixed-n 300000  --exclude ${dir_RA}/proj1_testprs_finngen_ukbb/pred_cor/exclude/$excludename


    " > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/finngen_R8_$sumstatout

    # I am doing blabla
    cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/
    sbatch finngen_R8_$sumstatout

done


```
