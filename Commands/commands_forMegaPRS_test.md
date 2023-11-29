# Commands for MegaPRS test
 

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

${dir}/software/plink --bfile ${dir_data}/geno --noweb --keep ${dir_RA}/test/data/geno_t.fam --make-bed --out ${dir_RA}/test/data/geno_t

" > ${dir_RA}/scripts/test/data/geno_t

# I am doing blabla
cd ${dir_RA}/scripts/test/data/
sbatch geno_t

```