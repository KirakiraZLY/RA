# Commands during RA
## Week 3

12/4/2023

# New MegaPRS
## 1. Pre-pre cor

```python
dir_data="/home/lezh/dsmwpred/data/ukbb"
shuf -n 5000 ${dir_data}/geno.fam > ${dir_RA}/megaprs_new/pred_cor/rand.5000 
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

${dir_LDAK} --calc-cors ${dir_RA}/megaprs_new/pred_cor/geno_train_cors --bfile ${dir_data}/geno --window-cm 3  --keep ${dir_RA}/scripts/megaprs_new/pred_cor/rand.5000

" > ${dir_RA}/scripts/megaprs_new/pred_cor/geno_train_cors

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/pred_cor/
sbatch geno_train_cors
done
``` 

## 2. Prediction Model


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
${dir_LDAK} --mega-prs ${dir_RA}/megaprs_new/geno_train_megabayesr --model bayesr --summary ${dir_RA}/megaprs/white_train.summaries --cors ${dir_RA}/megaprs/pred_cor/cors_white_total --cv-proportion .1 --high-LD ${dir_RA}/megaprs/highld_white/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25


" > ${dir_RA}/scripts/megaprs_new/geno_train_megabayesr

# I am doing blabla
cd ${dir_RA}/scripts/megaprs_new/
sbatch geno_train_megabayesr
```

## 3. Predict Phenotype

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
${dir_LDAK} --calc-scores ${dir_RA}/megaprs_new/prediction/geno_test_scores_megaprs_new --scorefile ${dir_RA}/megaprs_new/geno_train_megabayesr.effects --bfile ${dir_data}/geno --power 0 --pheno ${dir_data}/height.test

" > ${dir_RA}/scripts/megaprs_new/prediction/geno_test_scores_megaprs_new

cd ${dir_RA}/scripts/megaprs_new/prediction
sbatch geno_test_scores_megaprs_new


```



# On 100 phenotypes from FinnGen

## Download
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh

wget -i ${dir_RA}/data/FinnGen/list_100_ss_links.txt -P ${dir_RA}/data/FinnGen/summarystatistics/

" > ${dir_RA}/scripts/data/FinnGen/ss_100_download

cd ${dir_RA}/scripts/data/FinnGen/
sbatch ss_100_download


```

## Unzip
```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
#SBATCH --constraint \"s05\"
source /home/lezh/miniconda3/etc/profile.d/conda.sh

gunzip ${dir_RA}/data/FinnGen/summarystatistics/*

" > ${dir_RA}/scripts/data/FinnGen/ss_100_gunzip

cd ${dir_RA}/scripts/data/FinnGen/
sbatch ss_100_gunzip


```


### Try to make a loop in the list.

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"
for j in {1..5}; do
    line=$(head -n $j $ss_filename | tail -n 1)
    linename=$(head -n $j $ss_name_filename | tail -n 1)
    linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
    linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')
    a=()
    for p in "$linenamecleaned"; do a+=("$p.bed"); done
    echo -e $linecleanedstring
    echo -e $linenamecleaned
    echo -e $p
done
```


### Construct the prediction model.

Using 100 SS in the list.

```python


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"


for j in {1..5}; do

    line=$(head -n $j $ss_filename | tail -n 1)
    linename=$(head -n $j $ss_name_filename | tail -n 1)
    linecleanedstring=$(echo -n "$line" | tr -d '\r\n')
    linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

    echo "#"'!'"/bin/bash
    #SBATCH --mem 16G
    #SBATCH -t 8:0:0
    #SBATCH -c 4
    #SBATCH -A dsmwpred
    #SBATCH --constraint \"s05\"
    source /home/lezh/miniconda3/etc/profile.d/conda.sh



    ${dir_LDAK} --mega-prs ${dir_RA}/proj1_testprs_finngen_ukbb/megaprs_new/prediction/megabayesr_$linename --model bayesr --summary $linecleanedstring --cors ${dir_RA}/megaprs/pred_cor/cors_white_total --cv-proportion .1 --high-LD ${dir_RA}/megaprs/highld_white/genes.predictors.used --window-cm 1 --allow-ambiguous YES  --power -0.25

    " > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/megabayesr_$linename

    cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/megaprs_new/prediction/
    sbatch megabayesr_$linename

done
``` 






# Liftover, Modifying FinnGen SS, QC

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 10:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript ${dir_RA}/data/FinnGen/finn_gen_qc.R


" > ${dir_RA}/scripts/data/FinnGen/finn_gen_qc.sh

cd ${dir_RA}/scripts/data/FinnGen/
sbatch finn_gen_qc.sh

```







## Liftover, Deleting the title of SS files (SKIP)
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

    linecleanedstringqc=()
    for p in $linecleanedstring; do 
    linecleanedstringqc+=("$p.qc"); 
    done

    linecleanedstringwithouttitle=()
    for p in $linecleanedstring; do 
    linecleanedstringwithouttitle+=("$p.notitle"); 
    done

    linenamecleanednotitle=()
    for p in $linenamecleaned; do 
    linenamecleanednotitle+=("$p.notitle.sh"); done

    echo -e $j $linecleanedstringqc

    tail -n +2 $linecleanedstringqc > $linecleanedstringwithouttitle

done

```

## Liftover, SS -> bed

https://www.biostars.org/p/9476954/   

https://groups.google.com/a/soe.ucsc.edu/g/genome/c/8dN0d5-N61Q   


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

    linecleanedstringqc=()
    for p in $linecleanedstring; do 
    linecleanedstringqc+=("$p.qc"); 
    done
    
    linecleanedstringwithouttitle=()
    for p in "$linecleanedstring"; do linecleanedstringwithouttitle+=("$p.notitle"); done
    linecleanedstringbed=()
    for p in "$linecleanedstring"; do linecleanedstringbed+=("$p.bed"); done
    linenamecleanedbedscript=()
    for p in "$linenamecleanedbed"; do linenamecleanedbedscript+=("$p.sh"); done

    echo -e $j $linecleanedstringqc  $linecleanedstringbed

    #awk '{print "chr"$1, ($2-1), $2, $3, $4, $5, $6, $7, $8, $9}'  $linecleanedstringwithouttitle > ${dir_RA}/data/FinnGen/summarystatistics/liftover_hg19/$linenamecleanedbed

    awk 'NR>1 {print "chr"$1, ($2-1), $2, $5}'  $linecleanedstringqc > $linecleanedstringbed

done


```




## By using R

```python


cd /faststorage/project/dsmwpred/takiy/analysis12_biobanks_finngen/1_data/finngen_sumstats_folder/ # example using my folder

conda activate r4 # use R envirenment
R
library(data.table)
#read sumstat
sumstat = fread("/faststorage/project/dsmwpred/takiy/analysis12_biobanks_finngen/1_data/finngen_sumstats_folder/finngen_R8_ASTHMA_ALLERG.gz") # example using finngen_R8_ASTHMA_ALLERG.gz sumstat
setnames(sumstat,"#chrom","chrom")
summary(sumstat)
# some qc (remove non SNP varaints, MAF <0.01, info if available)
sumstat_qc1 = sumstat[nchar(ref)==1 & nchar(alt)==1 & (af_alt_cases>=0.01 & af_alt_cases<=0.99) & (af_alt_controls>=0.01 & af_alt_controls<=0.99),]

# hg38 to hg19
sumstat_qc1[,c("CHR_hg38","start","end","pos_hg38"):=.(paste0("chr",chrom),pos,pos,pos)]
sumstat_qc1[CHR_hg38=="chr23",CHR_hg38:="chrX"]

library(rtracklayer) # need to install rtracklayer from bioconductor repository conda install -c bioconda bioconductor-rtracklayer
path = system.file(package="liftOver", "extdata", "hg38ToHg19.over.chain")
ch = import.chain(path)
ch

sumstat_qc1_granges = makeGRangesFromDataFrame(sumstat_qc1,seqnames.field="CHR_hg38",start.field="start",end.field="end",keep.extra.columns=T)
sumstat_qc1_granges_res = data.table(as.data.frame(liftOver(sumstat_qc1_granges,ch)))
sumstat_qc1_granges_res [,pos_hg19 :=start]
sumstat_qc1_granges_res[,posid_hg19 := paste0(chrom,":",pos_hg19)]

# reformat sumstat keeping only columns of interst then saving
#rio::export(sumstat_qc1_format,"path/sumstat_qc1_format.tsv") # need install rio package conda install -c conda-forge r-rio, then first time loading rio "library(rio)" run install_formats() function as required

```


```python

library(readr)
library(data.table)

list_fg <- read_table("/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt", col_names = FALSE)
# list_fg <- read_table("./list_100_ss_phenocode_withprefix.txt", col_names = FALSE)

for (j in list_fg$X1) {
  j <- trimws(j)
  sumstat = fread(j)
  print(j)
  outfile = paste(j, ".qc", sep='')
  setnames(sumstat,"#chrom","chrom")
  summary(sumstat)
  # some qc (remove non SNP varaints, MAF <0.01, info if available)
  sumstat_qc1 = sumstat[nchar(ref)==1 & nchar(alt)==1 & (af_alt_cases>=0.01 & af_alt_cases<=0.99) & (af_alt_controls>=0.01 & af_alt_controls<=0.99),]
  write.table(sumstat_qc1, outfile, col.names = TRUE, quote = FALSE, row.names = FALSE)
}

```



## Using liftover

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
    
    #linecleanedstringwithouttitle=()
    #for p in "$linecleanedstring"; do linecleanedstringwithouttitle+=("$p.notitle"); done

    linecleanedstringbed=()
    for p in "$linecleanedstring"; do linecleanedstringbed+=("$p.bed"); done


    linenamecleanedlift=()
    for p in "$linenamecleaned"; do 
    a=("finngen_R8_$p");
    linenamecleanedlift+=("$a.lifted"); done

    linenamecleanedunlift=()
    for p in "$linenamecleaned"; do 
    a+=("finngen_R8_$p");
    linenamecleanedunlift+=("$a.unlifted"); done



    echo -e $j $linenamecleanedlift


    ${dir_RA}/data/liftover/liftOver $linecleanedstringbed ${dir_RA}/data/liftover/hg38ToHg19.over.chain.gz ${dir_RA}/data/liftover/lift_output/$linenamecleanedlift ${dir_RA}/data/liftover/unlift_output/$linenamecleanedunlift

done




    echo "#"'!'"/bin/bash
    #SBATCH --mem 1G
    #SBATCH -t 2:0:0
    #SBATCH -c 4
    #SBATCH -A dsmwpred
    source /home/lezh/miniconda3/etc/profile.d/conda.sh

    echo -e $j $linenamecleanedlift

    ${dir_RA}/data/liftover/liftOver ${dir_RA}/data/FinnGen/summarystatistics/liftover_hg19/$linenamecleanedbed ${dir_RA}/data/liftover/hg38ToHg19.over.chain.gz ${dir_RA}/data/liftover/lift_output/$linenamecleanedlift ${dir_RA}/data/liftover/unlift_output/$linenamecleanedunlift
  
    " > ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/liftover_hg19/result/finngen_liftover_$j

    cd ${dir_RA}/scripts/proj1_testprs_finngen_ukbb/liftover_hg19/result/
    sbatch finngen_liftover_$j

done

```


## Changing FinnGen SS into hg19
with the suffix .hg19

```python
dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode.txt"

for j in {1..100}; do

echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 1:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript ${dir_RA}/data/FinnGen/finn_gen_liftover_hg19.R $j

echo -e $j "done"

" > ${dir_RA}/scripts/data/FinnGen/hg19/finn_gen_liftover_hg19_sh_$j

cd ${dir_RA}/scripts/data/FinnGen/hg19/
sbatch finn_gen_liftover_hg19_sh_$j
done
```
