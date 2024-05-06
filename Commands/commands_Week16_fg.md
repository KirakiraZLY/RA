# Commands during RA
## Week 16

# Pre-process FG

## Download

## Alter Remove not start with "rs"

awk '$5 ~ /^rs/' finngen_R10_M13_DUPUTRYEN > finngen_R10_M13_DUPUTRYEN.1
mv finngen_R10_M13_DUPUTRYEN.1 finngen_R10_M13_DUPUTRYEN
echo "chrom pos ref alt rsids nearest_genes pval mlogp beta sebeta af_alt af_alt_cases af_alt_controls" | cat - finngen_R10_M13_DUPUTRYEN > finngen_R10_M13_DUPUTRYEN.1
mv finngen_R10_M13_DUPUTRYEN.1 finngen_R10_M13_DUPUTRYEN

## Convert

conda activate zly2


awk '{OFS="\t"} {$1=$1} 1' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.1

mv /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.1  /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/finngen_ss_add_n.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN  --fileName  I9_AF  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.addn

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.addn  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  


## MegaPRS

### Bayesr

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"


echo "#"'!'"/bin/bash
#SBATCH --mem 32G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh


${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/bayesr/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.bayesr --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/cors_geno4 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/highld_geno4/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.ldak --model bayesr --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.ldak --her 0.0707


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/bayesr/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.bayesr.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/bayesr/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.bayesr.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code8528.pheno


prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/bayesr/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.bayesr.pred.profile)


${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/bayesr/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.bayesr.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/bayesr/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.bayesr.pred.profile  --num-blocks 200 --prevalence ${prev}

### Elastic

${dir_LDAK} --mega-prs /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/elastic/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.elastic --allow-ambiguous YES --cors /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/cors_geno4 --high-LD /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/geno4_cor_ld/highld_geno4/genes.predictors.used --summary /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.ldak --model elastic --power -.25 --max-threads 4  --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.ldak


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/elastic/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.elastic.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/elastic/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.elastic.effects  --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code68.pheno

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/elastic/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.elastic.pred.profile)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/elastic/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.elastic.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/elastic/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.elastic.pred.profile  --num-blocks 200 --prevalence ${prev}

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/scripts/finngen_R10_M13_DUPUTRYEN.geno4.megaprs.sh

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/scripts/
sbatch finngen_R10_M13_DUPUTRYEN.geno4.megaprs.sh


## PRS-CS

#### First Part

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

awk '{print $1, $4, $5, $8, $10}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.ldpred.ss > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.prscs.ss

sed -i '1s/.*/Predictor A1 A2 Beta P/' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.prscs.ss


echo "#"'!'"/bin/bash
#SBATCH --mem 16G
#SBATCH -t 8:0:0
#SBATCH -c 4
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly_python3.6.3

python /faststorage/project/dsmwpred/zly/software/PRS_CS/PRScs.py --ref_dir=/faststorage/project/dsmwpred/zly/software/PRS_CS/ld_ref/ldblk_ukbb_eur --bim_prefix=/faststorage/project/dsmwpred/data/ukbb/geno4 --sst_file=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.prscs.ss --n_gwas=300000 --out_dir=/faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step1.results


" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/scripts/Step1_finngen_R10_M13_DUPUTRYEN.geno4.prscs.sh

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/scripts
sbatch Step1_finngen_R10_M13_DUPUTRYEN.geno4.prscs.sh



#### Second part


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"


cat /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step1.results* >> /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.combined

sort -n -k1 /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.combined >> /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.combined

rm /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step1.results_pst*


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/code/prs_cs_formatting.R --inputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.combined  --outputFile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.combined.effect


${dir_LDAK} --calc-scores /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.pred --power 0 --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 --scorefile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.combined.effect   --max-threads 4  --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code68.pheno

prev=$(awk 'NR>1 && $3==1 {count++} END {print count/(NR-1)}' /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.pred.profile)

${dir_LDAK} --jackknife /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.pred.jackknife --profile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/geno4_results/prs_cs/finngen_R10_M13_DUPUTRYEN.geno4.prscs.step2.results.pred.profile  --num-blocks 200  --prevalence ${prev}





















