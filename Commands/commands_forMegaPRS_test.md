# Commands for MegaPRS test
 

## To generate basic plink data
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

${dir_LDAK} --make-snps ${dir_RA}/test/data/snps_t --num-samples 10 --num-snps 100

" > ${dir_RA}/scripts/test/data/snps_t

# I am doing blabla
cd ${dir_RA}/scripts/test/data/
sbatch snps_t

```

## conver to vcf file
```
${dir}/software/plink --file ${dir_RA}/test/data/snps_t --recode vcf --out ${dir_RA}/test/data/snps_t
```