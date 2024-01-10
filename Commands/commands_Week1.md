# Commands during RA
## Week 1
2023/11/15   

### Data
```python
dir="/home/lezh/dsmwpred/zly"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir}/data_qc
```  

### High-LD Regions
```python
dir="/home/lezh/dsmwpred/zly"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "Region25 21  14600000 14700000" | cat ${dir}/RA/highld.txt - > ${dir}/RA/highld.fake
${dir_LDAK} --cut-genes ${dir}/RA/highld --bfile ${dir}/data_qc --genefile ${dir}/RA/highld.fake
```  

### Making Summary Statistics
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
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh
${dir_LDAK} --linear ${dir_RA}/megaprs/white_train --bfile ${dir_data}/geno --pheno ${dir_data}/height.train
${dir_LDAK} --linear ${dir_RA}/megaprs/white_test --bfile ${dir_data}/geno --pheno ${dir_data}/height.test

" > ${dir_RA}/scripts/megaprs/white_train_test

# I am doing blabla
cd ${dir_RA}/scripts/megaprs/
sbatch white_train_test
``` 

Summary statistics will store in white_train.summaries

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
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --cut-genes ${dir_RA}/megaprs/highld_white --bfile ${dir_data}/geno --genefile ${dir_RA}/data/highld.txt

" > ${dir_RA}/scripts/megaprs/highld_white












# I am doing blabla
cd ${dir_RA}/scripts/megaprs/
sbatch highld_white
``` 

Usually, the lists of SNPs in high-LD regions would be saved in the file highld/genes.predictors.used   

### Calculate predictor-predictor correlations.
```python
for j in {1..22}; do
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

${dir_LDAK} --calc-cors ${dir_RA}/megaprs/pred_cor/cors_white_$j --bfile ${dir_data}/geno --window-cm 3 --chr $j

" > ${dir_RA}/scripts/megaprs/pred_cor/cors_white_$j

# I am doing blabla
cd ${dir_RA}/scripts/megaprs/pred_cor/
sbatch cors_white_$j
done
``` 
放到pred_cor中
路径更改到pred_cor

Chr 6 wrong, do it specificly.
```python
for j in {6..6}; do
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash

#SBATCH --mem 64G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-cors ${dir_RA}/megaprs/pred_cor/cors_white_$j --bfile ${dir_data}/geno --window-cm 3 --chr $j

" > ${dir_RA}/scripts/megaprs/pred_cor/cors_white_$j

# I am doing blabla
cd ${dir_RA}/scripts/megaprs/pred_cor/
sbatch cors_white_$j
done
``` 

```python
rm list.txt; for j in {1..22}; do echo "cors_white_$j" >> list.txt; done
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
${dir_LDAK} --join-cors ${dir_RA}/megaprs/pred_cor/cors_white_total --corslist ${dir_RA}/megaprs/pred_cor/list.txt

" > ${dir_RA}/scripts/megaprs/pred_cor/cors_white_total

cd ${dir_RA}/scripts/megaprs/pred_cor/
sbatch cors_white_total
``` 

Reference Panel is from Pre-computed Taggings https://dougspeed.com/pre-computed-tagging-files/   



### Estimate per-predictor heritabilities assuming the LDAK-Thin Model
https://dougspeed.com/per-predictor-heritabilities/

To assume the LDAK-Thin Model, we must first create a weightsfile that gives weighting 1 to the predictors that remain after thinning for duplicates, and weighting 0 to those removed. This can be achieved using the commands
1
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
${dir_LDAK} --thin ${dir_RA}/megaprs/her_ldak_thin/white_thin --bfile ${dir_data}/geno --window-prune .98 --window-kb 100

" > ${dir_RA}/scripts/megaprs/her_ldak_thin/white_thin

cd ${dir_RA}/scripts/megaprs/her_ldak_thin/
sbatch white_thin
``` 
2
```python
awk < ${dir_RA}/megaprs/her_ldak_thin/white_thin.in '{print $1, 1}' > ${dir_RA}/megaprs/her_ldak_thin/white_weights.thin
``` 

3
Now when calculating the tagging file, we use the options --weights <weightsfile> and --power -.25

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
${dir_LDAK} --calc-tagging ${dir_RA}/megaprs/her_ldak_thin/white_thin.thin --bfile ${dir_data}/geno --weights ${dir_RA}/megaprs/her_ldak_thin/white_weights.thin --power -.25 --window-cm 1 --save-matrix YES


" > ${dir_RA}/scripts/megaprs/her_ldak_thin/white_thin_calc_matrix

cd ${dir_RA}/scripts/megaprs/her_ldak_thin/
sbatch white_thin_calc_matrix
``` 
4
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
${dir_LDAK} --sum-hers ${dir_RA}/megaprs/her_ldak_thin/white_thin.thin --tagfile ${dir_RA}/megaprs/her_ldak_thin/white_thin.thin.tagging --summary ${dir_RA}/megaprs/white_train.summaries --matrix ${dir_RA}/megaprs/her_ldak_thin/white_thin.thin.matrix

" > ${dir_RA}/scripts/megaprs/her_ldak_thin/white_thin_calc

cd ${dir_RA}/scripts/megaprs/her_ldak_thin/
sbatch white_thin_calc

``` 



### Construct the prediction model.

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
${dir_LDAK} --mega-prs ${dir_RA}/megaprs/prediction/megabayesr --model bayesr --ind-hers ${dir_RA}/megaprs/her_ldak_thin/white_thin.thin.ind.hers --summary ${dir_RA}/megaprs/white_train.summaries --cors ${dir_RA}/megaprs/pred_cor/cors_white_total --cv-proportion .1 --high-LD ${dir_RA}/megaprs/highld_white/genes.predictors.used --window-cm 1 --allow-ambiguous YES

" > ${dir_RA}/scripts/megaprs/prediction/white_megaprs_pred

cd ${dir_RA}/scripts/megaprs/prediction/
sbatch white_megaprs_pred
``` 


2
Predict Phenotype
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
${dir_LDAK} --calc-scores ${dir_RA}/megaprs/prediction/white_scores_megaprs --scorefile ${dir_RA}/megaprs/prediction/megabayesr.effects --bfile ${dir_data}/geno --power 0 --pheno ${dir_data}/height.test

" > ${dir_RA}/scripts/megaprs/prediction/white_scores_megaprs

cd ${dir_RA}/scripts/megaprs/prediction
sbatch white_scores_megaprs


```