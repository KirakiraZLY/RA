# Commands during RA
# Week 11

2/18/2024

# Run LDpred2

## Change SS from hg38 to hg37

### Make BED
```python
awk 'NR>1 && $5 ~ /^rs/ {print "chr"$1, ($2-1), $2, $5}'  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_I9_HYPTENS > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/finngen_R10_I9_HYPTENS.bed
```

### SS QC
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


" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/finn_gen_qc.sh

cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/scripts/
sbatch finn_gen_qc.sh

```

### Liftover
```python

/home/lezh/dsmwpred/zly/RA/data/liftover/liftOver /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/finngen_R10_I9_HYPTENS.bed  /home/lezh/dsmwpred/zly/RA/data/liftover/hg38ToHg19.over.chain.gz /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/liftover/finngen_R10_I9_HYPTENS.lifted /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/preparation/liftover/finngen_R10_I9_HYPTENS.unlifted


```

## Make Bed
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 100:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/LDpred2_readbed.R

" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/readbed.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2/
sbatch readbed.sh


```