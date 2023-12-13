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

${dir_LDAK} --calc-cors ${dir_RA}/proj1_testprs_finngen_ukbb/pred_cor/geno2_cors --bfile ${dir_data}/geno2 --window-cm 3  --keep ${dir_RA}/proj1_testprs_finngen_ukbb/pred_cor/rand.5000

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pred_cor/geno2_cors

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pred_cor/
sbatch geno2_cors

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

## geno2 inconsistent -> consistent
### Simulation, bim -> bed
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/plink --bfile ${dir_data}/geno2 --noweb --extract ${dir_RA}/proj1_testprs_finngen_ukbb/data/geno2_consistent_bim_list.txt --make-bed --out ${dir_RA}/proj1_testprs_finngen_ukbb/data/geno2_v2

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/data/geno2_v2

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/data/
sbatch geno2_v2


```


## 2.1 Making extract list for Prediction Model
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

linenamecleanedextractsh=()
for p in "$linenamecleaned"; do 
a=("finngen_R8_$p");
linenamecleanedextractsh+=("$a.extract.sh"); done

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript ${dir_RA}/proj1_testprs_finngen_ukbb/code/finn_gen_hg19_extract.R $j
echo -e $j $linenamecleanedextractsh "done"

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pred_cor/extract/$linenamecleanedextractsh

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/pred_cor/extract/
sbatch $linenamecleanedextractsh

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



# SumHer Checking

### Estimate per-predictor heritabilities assuming the LDAK-Thin Model
https://dougspeed.com/per-predictor-heritabilities/

To assume the LDAK-Thin Model, we must first create a weightsfile that gives weighting one to the predictors that remain after thinning for duplicates, and weighting zero to those removed. This can be achieved using the commands

### 1
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

shuf -n 5000 ${dir_data}/geno2.fam > ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/rand.5000 

${dir_LDAK} --thin ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/geno2_thin_weight --bfile ${dir_data}/geno2 --window-prune .98 --window-kb 100 --keep ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/rand.5000 

```

### 1.5 weight
```python
awk < ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/geno2_thin_weight.in '{print $1, 1}' > ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/geno2_weights.thin


```



Now when calculating the tagging file, we use the options --weights <weightsfile> and --power -.25


### 2 tagging
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

${dir_LDAK} --calc-tagging ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/geno2.thin --bfile ${dir_data}/geno2 --weights ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/geno2_weights.thin --power -.25 --window-cm 1 --save-matrix YES  --keep ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/rand.5000 


```

### 3
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

sumher=()
for p in $linenamecleaned; do 
sumher+=("$p.sumher"); done

sumhername=()
for p in $linenamecleaned; do 
a=("finngen_R8_$p");
sumhername+=("$a.sumher"); done

extractname=()
for p in $linenamecleaned; do 
a=("finngen_R8_$p");
extractname+=("$a.ss.extrac"); done

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --sum-hers ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/results/$sumhername --tagfile ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/geno2.thin.tagging --summary ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractname --matrix ${dir_RA}/proj1_testprs_finngen_ukbb/sumher/geno2.thin.matrix  --extract ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/$extractnamelist  --check-sums NO
echo -e $j $sumher "done"

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/sumher/finngen_R8_$sumher

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/sumher/
sbatch finngen_R8_$sumher

done







```
The per-predictor heritabilities are saved in ldak.thin.ind.hers.

