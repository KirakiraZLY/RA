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





## LDAK Weighting on each dataset 
1
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

${dir_LDAK} --bfile ${dir_data}/geno  --max-threads 4  --cut-weights ${dir_RA}/data/geno_weighting 

${dir_LDAK} --bfile ${dir_data}/geno  --max-threads 4  --calc-weights-all ${dir_RA}/data/geno_weighting 


" > ${dir_RA}/scripts/data/LDAK_Weighting_Step1and2

# I am doing blabla
cd ${dir_RA}/scripts/data/
sbatch LDAK_Weighting_Step1and2

```

# LDAK-thin
## LDAK-thin on each dataset 
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

${dir_LDAK} --bfile ${dir_data}/geno  --max-threads 4  --thin ${dir_RA}/data/geno_weighting_thin  --window-prune 0.98 --window-kb 100


" > ${dir_RA}/scripts/data/LDAK_Weighting_thin_Step1and2

# I am doing blabla
cd ${dir_RA}/scripts/data/
sbatch LDAK_Weighting_thin_Step1and2
```

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
awk < ${dir_RA}/data/geno_weighting_thin.in '{print $1, 1}' > ${dir_RA}/data/geno_weighting_thin.thin
```




## Make Pheno, Simulation

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} \
  --make-phenos ${dir_RA}/data/makepheno/Trait_1 \
  --bfile ${dir_data}/geno \
  --weights ${dir_RA}/data/geno_weighting_thin.thin \
  --power -0.25 \
  --her 0.9 \
  --num-phenos 5 \
  --num-causals 50000 \
  --extract ${dir_RA}/data/snps_1_to_12_geno.txt


${dir_LDAK} \
  --make-phenos ${dir_RA}/data/makepheno/Trait_2 \
  --bfile ${dir_data}/geno \
  --weights ${dir_RA}/data/geno_weighting_thin.thin \
  --power -0.25 \
  --her 0.1 \
  --num-phenos 5 \
  --num-causals 50000 \
  --extract ${dir_RA}/data/snps_1_to_12_geno.txt


${dir_LDAK} \
  --make-phenos ${dir_RA}/data/makepheno/Trait_3 \
  --bfile ${dir_data}/geno \
  --weights ${dir_RA}/data/geno_weighting_thin.thin \
  --power -0.25 \
  --her 0.9 \
  --num-phenos 5 \
  --num-causals 5000 \
  --extract ${dir_RA}/data/snps_1_to_12_geno.txt


${dir_LDAK} \
  --make-phenos ${dir_RA}/data/makepheno/Trait_4 \
  --bfile ${dir_data}/geno \
  --weights ${dir_RA}/data/geno_weighting_thin.thin \
  --power -0.25 \
  --her 0.1 \
  --num-phenos 5 \
  --num-causals 5000 \
  --extract ${dir_RA}/data/snps_1_to_12_geno.txt

  
  " > ${dir_RA}/scripts/data/makepheno/Trait_1_to_4

	# I am doing blabla
	cd ${dir_RA}/scripts/data/makepheno/
	sbatch Trait_1_to_4


```



## Summary Statistics
### Bolt height
```python
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"


source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/BOLT-LMM_v2.4/bolt --bfile=${dir_data}/geno --phenoFile=${dir}/Phenotype_UKBB/height_label.pheno  --phenoCol=Phenotype  --covarFile=${dir}/covar_Black_PC_10.covars --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=${dir}/Real_Traits/height/data_Black_Bolt_height

" > ${dir}/scripts/Real_Traits/height/data_Black_Bolt_height


# I am doing blabla
cd ${dir}/scripts/Real_Traits/height/

sbatch data_Black_Bolt_height
```


## Bolt-lmm-inf height
```python
##############################
Bolt-inf
##############################
dir="/home/lezh/dsmwpred/zly"
echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"


source /home/lezh/miniconda3/etc/profile.d/conda.sh


${dir}/software/BOLT-LMM_v2.4/bolt --bfile=${dir}/data_Black --phenoFile=${dir}/Phenotype_UKBB/height_label.pheno  --phenoCol=Phenotype  --covarFile=${dir}/covar_Black_PC_10.covars --qCovarCol=PC{1:10}  --lmmInfOnly --LDscoresUseChip --numThreads 4  --statsFile=${dir}/Real_Traits/height/data_Black_Bolt_inf_height



" > ${dir}/scripts/Real_Traits/height/data_Black_Bolt_inf_height


# I am doing blabla
cd ${dir}/scripts/Real_Traits/height/

sbatch data_Black_Bolt_inf_height
```