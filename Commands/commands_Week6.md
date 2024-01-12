# Commands during RA
# Week 6

1/7/2024



## Mega-prs Asthma

########

cd /home/doug/dsmwpred/doug/leyi/asthma

#leyi gave me manifest - note that this is a bit old (R8 - latest version is R10)

########


#download finngen ss for asthma allergies (manifest gave link)
wget https://storage.googleapis.com/finngen-public-data-r8/summary_stats/finngen_R8_ASTHMA_ALLERG.gz


#convert to ldak format, keeping only snps consistent with those in /home/doug/dsmwpred/data/ukbb/geno3.bim
#note that manisfest says sample size is 4106 + 193857

gunzip -c finngen_R8_ASTHMA_ALLERG.gz | awk '(NR==FNR){a[$2]=$5$6;next}(FNR==1){print "Predictor A1 A2 Direction P n"}($5 in a && (a[$5]==$3$4 || a[$5]==$4$3)){print $5, $4, $3, $9, $7, 4106 + 193857}' /home/lezh/dsmwpred/data/ukbb/geno3.bim - > asthma.txt


#make prs

#shuf -n 5000 /home/lezh/dsmwpred/data/ukbb/geno3.fam > rand.5000
/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors cors --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --keep rand.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes highld --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --genefile /home/lezh/snpher/faststorage/highld.txt

/home/lezh/snpher/faststorage/ldak5.2.linux --mega-prs asthma.bayesr --extract asthma.txt --allow-ambiguous YES --cors cors --high-LD highld/genes.predictors.used --summary asthma.txt --model bayesr --power -.25 --max-threads 4


#test using ukbb asthma phenotype (/home/doug/snpher/faststorage/biobank/newphens/icdphens/code4648.pheno)

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-scores test.asthma.bayesr --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --power 0 --scorefile asthma.bayesr.effects --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code4648.pheno --max-threads 4

/home/doug/ldak5.2.linux --jackknife test.asthma.bayesr --profile test.asthma.bayesr.profile --num-blocks 200 --AUC YES --prevalence 0.02



## New MegaPRS
### 1. Pre-pre cor

```python
dir_data="/home/lezh/dsmwpred/data/ukbb"
shuf -n 5000 ${dir_data}/geno2.fam > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test/rand.5000 
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

${dir_LDAK} --calc-cors /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test/asthma_megaprs_mine --bfile ${dir_data}/geno2 --window-cm 3  --keep /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test/rand.5000 

" > ${dir_RA}/scripts/megaprs_new/pred_cor/geno_train_cors

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/pred_cor/
sbatch geno_train_cors
done
``` 

### 2. Prediction Model


/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes highld_geno2 --bfile /home/lezh/dsmwpred/data/ukbb/geno2 --genefile /home/lezh/snpher/faststorage/highld.txt


```python

for j in list
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
$j
${dir_LDAK} --mega-prs /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test/asthma_megaprs_mine_2 --model bayesr --summary ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/finngen_R8_ASTHMA_ALLERG.ss.extrac --cors /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test/asthma_megaprs_mine --cv-proportion .1 --high-LD /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test/highld_geno2/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25  --extract ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/finngen_R8_ASTHMA_ALLERG.ss.extrac


" > ${dir_RA}/scripts/megaprs_new/geno_train_megabayesr 

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/
sbatch geno_train_megabayesr
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
${dir_LDAK} --calc-scores /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test/asthma_megaprs_mine_score_3 --scorefile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test/asthma_megaprs_mine_2.effects --bfile ${dir_data}/geno2 --power 0 --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code4648.pheno  --extract ${dir_RA}/proj1_testprs_finngen_ukbb/ss_extract/finngen_R8_ASTHMA_ALLERG.ss.extrac

" > ${dir_RA}/scripts/megaprs_new/prediction/geno_test_scores_megaprs_new

cd ${dir_RA}/scripts/megaprs_new/prediction
sbatch geno_test_scores_megaprs_new


```


## QuickPRS Asthma
cd /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/test

1
#make prs
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
icd10="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_list.txt"
finngen_ss_link="/home/lezh/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode_withprefix.txt"
finngen_ss_name="/home/lezh/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode.txt"
finngen_42phenos="/home/lezh/dsmwpred/zly/RA/data/FinnGen/finngen_42phenos.txt"

${dir_LDAK} --sum-hers asthma_quickprs_1 --summary asthma.txt --tagfile ${dir_RA}/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.tagging --matrix ${dir_RA}/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap.bld.ldak.quickprs.matrix --check-sums NO  --fixed-n 300000
```

2.
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
icd10="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_list.txt"
finngen_ss_link="/home/lezh/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode_withprefix.txt"
finngen_ss_name="/home/lezh/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode.txt"
finngen_42phenos="/home/lezh/dsmwpred/zly/RA/data/FinnGen/finngen_42phenos.txt"

${dir_LDAK} --mega-prs asthma_quickprs_2 --summary asthma.txt --ind-hers asthma_quickprs_1.ind.hers --cors ${dir_RA}/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/gbr.hapmap --high-LD ${dir_RA}/proj0_megaprs_test/quickprs/precomputed/gbr.hapmap/highld.snps --model bayesr --cv-proportion .1 --window-cm 1  --fixed-n 300000  --extract asthma.txt
```

3.
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
icd10="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/icd10_100pheno_list.txt"
finngen_ss_link="/home/lezh/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode_withprefix.txt"
finngen_ss_name="/home/lezh/dsmwpred/zly/RA/data/FinnGen/list_100_ss_phenocode.txt"
finngen_42phenos="/home/lezh/dsmwpred/zly/RA/data/FinnGen/finngen_42phenos.txt"

${dir_LDAK} --calc-scores asthma_quickprs_3.scores --scorefile asthma_quickprs_2.bayesr.effects  --bfile ${dir_data}/geno3 --power 0 --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code4648.pheno
```


#shuf -n 5000 /home/lezh/dsmwpred/data/ukbb/geno3.fam > rand.5000
/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors cors --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --keep rand.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes highld --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --genefile /home/lezh/snpher/faststorage/highld.txt

/home/lezh/snpher/faststorage/ldak5.2.linux --mega-prs asthma.bayesr --extract asthma.txt --allow-ambiguous YES --cors cors --high-LD highld/genes.predictors.used --summary asthma.txt --model bayesr --power -.25 --max-threads 4


#test using ukbb asthma phenotype (/home/doug/snpher/faststorage/biobank/newphens/icdphens/code4648.pheno)

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-scores test.asthma.bayesr --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --power 0 --scorefile asthma.bayesr.effects --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code4648.pheno --max-threads 4

/home/doug/ldak5.2.linux --jackknife test.asthma.bayesr --profile test.asthma.bayesr.profile --num-blocks 200 --AUC YES --prevalence 0.02



# For 100 phenotypes


## Converting to LDAK format, consistent with geno3.
convert to ldak format, keeping only snps consistent with those in /home/doug/dsmwpred/data/ukbb/geno3.bim
#note that manisfest says sample size is 4106 + 193857

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

    linecleanedstringgz=()
    for p in $linecleanedstring; do 
    linecleanedstringqc+=("$p.qc"); 
    done

    linecleanedstringout=()
    for p in $linecleanedstring; do 
    linecleanedstringqc+=("$p.ldak"); 
    done

    #echo -e $j $linecleanedstringqc

    #gunzip -c $linecleanedstringgz | awk '(NR==FNR){a[$2]=$5$6;next}(FNR==1){print "Predictor A1 A2 Direction P"}($5 in a && (a[$5]==$3$4 || a[$5]==$4$3)){print $5, $4, $3, $9, $7}' /home/lezh/dsmwpred/data/ukbb/geno3.bim - > $linecleanedstringout

    awk '(NR==FNR){a[$2]=$5$6;next}(FNR==1){print "Predictor A1 A2 Direction P"}($5 in a && (a[$5]==$3$4 || a[$5]==$4$3)){print $5, $4, $3, $9, $7}' /home/lezh/dsmwpred/data/ukbb/geno3.bim $linecleanedstringgz - > $linecleanedstringout

    #awk '(NR==FNR){a[$2]=$5$6;next}(FNR==1){print "Predictor A1 A2 Direction P"}($5 in a && (a[$5]==$3$4 || a[$5]==$4$3)){print $5, $4, $3, $9, $7}' $linecleanedstringgz /home/lezh/dsmwpred/data/ukbb/geno3.bim - > $linecleanedstringout
done

```

### Using My Proj3 Code
1. ss -> addn
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

linecleanedstringgz=()
for p in $linecleanedstring; do 
linecleanedstringqc+=("$p.qc"); 
done

linecleanedstringout=()
for p in $linecleanedstring; do 
linecleanedstringqc+=("$p.ldak"); 
done

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 3:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/finngen_ss_add_n.R --inputFile ${linecleanedstring}  --fileName  ${linenamecleaned}  --outputFile ${linecleanedstring}.addn

echo $j

" > /home/lezh/dsmwpred/zly/RA/scripts/data/FinnGen/addn/${linenamecleaned}.addn.sh

# I am doing blabla
cd /home/lezh/dsmwpred/zly/RA/scripts/data/FinnGen/addn/
sbatch ${linenamecleaned}.addn.sh

done

```

2. addn -> ldak
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

linecleanedstringgz=()
for p in $linecleanedstring; do 
linecleanedstringqc+=("$p.qc"); 
done

linecleanedstringout=()
for p in $linecleanedstring; do 
linecleanedstringqc+=("$p.ldak"); 
done

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /home/lezh/dsmwpred/zly/RA/proj3_ss_to_ldak_format/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/finngen_R8_${linenamecleaned}.addn  --outputFile ${linecleanedstring}.ldak  --bfile /home/lezh/dsmwpred/data/ukbb/geno3


" > /home/lezh/dsmwpred/zly/RA/scripts/data/FinnGen/ldak/${linenamecleaned}.ldak.sh

# I am doing blabla
cd /home/lezh/dsmwpred/zly/RA/scripts/data/FinnGen/ldak/
sbatch ${linenamecleaned}.ldak.sh



done


```

## Mega PRS New

### Step 1
```python
shuf -n 5000 /home/lezh/dsmwpred/data/ukbb/geno3.fam > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/rand_geno3.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/cors_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --keep /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/rand_geno3.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/highld_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --genefile /home/lezh/snpher/faststorage/highld.txt


```

### Step 2 Make Model
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

linecleanedstringout=()
for p in $linecleanedstring; do 
linecleanedstringout+=("$p.ldak"); 
done

linecleanedsh=()
for p in $linenamecleaned; do 
linecleanedsh+=("$p.sh"); 
done

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --mega-prs /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/${linenamecleaned}.megaprs.new --allow-ambiguous YES --cors /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/cors_geno3 --high-LD /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/highld_geno3/genes.predictors.used --summary $linecleanedstringout --model bayesr --power -.25 --max-threads 4  --extract $linecleanedstringout

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_R8_$linecleanedsh

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/
sbatch finngen_R8_$linecleanedsh

done

```



#test using ukbb asthma phenotype (/home/doug/snpher/faststorage/biobank/newphens/icdphens/code4648.pheno)

### Step 3 Predicting on UKBB
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
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

linecleanedstringout=()
for p in $linecleanedstring; do 
linecleanedstringout+=("$p.ldak"); 
done

linenamecleanedscore=()
for p in $linenamecleaned; do 
linenamecleanedscore+=("$p.megaprs.new.score"); 
done

linecleanedsh=()
for p in $linenamecleaned; do 
linecleanedsh+=("$p.score.sh"); 
done

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-scores /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/prediction/finngen_R8_${linenamecleanedscore} --power 0 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --scorefile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/${linenamecleaned}.megaprs.new.effects  --pheno /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/finngen_R8_${linenamecleaned}.pheno --max-threads 4

" > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/finngen_R8_$linecleanedsh

# I am doing blabla
cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/
sbatch finngen_R8_$linecleanedsh

done


```

### Step 3 Predicting on UKBB, test only on code4648 with Asthma
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-scores /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/prediction/finngen_R8_ASTHMA_ALLERG --power 0 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --scorefile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/ASTHMA_ALLERG.megaprs.new.effects  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code4648.pheno --max-threads 4

```


```python

/home/lezh/snpher/faststorage/ldak5.2.linux --jackknife /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/prediction/finngen_R8_ASTHMA_ALLERG.bayesr --profile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/prediction/finngen_R8_ASTHMA_ALLERG.profile --num-blocks 200 --AUC YES --prevalence 0.02
```



# FinnGen R10 icd10

## Download
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss

2409 in total

另外，有一个包含全部948个ukbb traits位置的文件
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_to_copy.txt
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 4G
#SBATCH -t 30:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

wget -i /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_links.txt -P /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/finngen_icd10/fg_icd10_download

cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/finngen_icd10/
sbatch fg_icd10_download

```

## Unzip
```python


gunzip /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/*



dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_links.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

for j in {1..2409}; do

line=$(head -n $j $ss_filename | tail -n 1)
linename=$(head -n $j $ss_name_filename | tail -n 1)
linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')


echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 2:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

gunzip /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_${linenamecleaned}.gz

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/finngen_icd10/unzip/fg_icd10_gunzip_finngen_R10_${linenamecleaned}.sh

echo ${j} ${linenamecleaned}

cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/finngen_icd10/unzip/
sbatch fg_icd10_gunzip_finngen_R10_${linenamecleaned}.sh

echo ${j}

done


```


## Convert
1. ss -> addn
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do

line=$(head -n $j $ss_filename | tail -n 1)
linename=$(head -n $j $ss_name_filename | tail -n 1)
linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

linecleanedstringgz=()
for p in $linecleanedstring; do 
linecleanedstringqc+=("$p.qc"); 
done

linecleanedstringout=()
for p in $linecleanedstring; do 
linecleanedstringqc+=("$p.ldak"); 
done

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 3:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/finngen_ss_add_n.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_${linenamecleaned}  --fileName  ${linenamecleaned}  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.addn

echo $j

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/ldak_format/${linenamecleaned}.addn.sh

# I am doing blabla
cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/ldak_format/
sbatch ${linenamecleaned}.addn.sh

done

```

2. addn -> ldak
```python


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

for j in {1..551}; do


line=$(head -n $j $ss_filename | tail -n 1)
linename=$(head -n $j $ss_name_filename | tail -n 1)
linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /home/lezh/dsmwpred/zly/RA/proj3_ss_to_ldak_format/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.addn  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak  --bfile /home/lezh/dsmwpred/data/ukbb/geno3

echo $j


" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/ldak_format/${linenamecleaned}.ldak.sh

# I am doing blabla
cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/ldak_format
sbatch ${linenamecleaned}.ldak.sh

done


```

## Combine all traits of UKBB into one table
For jackknife use
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_test.txt
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ukbb_icd10_combine.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_to_copy.txt  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/ukbb_phenotype_948_all.pheno  --bfile /home/lezh/dsmwpred/data/ukbb/geno3

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/ldak_format/ukbb_combine

# I am doing blabla
cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/data/ldak_format/
sbatch ukbb_combine

```




## Mega PRS New

### Step 1 有了不用跑，直接调用
```python
shuf -n 5000 /home/lezh/dsmwpred/data/ukbb/geno3.fam > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/rand_geno3.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/cors_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --keep /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/rand_geno3.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/highld_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --genefile /home/lezh/snpher/faststorage/highld.txt


```

### Step 2 Make Model
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do

line=$(head -n $j $ss_filename | tail -n 1)
linename=$(head -n $j $ss_name_filename | tail -n 1)
linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

linenamecleanedstringout=()
for p in $linenamecleaned; do 
linenamecleanedstringout+=("$p.ldak"); 
done

linecleanedsh=()
for p in $linenamecleaned; do 
linecleanedsh+=("$p.sh"); 
done

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --mega-prs /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/finngen_R10_${linenamecleaned}.megaprs.new --allow-ambiguous YES --cors /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/cors_geno3 --high-LD /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/pheno100/megaprs_new/highld_geno3/genes.predictors.used --summary /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak --model bayesr --power -.25 --max-threads 4  --extract /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ldak_format/finngen_R10_${linenamecleaned}.ldak

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/finngen_R10_${linenamecleaned}.sh

# I am doing blabla
cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/
sbatch finngen_R10_${linenamecleaned}.sh

done


```



### Step 3 Predicting, without checking
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/100icd10/
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do
echo $j
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

${dir_LDAK} --calc-scores /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred --power 0 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --scorefile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/finngen_R10_${linenamecleaned}.megaprs.new.effects  

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.sh

# I am doing blabla

cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/

done

```

```python

for j in {1..551}; do
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
sbatch finngen_R10_${linenamecleaned}.sh

done


```

### Step 4, jackknife
/home/doug/ldak5.2.linux --jackknife test.asthma.bayesr --profile test.asthma.bayesr.profile --num-blocks 200 --AUC YES --prevalence 0.02

```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do

line=$(head -n $j $ss_filename | tail -n 1)
linename=$(head -n $j $ss_name_filename | tail -n 1)
linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')



echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 16:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

while IFS= read -r path2; do

/home/lezh/snpher/faststorage/ldak5.2.linux --jackknife /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleanedscore} --profile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleanedscore} --num-blocks 200 --AUC YES --prevalence 0.02  --pheno $path2

done < "/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_to_copy.txt"

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleaned}.sh

# I am doing blabla
cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife
sbatch finngen_R10_${linenamecleaned}.sh

done


```


### Step 4, my jackknife
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do
echo $j
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 4:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/jackknife_onecolumn_and_theothers.R --scoreFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife  --phenoFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/ukbb_phenotype_948_all.pheno

" > /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife.sh

# I am doing blabla

cd /home/lezh/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/
sbatch finngen_R10_${linenamecleaned}.megaprs.new.jackknife.sh

done


```

### Combine all traits of UKBB into one table
/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_test.txt
```python

conda activate zly2
Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ukbb_icd10_combine.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/icd10_alltraits_to_copy.txt  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_ukbb/all948/ukbb_phenotype_948_all.pheno  --bfile /home/lezh/dsmwpred/data/ukbb/geno3


```

### Combine all PRS of MegaPRS into one table
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

for i in {1..551}; do

linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
awk '{print $5}' "/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile" > "/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_${linenamecleaned}.txt"

done
paste /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_*.txt > megaprs_new_pred_merged.txt

rm /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_*.txt
```