# Commands during RA
## Week 3

12/4/2023

# New MegaPRS
## 1. Pre-pre cor

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

${dir_LDAK} --calc-cors ${dir_RA}/megaprs_new/pred_cor/geno_train_cors_$j --bfile ${dir_RA}/data/geno_train --window-cm 3 --chr $j

" > ${dir_RA}/scripts/megaprs_new/pred_cor/geno_train_cors_$j

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/pred_cor/
sbatch geno_train_cors_$j
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
${dir_LDAK} --join-cors ${dir_RA}/megaprs_new/pred_cor/geno_train_cors_total --corslist ${dir_RA}/megaprs_new/pred_cor/list.txt

" > ${dir_RA}/scripts/megaprs_new/pred_cor/geno_train_cors_total

cd ${dir_RA}/scripts/megaprs_new/pred_cor/
sbatch geno_train_cors_total
``` 



## 2. Prediction Model


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

${dir_LDAK} --mega-prs ${dir_RA}/megaprs_new/geno_train_megabayesr --model bayesr --summary ${dir_RA}/megaprs/white_train.summaries --cors ${dir_RA}/megaprs_new/geno_precor --cv-proportion .1 --high-LD ${dir_RA}/megaprs/highld_white/genes.predictors.used --window-cm 1 --allow-ambiguous YES


" > ${dir_RA}/scripts/megaprs_new/geno_train_megabayesr

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/
sbatch geno_train_megabayesr
```