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

${dir_LDAK} --bfile ${dir_data}/geno --noweb --keep ${dir_RA}/data/geno_train.fam --recode --make-bed --out ${dir_RA}/data/geno_train

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
#SBATCH --mem 8G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --bfile ${dir_data}/geno --noweb --keep ${dir_RA}/data/geno_test.fam --recode --make-bed --out ${dir_RA}/data/geno_test

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

${dir}/software/BOLT-LMM_v2.4/bolt --bfile=${dir_data}/geno --phenoFile=${dir_RA}/data/makepheno/Trait_1_label.pheno  --phenoCol=Phenotype  --covarFile=${dir_RA}/data/geno.sex.townsend.age.pcs_label.covars --qCovarCol=PC{1:10}  --lmmForceNonInf --LDscoresUseChip --numThreads 4  --statsFile=${dir_RA}/gwas/Trait_1/geno_Bolt_Trait_1

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

### LDAK run T1

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

${dir_LDAK} --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.train  --covar ${dir_RA}/data/geno.sex.townsend.age.pcs.covars --max-threads 4  --bfile ${dir_data}/geno --mpheno $j  --linear ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j

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
${dir_LDAK} --mega-prs ${dir_RA}/simulateddata_prs/trait_2/megaprs/trait_2_megabayesr_P$j --model bayesr --ind-hers ${dir_RA}/megaprs/her_ldak_thin/white_thin.thin.ind.hers --summary ${dir_RA}/gwas/Trait_2/geno_LDAK_Trait_2_P$j.summaries --cors ${dir_RA}/megaprs/pred_cor/cors_white_total --cv-proportion .1 --high-LD ${dir_RA}/megaprs/highld_white/genes.predictors.used --window-cm 1 --allow-ambiguous YES

" > ${dir_RA}/scripts/simulateddata_prs/trait_2/megaprs/trait_2_megabayesr_pred_P$j


cd ${dir_RA}/scripts/simulateddata_prs/trait_2/megaprs/
sbatch trait_2_megabayesr_pred_P$j
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
${dir_LDAK} --calc-scores ${dir_RA}/simulateddata_prs/trait_1/megaprs/trait_1_scores_megaprs_P$j --scorefile ${dir_RA}/simulateddata_prs/trait_1/megaprs/trait_1_megabayesr_P$j.effects --bfile ${dir_data}/geno --power 0 --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.test --mpheno $j

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
${dir_LDAK} --sum-hers ${dir_RA}/simulateddate_prs/trait_1/quickprs/trait_1_P$j.bld.ldak --summary ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries --tagfile ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.tagging --matrix ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.matrix --check-sums NO

" > ${dir_RA}/scripts/simulateddata_prs/trait_1/quickprs/trait_1_sumher_P$j

cd ${dir_RA}/scripts/simulateddata_prs/trait_1/quickprs/
sbatch trait_1_sumher_P$j
done

``` 

The estimated per-predictor heritabilities are saved in white_train.bld.ldak.ind.hers   

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
${dir_LDAK} --mega-prs ${dir_RA}/simulateddate_prs/trait_1/quickprs/trait_1_P$j.bld.ldak.bayesr --summary ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries --ind-hers ${dir_RA}/quickprs/white_train.bld.ldak.ind.hers --cors ${dir_RA}/quickprs/precomputed/gbr.hapmap/gbr.hapmap --high-LD ${dir_RA}/quickprs/precomputed/gbr.hapmap/highld.snps --model bayesr --cv-proportion .1 --window-cm 1 --extract ${dir_RA}/megaprs/white_train.summaries.quickprs

" > ${dir_RA}/scripts/quickprs/per_pred_her/white_train_bayesr

cd ${dir_RA}/scripts/quickprs/per_pred_her/
sbatch white_train_bayesr
done
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



### Classical PRS by Plink 

1. Basic data: ${dir_RA}/gwas/Trait_1/geno_LDAK_Trait_1_P$j.summaries  
   Target data: ${dir_data}/height.test   
2. Clumping + Threshold
   ```python
   dir="/home/lezh/dsmwpred/zly"

   echo "#"'!'"/bin/bash
    #SBATCH --mem 32G
    #SBATCH -t 10:0:0
    #SBATCH -c 8
    #SBATCH -A dsmwpred

   ${dir}/software/plink \
    --bfile ${dir}/newdata/new_data_qc \
    --clump-p1 1 \
    --clump-r2 0.1 \
    --clump-kb 250 \
    --clump ${dir}/Real_Traits/bmi/data_qc_Bolt_bmi \
    --clump-snp-field SNP \
    --clump-field P_BOLT_LMM \
    --out ${dir}/Real_Traits/PRS/bmi/data_qc_bmi

   awk 'NR!=1{print $3}' ${dir}/Real_Traits/PRS/bmi/data_qc_bmi.clumped  >  ${dir}/Real_Traits/PRS/bmi/data_qc_bmi.valid.snp
   awk '{print $1,$12}' ${dir}/Real_Traits/bmi/data_qc_Bolt_bmi > ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_SNP.pvalue

    echo "0.001 0 0.001" > ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_range_list 
    echo "0.05 0 0.05" >> ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_range_list
    echo "0.1 0 0.1" >> ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_range_list
    echo "0.2 0 0.2" >> ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_range_list
    echo "0.3 0 0.3" >> ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_range_list
    echo "0.4 0 0.4" >> ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_range_list
    echo "0.5 0 0.5" >> ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_range_list

    ${dir}/software/plink \
    --bfile ${dir}/newdata/new_data_qc \
    --score ${dir}/Real_Traits/bmi/data_qc_Bolt_bmi 1 5 9 header \
    --q-score-range ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_range_list ${dir}/Real_Traits/PRS/bmi/data_qc_bmi_SNP.pvalue \
    --extract ${dir}/Real_Traits/PRS/bmi/data_qc_bmi.valid.snp \
    --out ${dir}/Real_Traits/PRS/bmi/data_qc_bmi
    ```

    ```python
    dir="/home/lezh/dsmwpred/zly"

   echo "#"'!'"/bin/bash
    #SBATCH --mem 32G
    #SBATCH -t 10:0:0
    #SBATCH -c 8
    #SBATCH -A dsmwpred
   ${dir}/software/plink \
    --bfile ${dir}/newdata/new_data_qc \
    --indep-pairwise 200 50 0.25 \
    --out ${dir}/Real_Traits/PRS/bmi/data_qc_bmi
    # Then we calculate the first 10 PCs
    ${dir}/software/plink \
        --bfile ${dir}/newdata/new_data_qc \
        --extract ${dir}/Real_Traits/PRS/bmi/data_qc_bmi.prune.in \
        --pca 10 \
        --out ${dir}/Real_Traits/PRS/bmi/data_qc_bmi


    " > ${dir}/scripts/Real_Traits/PRS/bmi/data_qc_bmi_2

    # I am doing blabla
    cd ${dir}/scripts/Real_Traits/PRS/bmi/
    sbatch data_qc_bmi_2
    ```
3. Finding the "best-fit" PRS
        **In Rmd** 