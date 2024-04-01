# Commands during RA
## Week 16

# Pre-process FG

## Download

## Alter Remove not start with "rs"

awk '$5 ~ /^rs/' finngen_R10_T2D_WIDE > finngen_R10_T2D_WIDE.1
mv finngen_R10_T2D_WIDE.1 finngen_R10_T2D_WIDE
echo "chrom pos ref alt rsids nearest_genes pval mlogp beta sebeta af_alt af_alt_cases af_alt_controls" | cat - finngen_R10_T2D_WIDE > finngen_R10_T2D_WIDE.1
mv finngen_R10_T2D_WIDE.1 finngen_R10_T2D_WIDE

## Convert

conda activate zly2


awk '{OFS="\t"} {$1=$1} 1' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.1

mv /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.1  /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/finngen_ss_add_n.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN  --fileName  T2D_WIDE  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.addn

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN.addn  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_DUPUTRYEN  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  




awk '{OFS="\t"} {$1=$1} 1' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.1

mv /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.1  /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/finngen_ss_add_n.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC  --fileName  T2D_WIDE  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.addn

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC.addn  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_M13_FIBROBLASTIC  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  






awk '{OFS="\t"} {$1=$1} 1' /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE > /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.1

mv /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.1  /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE

Rscript /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/finngen_ss_add_n.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE  --fileName  T2D_WIDE  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.addn

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/code/ss_to_ldak_format.R --inputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE.addn  --outputFile /home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_T2D_WIDE  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4  

