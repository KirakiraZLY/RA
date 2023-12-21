# Commands during RA
## Week 5

17/12/2023

# non-iid problem

## high LD region

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/plink --bfile ${dir_noniid_data}/mhc --r2 --ld-window-r2 0.8 --ld-window 50000 --ld-window-kb 1000 --out ${dir_RA}/proj2_noniid_problem/highld/mhc_highld

" > ${dir_RA}/scripts/proj2_noniid_problem/highld/mhc_highld

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/highld/
sbatch mhc_highld
```

### high ld for a single snp

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 20:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir}/software/plink --bfile ${dir_noniid_data}/mhc --r2  --ld-snp 6:25279824:G:A  --ld-window-r2 0 --ld-window 99999 --ld-window-kb 1000  --out ${dir_RA}/proj2_noniid_problem/highld/mhc_highld_6:25279824:G:A  

#${dir}/software/plink --bfile ${dir_RA}/proj2_noniid_problem/pseudo_genotype/smallset  --r2   --ld-window-r2 0 --ld-window 99999 --ld-window-kb 1000  --out ${dir_RA}/proj2_noniid_problem/highld/smallset_highld_nomatrix

" > ${dir_RA}/scripts/proj2_noniid_problem/highld/mhc_highld_6:25279824:G:A  

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/highld/
sbatch mhc_highld_6:25279824:G:A  
```


### By calculating Genetic Correlation

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 4:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --linear ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_1 --bfile ${dir_noniid_data}/mhc --pheno ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_1.pheno
${dir_LDAK} --linear ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_2 --bfile ${dir_noniid_data}/mhc --pheno ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_2.pheno

${dir_LDAK} --sum-cors ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_gencor --summary ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_1.summaries --summary2 ${dir_RA}/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_2.summaries --tagfile ${dir_RA}/proj2_noniid_problem/highld/ldak.thin.genotyped.gbr.tagging --allow-ambiguous YES  --cutoff 0.01  --extract ${dir_RA}/proj2_noniid_problem/mhc_phenotype/snps_only_chr6_mhc.txt

" > ${dir_RA}/scripts/proj2_noniid_problem/highld/genetic_correlation/mhc_trait_1and2_geneticcorrelation

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/highld/genetic_correlation/
sbatch mhc_trait_1and2_geneticcorrelation

```



## "make genotype"
```python
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
${dir_LDAK} --make-snps ${dir_RA}/proj2_noniid_problem/pseudo_genotype/smallset --num-samples 20 --num-snps 100
```

## make phenotype

### 1 Weighting

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

shuf -n 5000 ${dir_noniid_data}/mhc.fam > ${dir_RA}/proj2_noniid_problem/mhc_phenotype/rand.5000 

${dir_LDAK} --bfile ${dir_noniid_data}/mhc  --max-threads 4  --thin ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin  --window-prune 0.98 --window-kb 100 --keep ${dir_RA}/proj2_noniid_problem/mhc_phenotype/rand.5000


" > ${dir_RA}/scripts/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/mhc_phenotype/
sbatch mhc_weighting_thin

```

### 1.5
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
awk < ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin.in '{print $1, 1}' > ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin.thin
```

### 2 SNP extract for mhc, chr == 6
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

conda activate zly2
Rscript ${dir_RA}/proj2_noniid_problem/codes/mhc_snp_extract.R
```

### 3 Simulating 
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} \
  --make-phenos ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_2 \
  --bfile ${dir_noniid_data}/mhc \
  --weights ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_weighting_thin.thin \
  --power -0.25 \
  --her 0.1 \
  --num-phenos 1 \
  --num-causals 5000 \
  --extract ${dir_RA}/proj2_noniid_problem/mhc_phenotype/snps_only_chr6_mhc.txt

" > ${dir_RA}/scripts/proj2_noniid_problem/mhc_phenotype/mhc_trait_2.sh

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/mhc_phenotype/
sbatch mhc_trait_2.sh
```

## Make Summary Statistics
By LDAK
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"
echo "#"'!'"/bin/bash
#SBATCH --mem 8G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --pheno ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_1.pheno --max-threads 4  --bfile ${dir_noniid_data}/mhc  --linear ${dir_RA}/proj2_noniid_problem/summarystatistics/mhc_ldak_trait_1

" > ${dir_RA}/scripts/proj2_noniid_problem/summarystatistics/mhc_ldak_trait_1

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/summarystatistics/
sbatch mhc_ldak_trait_1

```

## Make phenotype by smallset
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

${dir_LDAK} \
  --make-phenos ${dir_RA}/proj2_noniid_problem/pseudo_genotype/smallset_pheno \
  --bfile ${dir_RA}/proj2_noniid_problem/pseudo_genotype/smallset \
  --ignore-weights YES  \
  --power -1 \
  --her 0.5 \
  --num-phenos 1 \
  --num-causals 5

```

## Run PRS on an example data
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python ${dir_RA}/proj2_noniid_problem/codes/Transformer_PRS/main.py --bfile ${dir_noniid_data}/mhc  --phenoFile ${dir_RA}/proj2_noniid_problem/mhc_phenotype/mhc_trait_1.pheno  --out ${dir_RA}/proj2_noniid_problem/results/mhc_result

" > ${dir_RA}/scripts/proj2_noniid_problem/results/mhc_result

# I am doing blabla
cd ${dir_RA}/scripts/proj2_noniid_problem/results/
sbatch mhc_result
```




# Bolt Predict
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"
echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
${dir_LDAK} --bolt ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/geno_train_Trait1_bolt_prs --LDpred YES --bfile ${dir_RA}/data/geno_train --pheno ${dir_RA}/data/makepheno/Trait_1.pheno.train --LOCO NO  --mpheno 1

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/bolt_pred/geno_train_Trait1_bolt_prs

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/bolt_pred/
sbatch geno_train_Trait1_bolt_prs

```

## Example
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_noniid_data="/home/lezh/dsmwpred/ml"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"
echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 20:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred

${dir_LDAK} --make-snps ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake --num-samples 10000 --num-snps 10000
${dir_LDAK} --make-phenos ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake --num-phenos 1 --her .3 --power -1 --num-causals 100 --bfile ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake

${dir_LDAK}  --bolt ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/ldpred_fake --LDpred YES --bfile ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake --pheno ${dir_RA}/proj1_testprs_finngen_ukbb/bolt_pred/fake.pheno --LOCO NO

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/bolt_pred/ldpred_fake

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/bolt_pred/
sbatch ldpred_fake
```

