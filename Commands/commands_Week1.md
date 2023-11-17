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
${dir_LDAK} --linear ${dir_RA}/megaprs/white_test --bfile ${dir_data}/geno --pheno ${dir_data}/height.train

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

#SBATCH --mem 8G
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

```python
rm list.txt; for j in {1..22}; do echo "cors$j" >> list.txt; done
./ldak.out --join-cors cors --corslist list.txt
``` 