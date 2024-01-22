# Commands during RA
# Week 7

1/17/2024



# 33KG

## extract $12 for ethnic group
awk -F'\t' '{print $12}' 33kg_chr1_geno | head -n 6

zcat 33kg_chr21_geno.gz | awk -F'\t' '{print $12}'

## Download full reference panel

wget --header="Host: drive.usercontent.google.com" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" --header="Accept-Language: zh-TW,zh-CN;q=0.9,zh;q=0.8,da-DK;q=0.7,da;q=0.6,en-US;q=0.5,en;q=0.4" --header="Cookie: HSID=APnoQbcg27H_vMEH-; SSID=AGc6vTJNsS7-66fkn; APISID=xABBLOKwdKNjJjvk/AiUafM0SkrRNoaKvm; SAPISID=VJX2qR3T9TGbVmXN/Ag3xuaRQRubuSkCnF; __Secure-1PAPISID=VJX2qR3T9TGbVmXN/Ag3xuaRQRubuSkCnF; __Secure-3PAPISID=VJX2qR3T9TGbVmXN/Ag3xuaRQRubuSkCnF; SOCS=CAESOAgEEitib3FfaWRlbnRpdHlmcm9udGVuZHVpc2VydmVyXzIwMjMwNjEzLjAwX3AwGgV6aC1DTiACGgYIgJK5pAY; SID=eQhQDfp1rQWrgZvkr14d8LvVHiDrCG0sphbB-Y6oJG3EbxLCQGo3Ob2jZqAFs1F9FzaVWA.; __Secure-1PSID=eQhQDfp1rQWrgZvkr14d8LvVHiDrCG0sphbB-Y6oJG3EbxLCI9tPthypZwes0mwYba1H5Q.; __Secure-3PSID=eQhQDfp1rQWrgZvkr14d8LvVHiDrCG0sphbB-Y6oJG3EbxLCSIXn34-CnuI6h4npr3OMaw.; SEARCH_SAMESITE=CgQImJoB; 1P_JAR=2024-1-14-22; AEC=Ae3NU9MsFgF5SacQ9r2XpseOTiSIaooD2-i8W6HO_TvnxV-IJ7r4jp_EZwU; __Secure-ENID=17.SE=xSstVS3FvOeSI4uJegOg_bLhLqPMcCyc0zlLAM9wMmpPqSYqlJfBedRbTr0EPZCmAPEA8rgwBcnE8tcVc-dpLvvGvSYRGWdYOp0p5Vuqr-zPsiBzz-nOXIG20YA3KWrK6JQCkm0gQ6Dg9sOv6mF2kbKZU1g9Iv7fZOHepJzeLy-KfkP8FENs6yewC6YHcfbUm-oxt03dH4lMC--O0heAzkfQ9-mLIMxPt8gYB5QZD3ujy2NXgKz_Ynkl2EVLZj4R5rza9aCKCk2rEVpaKhJv_nmUMc84cG5_4jQCk9AO2UzSDuSTh7h-lnnBwMyXo9wVX9_-a-qtStl4IOMCKXTRIrL06YP92wT5z9-x0tHVq7YvPVjK5Lc8PsGajrgNe5bp2w3Xj4KLvMnAbjBIDMlcO6hjbVhmCMqrTwAfI-NHugkGHtLLehMIb0YyKf4eGIIOugbHgvsgrQb8nn1eYUBTjj-_S8QBwHjBXzEkR5H8Ql0; __Secure-1PSIDTS=sidts-CjIBPVxjSv8k1Q6OoLjrls8EObKtdDT8hoNjQ9bTHkS0nkFhjmSg5qg8MIXE01KKxIwc8hAA; __Secure-3PSIDTS=sidts-CjIBPVxjSv8k1Q6OoLjrls8EObKtdDT8hoNjQ9bTHkS0nkFhjmSg5qg8MIXE01KKxIwc8hAA; NID=511=Clu_80BPJFDbIUEMItpeFJQcQN8Q-EclF7zIoWCldtLOCS8bLjpk139PDiSmLY7ij2GQIgvkF00Pu1SqASfAPu1cWBfSyrKt5WG9DkRl-4g8MQUSfaGcvzJghnZlw_cSqxflQJUPBYkYIeLHfTVEQer8myN-0Y2Kp2p_r9075LL18bnXbVTPfn5_AqEx5K6ZcYNRm_WGA3dlau6DshXH44L6BdrJTX7KQl1dJp7LCBwsrilitdaN1dudMnBO6UnGzOMWZw39EU3soyqyqxV5AUEFGnrOrDgowdx2z9g5v7Ey2yl-KyO0sOL237PubyPGUUAoioxlvBOiwTX-aFL2vKrp0YOyvMJWX3RSXs4ZKk1Gl-K_RtqH1FZP1b5IBFPMhTegTD2IJHp4UUDeO39qpzMQM-LXT4skLVn3gNFigJ1OgO-ISxOx3m-QtIbYYIDC90FKfqMzSzzDQyXdFw; SIDCC=ABTWhQE9kZRIsZv11DVDKFxvb8-YfemktsD4pIbTGtOBcIV6zBunu3T6r5MW93Qn9RqA5CaW5F6n; __Secure-1PSIDCC=ABTWhQEHwEO5X_VubAabQl3NIvDPCYdeTySlwNh132qteaIDoa27lblnS33Qyzflj4R7p_XBCGAo; __Secure-3PSIDCC=ABTWhQEu5dLKSl8a9Iu1JWrVkVR96se3XiL36f9bFRl8Oi8Cg4s2i3UrtHF3jSBWcvLwxSF-PA" --header="Connection: keep-alive" "https://drive.usercontent.google.com/download?id=1Ie2vtPeHJJ7xpGNlReH_fUcZ2DLUmP2H&export=download&authuser=0&confirm=t&uuid=1e5a71d3-4347-4d78-8539-776592444e4f&at=APZUnTVaiPnPzyZFfTjcv9S46FNB:1705566023210" -c -O '33kg_geno.gz'


## extract $12 for ethnic group from the full text
```python
zcat 33kg_geno.gz | awk '{print $12}' | sed 's/0/0 /g' | sed 's/1/1 /g' | sed 's/2/2 /g'> 33kg_geno_fin.sp

```

### TEST: extract $12 for ethnic group from the chr21 text
```python
zcat 33kg_chr21_geno.gz | awk '{print $12}' | sed 's/0/0 /g' | sed 's/1/1 /g' | sed 's/2/2 /g' | head -n 6 > 33kg_chr21_geno_fin_6snps.sp

```



### Print first 6 columns
```python
head -n 6 33kg_geno_fin.txt > 33kg_geno_fin_6columns.sp

```

### gzip .sp file

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

gzip /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin.sp

" > /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_gzip.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/
sbatch 33kg_geno_fin_gzip.sh

```


## get bim file of the full one
```python
zcat 33kg_index.gz | awk '{print $2, $2 ":" $3, $6, $3, $5, $4}'> 33kg_geno_fin.bim

```

## Extract the number of individuals
awk 'NR==1 {print NF}' 33kg_geno_fin_6columns.txt

## Make fam file by a R code
See make_famfile.R




## TEST: Make bed with --sp
```python
/home/lezh/snpher/faststorage/ldak5.2.linux  --make-bed /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_6columns --gen /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_6columns.sp --fam /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin.fam  --bim /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_6columns.bim  --threshold 1 --gen-skip 0 --gen-headers 0 --gen-probs 1

```

## Make bed with --sp
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/home/lezh/snpher/faststorage/ldak5.2.linux  --make-bed /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin --sp-gz /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin  --threshold 1 --gen-skip 0 --gen-headers 0 --gen-probs 1


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/33kg_geno_fin_makebed.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch 33kg_geno_fin_makebed.sh

```


## chr:pos -> rsid, hg19

```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/annotate_variation.pl /faststorage/project/dsmwpred/zly/RA/data/33KG/bim_rsid/33kg_geno_fin_rsid.txt /faststorage/project/dsmwpred/zly/software/ANNOVAR/annovar/humandb/ -filter -build hg19 -dbtype avsnp150


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/33kg_geno_fin_bim_rsid.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch 33kg_geno_fin_bim_rsid.sh

```


# FinnGen UKBB
## To get correlation > 0.05

```python

conda activate zly2

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"
for j in {1..551}; do
echo $j
linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/jackknife_correlation_large.R --scoreFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife.bestpheno  --outputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/high_correlation/finngen_R10_${linenamecleaned}.megaprs.new.jackknife.bestpheno

done

```



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

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/jackknife_correlation_large.R --scoreFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/finngen_R10_${linenamecleaned}.megaprs.new.jackknife.bestpheno

" > /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/high_correlation/finngen_R10_${linenamecleaned}.megaprs.new.jackknife.bestscore.highcorrelation.sh

# I am doing blabla

cd /faststorage/project/dsmwpred/zly/RA/scripts/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/jackknife/high_correlation/
sbatch finngen_R10_${linenamecleaned}.megaprs.new.jackknife.bestscore.highcorrelation.sh

done


```






















# finngen ukbb 33kg

## Make Bim File

### bim get rsid
```python

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/data/33KG/bim_get_rsid.R


```

### Make bed QC
```python
/faststorage/project/dsmwpred/zly/software/plink2 --file /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1 --geno 0.1 --mind 0.1 --maf 0.05 --mac 100 --allow-no-sex --make-bed --out /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1

```

### QC

```python
/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1 --geno 0.1 --mind 0.1 --maf 0.05 --mac 100 --make-bed --out /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1

```


## Megaprs_new

### Step 1 有了不用跑，直接调用
```python
shuf -n 5000 /home/lezh/dsmwpred/data/ukbb/geno3.fam > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/rand_geno3.5000

/home/lezh/snpher/faststorage/ldak5.2.linux --calc-cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/cors_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --keep /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/rand_geno3.5000 --max-threads 4

/home/lezh/snpher/faststorage/ldak5.2.linux --cut-genes /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/megaprs_new/highld_geno3 --bfile /home/lezh/dsmwpred/data/ukbb/geno3 --genefile /home/lezh/snpher/faststorage/highld.txt


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

linename=$(head -n $j $ss_name_filename | tail -n 1)
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
for j in {1..551}; do

linename=$(head -n $j $ss_name_filename | tail -n 1)
linenamecleaned=$(echo -n "$linename" | tr -d '\r\n')

echo $j $linenamecleaned

awk '{print $5}' "/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/finngen_R10_${linenamecleaned}.megaprs.new.pred.profile" > "/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_${linenamecleaned}.txt"

done
paste /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_*.txt > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/megaprs_new_pred_merged.txt

rm /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/column_*.txt


```

### Run correlation: one Phenotype with multiple FinnGen ss
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh
conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/jackknife_one_ukbb_multiple_finngen.R

" > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/pheno_to_finngen.jackknife.sh

# I am doing blabla

cd /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/megaprs_new/finngen_ukbb/prediction/combine/
sbatch pheno_to_finngen.jackknife.sh


```