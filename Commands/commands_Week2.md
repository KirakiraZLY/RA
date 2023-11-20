# Commands during RA
## Week 1
2023/11/15   

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
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh
${dir_LDAK} --sum-hers ${dir_RA}/quickprs/white_train.bld.ldak --summary ${dir_RA}/megaprs/white_train.summaries.quickprs --tagfile ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.tagging --matrix ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.matrix --check-sums NO

" > ${dir_RA}/scripts/quickprs/per_pred_her/white_train_bldldak

cd ${dir_RA}/scripts/quickprs/per_pred_her/
sbatch white_train_bldldak

``` 

The estimated per-predictor heritabilities are saved in white_train.bld.ldak.ind.hers   

2   
We then construct a BayesR prediction model by running   
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
${dir_LDAK} --mega-prs ${dir_RA}/quickprs/white_train.bld.ldak.bayesr --summary ${dir_RA}/megaprs/white_train.summaries.quickprs --ind-hers ${dir_RA}/quickprs/white_train.bld.ldak.ind.hers --cors ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap --high-LD ${dir_RA}/quickprs/precomputed/gbr.hapmap/highld.snps --model bayesr --cv-proportion .1 --window-cm 1 --extract ${dir_RA}/megaprs/white_train.summaries.quickprs

" > ${dir_RA}/scripts/quickprs/per_pred_her/white_train_bayesr

cd ${dir_RA}/scripts/quickprs/per_pred_her/
sbatch white_train_bayesr

``` 

3
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
${dir_LDAK} --calc-scores ${dir_RA}/quickprs/white_scores --scorefile ${dir_RA}/quickprs/white_train.bld.ldak.bayesr.effects --bfile ${dir_data}/geno2 --power 0 --pheno ${dir_data}/height.test

" > ${dir_RA}/scripts/quickprs/white_scores

cd ${dir_RA}/scripts/quickprs/
sbatch white_scores


```