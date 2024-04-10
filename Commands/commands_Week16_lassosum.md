# Commands during RA
## Week 16


# Lassosum on FinnGen 2409

## RUN
```python

dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"
ss_name_filename="/home/lezh/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/list_R10_ss_phenocode.txt"

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/lassosum/lassosum.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/icdphens/code68.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/data/finngen_icd10/ss/finngen_R10_E4_THYROID.addn  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/lassosum/finngen_R10_E4_THYROID.geno4.lassosum  --bfile /faststorage/project/dsmwpred/data/ukbb/geno4 

```

## Results
```
#!/bin/bash

for file in /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/lassosum/*.r2; do
    data=$(awk 'NR==2 {print $1}' "$file")
    echo "${data} ${file}"
done | sort -n -k1,1gr > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/lassosum/finngen_R10_E4_THYROID_r2_results.txt

```


# Result visualization of 4 PRS tools

```python
conda activate zly2
Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/fg_ukbb_33kg/res_vis.R

```


