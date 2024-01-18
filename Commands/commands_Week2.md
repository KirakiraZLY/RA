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


## Simulation, fam -> bed
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

${dir}/software/plink --bfile ${dir_data}/geno --noweb --keep ${dir_RA}/data/geno_train.fam --make-bed --out ${dir_RA}/data/geno_train

" > ${dir_RA}/scripts/data/geno_train

# I am doing blabla
cd ${dir_RA}/scripts/data/
sbatch geno_train
```

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 10:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/plink --bfile ${dir_data}/geno --noweb --keep ${dir_RA}/data/geno_test.fam --recode --make-bed --out ${dir_RA}/data/geno_test

" > ${dir_RA}/scripts/data/geno_test

# I am doing blabla
cd ${dir_RA}/scripts/data/
sbatch geno_test
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
  --make-phenos ${dir_RA}/data/makepheno/Trait_1_pheno1 \
  --bfile ${dir_data}/geno \
  --weights ${dir_RA}/data/geno_weighting_thin.thin \
  --power -0.25 \
  --her 0.9 \
  --num-phenos 1 \
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



## Summary Statistics gwas
Trait 1 to 4
Trait 1 (Just replace to Trait j)
### Bolt T1
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 32:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"


source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/BOLT-LMM_v2.4/bolt --bfile=${dir_data}/geno_train --phenoFile=${dir_RA}/data/makepheno/Trait_1_label.pheno.train  --phenoCol=Phenotype  --covarFile=${dir_RA}/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=${dir_RA}/gwas/Trait_1/geno_Bolt_Trait_1

" > ${dir_RA}/scripts/gwas/geno_Bolt_Trait_1


# I am doing blabla
cd ${dir_RA}/scripts/gwas/

sbatch geno_Bolt_Trait_1
```


## Bolt-lmm-inf T1
```python
##############################
Bolt-inf
##############################
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 32:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"


source /home/lezh/miniconda3/etc/profile.d/conda.sh


${dir}/software/BOLT-LMM_v2.4/bolt --bfile=${dir_data}/geno --phenoFile=${dir_RA}/data/makepheno/Trait_1_label.pheno  --phenoCol=Phenotype  --covarFile=${dir_RA}/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=PC{1:10}  --lmmInfOnly --LDscoresUseChip --numThreads 4  --statsFile=${dir_RA}/gwas/Trait_1/geno_Bolt_inf_Trait_1



" > ${dir_RA}/scripts/gwas/geno_Bolt_inf_Trait_1


# I am doing blabla
cd ${dir_RA}/scripts/gwas/

sbatch geno_Bolt_inf_Trait_1
```

## LDAK run T1

```python
for j in {1..5}; do 
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

${dir_LDAK} --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.train  --covar ${dir_RA}/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile ${dir_RA}/data/geno_train --mpheno $j  --linear ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j

" > ${dir_RA}/scripts/gwas/geno_LDAK_Trait_1_P$j

# I am doing blabla
cd ${dir_RA}/scripts/gwas/
sbatch geno_LDAK_Trait_1_P$j
done
```



## MegaPRS on Trait_1_P1

The previous steps can be reused, see commands_Week1.md

### Construct the prediction model.

```python
for j in {1..5}; do 
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
${dir_LDAK} --mega-prs ${dir_RA}/simulateddata_prs/trait_1/megaprs/trait_1_megabayesr_P$j --model bayesr --ind-hers ${dir_RA}/megaprs/her_ldak_thin/white_thin.thin.ind.hers --summary ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries --cors ${dir_RA}/megaprs/pred_cor/cors_white_total --cv-proportion .1 --high-LD ${dir_RA}/megaprs/highld_white/genes.predictors.used --window-cm 1 --allow-ambiguous YES

" > ${dir_RA}/scripts/simulateddata_prs/trait_1/megaprs/trait_1_megabayesr_pred_P$j


cd ${dir_RA}/scripts/simulateddata_prs/trait_1/megaprs/
sbatch trait_1_megabayesr_pred_P$j
done
``` 


2
Predict Phenotype
```python
for j in {1..5}; do 
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
${dir_LDAK} --calc-scores ${dir_RA}/simulateddata_prs/trait_1/megaprs/trait_1_scores_megaprs_P$j --scorefile ${dir_RA}/simulateddata_prs/trait_1/megaprs/trait_1_megabayesr_P$j.effects --bfile ${dir_RA}/data/geno_test --power 0 --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.test --mpheno $j

" > ${dir_RA}/scripts/simulateddata_prs/trait_1/megaprs/trait_1_scores_megaprs_P$j

cd ${dir_RA}/scripts/simulateddata_prs/trait_1/megaprs/
sbatch trait_1_scores_megaprs_P$j
done

```








## QuickPRS on simulated_traits 1-4

### Quick PRS
Quick PRS is an approximate version of MegaPRS.   
MegaPRS requires the user to compute a tagging file, heritability matrix and predictor-predictor correlations;   
Quick PRS uses versions of these files pre-computed using data from the UK Biobank

1   
We first estimate per-predictor heritabilities by running

```python
for j in {1..5}; do 
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
${dir_LDAK} --sum-hers ${dir_RA}/simulateddata_prs/trait_1/quickprs/trait_1_P$j.bld.ldak --summary ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries.quickprs --tagfile ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.tagging --matrix ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.matrix --check-sums NO

" > ${dir_RA}/scripts/simulateddata_prs/trait_1/quickprs/trait_1_sumher_P$j

cd ${dir_RA}/scripts/simulateddata_prs/trait_1/quickprs/
sbatch trait_1_sumher_P$j
done

``` 

The estimated per-predictor heritabilities are saved in trait_1.bld.ldak.ind.hers   

2   
We then construct a BayesR prediction model by running   
```python
for j in {1..5}; do 
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
${dir_LDAK} --mega-prs ${dir_RA}/simulateddata_prs/trait_1/quickprs/trait_1_P$j.bld.ldak.bayesr --summary ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries.quickprs --ind-hers ${dir_RA}/simulateddata_prs/trait_1/quickprs/trait_1_P$j.bld.ldak.ind.hers --cors ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap --high-LD ${dir_RA}/quickprs/precomputed/gbr.hapmap/highld.snps --model bayesr --cv-proportion .1 --window-cm 1 --extract ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries.quickprs

" > ${dir_RA}/scripts/simulateddata_prs/trait_1/quickprs/trait_1_bayesr_P$j

cd ${dir_RA}/scripts/simulateddata_prs/trait_1/quickprs/
sbatch trait_1_bayesr_P$j
done


``` 

3
Predict Phenotype
```python
for j in {1..5}; do 
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
${dir_LDAK} --calc-scores ${dir_RA}/simulateddata_prs/trait_1/quickprs/trait_1_P$j --scorefile ${dir_RA}/simulateddata_prs/trait_1/quickprs/trait_1_P$j.bld.ldak.bayesr.effects --bfile ${dir_RA}/data/geno2_test --power 0 --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.test  --mpheno $j

" > ${dir_RA}/scripts/simulateddata_prs/trait_1/quickprs/trait_1_score_P$j

cd ${dir_RA}/scripts/simulateddata_prs/trait_1/quickprs/
sbatch trait_1_score_P$j
done

```


### Classical PRS
1.
```python
  for j in {1..5}; do 
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

   ${dir}/software/plink \
    --bfile ${dir_RA}/data/geno2_test \
    --clump-p1 1 \
    --clump-r2 0.1 \
    --clump-kb 250 \
    --clump ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.assoc.classical \
    --clump-snp-field Predictor \
    --clump-field Wald_P \
    --out ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_P$j_classicalprs

      " > ${dir_RA}/scripts/simulateddata_prs/trait_1/classicalprs/geno_LDAK_classicalprs_step1_Trait_1_P$j

    # I am doing blabla
    cd ${dir_RA}/scripts/simulateddata_prs/trait_1/classicalprs/
    sbatch geno_LDAK_classicalprs_step1_Trait_1_P$j

   done
```

```python

   awk 'NR!=1{print $2}' ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_P1_classicalprs.clumped  >  ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_P1_classicalprs.valid.snp
   awk '{print $2,$7}' ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P1.assoc.classical > ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_P1.SNP.pvalue

```


```python

    echo "0.001 0 0.001" > ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_range_list 
    echo "0.05 0 0.05" >> ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_range_list 
    echo "0.1 0 0.1" >> ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_range_list 
    echo "0.2 0 0.2" >> ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_range_list 
    echo "0.3 0 0.3" >> ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_range_list 
    echo "0.4 0 0.4" >> ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_range_list 
    echo "0.5 0 0.5" >> ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_range_list 
```


2
```python

  for j in {1..5}; do 
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

    ${dir}/software/plink \
    --bfile ${dir_RA}/data/geno2_test \
    --score ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.assoc.classical 2 4 8 header \
    --q-score-range ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_range_list  ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_P$j.SNP.pvalue \
    --extract ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_P$j_classicalprs.valid.snp \
    --out ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_classicalprs_Trait_1_P$j

  " > ${dir_RA}/scripts/simulateddata_prs/trait_1/classicalprs/geno_LDAK_classicalprs_step2_Trait_1_P$j

    # I am doing blabla
    cd ${dir_RA}/scripts/simulateddata_prs/trait_1/classicalprs/
    sbatch geno_LDAK_classicalprs_step2_Trait_1_P$j

   done

```
3
```python
    dir="/home/lezh/dsmwpred/zly"
  dir_RA="/home/lezh/dsmwpred/zly/RA"
  dir_data="/home/lezh/dsmwpred/data/ukbb"
  dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
   echo "#"'!'"/bin/bash
    #SBATCH --mem 128G
    #SBATCH -t 10:0:0
    #SBATCH -c 8
    #SBATCH -A dsmwpred

   ${dir}/software/plink \
    --bfile ${dir_RA}/data/geno2_test \
    --indep-pairwise 200 50 0.25 \
    --out ${dir_RA}/data/geno2_test


    ${dir}/software/plink \
      --bfile ${dir_RA}/data/geno2_test \
      --extract ${dir_RA}/data/geno2_test.prune.in \
      --pca 10 \
      --out ${dir_RA}/data/geno2_test


    " > ${dir_RA}/scripts/simulateddata_prs/trait_1/classicalprs/geno_LDAK_Trait_1_classicalprs_step3

    # I am doing blabla
    cd ${dir_RA}/scripts/simulateddata_prs/trait_1/classicalprs/
    sbatch geno_LDAK_Trait_1_classicalprs_step3

```

4. calculate score
```python
for j in {1..1}; do 
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
${dir_LDAK} --calc-scores ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_classicalprs_Trait_1_P$j --scorefile ${dir_RA}/simulateddata_prs/trait_1/classicalprs/geno_LDAK_classicalprs_Trait_1_P$j.bestscore --bfile ${dir_RA}/data/geno_test --power 0 --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.test  --mpheno $j

" > ${dir_RA}/scripts/simulateddata_prs/trait_1/classicalprs/geno_LDAK_classicalprs_bestscore_Trait_1_P$j

cd ${dir_RA}/scripts/simulateddata_prs/trait_1/classicalprs/
sbatch geno_LDAK_classicalprs_bestscore_Trait_1_P$j
done

```




## By megaprs new

### 1. Pre-pre cor

```python
dir_data="/home/lezh/dsmwpred/data/ukbb"
shuf -n 5000 ${dir_data}/geno.fam > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/rand.5000 
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

${dir_LDAK} --calc-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/cors_geno --bfile ${dir_data}/geno --window-cm 3  --keep /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/rand.5000 

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/cors_geno

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/scripts/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/
sbatch cors_geno


``` 

### 2. Prediction Model

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes ${dir_RA}/proj0_megaprs_test/megaprs_new/highld_geno --bfile /home/lezh/dsmwpred/data/ukbb/geno --genefile /home/lezh/snpher/faststorage/highld.txt


```python

for j in {1..5}; do 
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

for j in {1..5}; do 

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/trait_1_megabayesr_P$j --model bayesr --summary ${dir_RA}/proj0_megaprs_test/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/cors_geno --cv-proportion .1 --high-LD ${dir_RA}/proj0_megaprs_test/megaprs_new/highld_geno/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25  --extract ${dir_RA}/proj0_megaprs_test/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries

done

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/trait_1_megabayesr_pred_P$j

# I am doing blabla
/faststorage/project/dsmwpred/zly/RA/scripts/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/
sbatch trait_1_megabayesr_pred_P$j
done
```

### 3. Predict Phenotype

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

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/trait_1_scores_megaprs_P1 --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/megaprs_new/trait_1_megabayesr_P1.effects --bfile ${dir_RA}/data/geno_test --power 0 --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.test --mpheno 1 

" > ${dir_RA}/scripts/megaprs_new/prediction/geno_test_scores_megaprs_new

cd ${dir_RA}/scripts/megaprs_new/prediction
sbatch geno_test_scores_megaprs_new


```



# Run MegaPRS (new) on simulated trait 1 again

## Make Pheno

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir_LDAK} \
  --make-phenos /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/trait_1 \
  --bfile ${dir_data}/geno \
  --weights ${dir_RA}/data/geno_weighting_thin.thin \
  --power -0.25 \
  --her 0.9 \
  --num-phenos 1 \
  --num-causals 50000 \
  --extract ${dir_RA}/data/snps_1_to_12_geno.txt

```
## To get train and test sets
by Rmd


## GWAS by LDAK

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir_LDAK} --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/trait_1.pheno.train  --covar ${dir_RA}/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile ${dir_RA}/data/geno_train --mpheno 1 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/gwas_ldak_trait_1_train

```

## MegaPRS New

### 1. Pre-pre cor

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
shuf -n 5000 ${dir_data}/geno.fam > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/rand.5000 
```
#########################################################

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --calc-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/cors_geno --bfile ${dir_data}/geno --window-cm 3  --keep /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/rand.5000 

``` 

### 1.5 High LD
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/highld_geno --bfile /home/lezh/dsmwpred/data/ukbb/geno --genefile /home/lezh/snpher/faststorage/highld.txt

```


### 2. Prediction Model

```python


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/trait_1_megabayesr --model bayesr --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/gwas_ldak_trait_1_train.summaries --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/cors_geno --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/highld_geno/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/gwas_ldak_trait_1_train.summaries

```

### 3. Predict Phenotype (calculate score)

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/trait_1_score --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/trait_1_megabayesr.effects --bfile ${dir_RA}/data/geno_test --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/megaprs_new_trait_1/trait_1.pheno.test  --mpheno 1 

```



# Run QuickPRS on Trait 1

## Make Pheno

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir_LDAK} \
  --make-phenos /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/trait_1 \
  --bfile ${dir_data}/geno2 \
  --power -1 \
  --her 0.9 \
  --num-phenos 1 \
  --num-causals 50000

```
## To get train and test sets
by Rmd


## GWAS by LDAK

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir_LDAK} --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/trait_1.pheno.train  --covar ${dir_RA}/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile ${dir_RA}/data/geno2_train --mpheno 1 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/gwas_ldak_trait_1_train

```


## 1. estimate h2
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/trait_1.bld.ldak --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/gwas_ldak_trait_1_train.summaries --tagfile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.tagging --matrix /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.matrix --check-sums NO


```

## 2. prediction model

```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/trait_1.bld.ldak.bayesr --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/gwas_ldak_trait_1_train.summaries --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/trait_1.bld.ldak.ind.hers --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap --high-LD /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/highld.snps --model bayesr --cv-proportion .1 --window-cm 1 --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/gwas_ldak_trait_1_train.summaries

```



## 3　Predict Phenotype
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/trait_1_score --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/trait_1.bld.ldak.bayesr.effects --bfile ${dir_RA}/data/geno2_test --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_1/quickprs/Trait_1.pheno.test  --mpheno 1


```



# Trait 2, h2 = 0.3

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir_LDAK} \
  --make-phenos /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/trait_03 \
  --bfile ${dir_data}/geno \
  --power -1 \
  --her 0.3 \
  --num-phenos 1 \
  --num-causals 50000

```
## To get train and test sets
by Rmd

## GWAS by LDAK

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir_LDAK} --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/trait_03.pheno.train  --covar ${dir_RA}/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile ${dir_RA}/data/geno_train --mpheno 1 --linear /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/gwas_ldak_trait_03_train

```



## MegaPRS Old

### Sum Her

```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --sum-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/trait_03_megaold_her.thin --tagfile ${dir_RA}/proj0_megaprs_test/megaprs/her_ldak_thin/white_thin.thin.tagging --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/gwas_ldak_trait_03_train.summaries --matrix ${dir_RA}/proj0_megaprs_test/megaprs/her_ldak_thin/white_thin.thin.matrix


```


### 1. Pre-pre cor

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
shuf -n 5000 ${dir_data}/geno.fam > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/rand.5000 
```
#########################################################

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --calc-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/cors_geno --bfile ${dir_data}/geno --window-cm 3  --keep /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/rand.5000 

``` 

### 1.5 High LD
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/highld_geno --bfile /home/lezh/dsmwpred/data/ukbb/geno --genefile /home/lezh/snpher/faststorage/highld.txt

```




### Construct the prediction model.

```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/trait_03_megabayesr --model bayesr --ind-hers /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/trait_03_megaold_her.thin.ind.hers --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/gwas_ldak_trait_03_train.summaries --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/cors_geno --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/highld_geno/genes.predictors.used --window-cm 1 --allow-ambiguous YES

``` 


2
Predict Phenotype
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/trait_03_scores --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_old/trait_03_megabayesr.effects --bfile ${dir_RA}/data/geno_test --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/trait_03.pheno.test --mpheno 1


```



## MegaPRS New

### 1. Pre-pre cor

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
shuf -n 5000 ${dir_data}/geno.fam > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/rand.5000 
```
#########################################################

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --calc-cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/cors_geno --bfile ${dir_data}/geno --window-cm 3  --keep /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/rand.5000 

``` 

### 1.5 High LD
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/highld_geno --bfile /home/lezh/dsmwpred/data/ukbb/geno --genefile /home/lezh/snpher/faststorage/highld.txt

```


### 2. Prediction Model

```python


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/trait_03_megabayesr --model bayesr --summary /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/gwas_ldak_trait_03_train.summaries --cors /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/cors_geno --cv-proportion .1 --high-LD /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/highld_geno/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25  --extract /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/gwas_ldak_trait_03_train.summaries

```

### 3. Predict Phenotype (calculate score)

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/trait_03_score --scorefile /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/megaprs_new/trait_03_megabayesr.effects --bfile ${dir_RA}/data/geno_test --power 0 --pheno /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/simulateddata_prs/trait_03/trait_03.pheno.test --mpheno 1

```


