# Commands during RA
## Week 16


/faststorage/project/dsmwpred/zly/software/plink  --make-bed --bfile /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4  --extract /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4_30wan.snplist  --out  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/geno4_30wan

## HDL
### auto test
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

#Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/LDpred2_1_auto.R

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/LDpred2_2_auto.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker29.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.EUR.HDL.gwas.dbGAP.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/MVP.EUR.HDL.gwas.dbGAP.geno4.ldpred2.auto --ss_type MVP


" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/scripts/MVP.EUR.HDL.gwas.dbGAP.geno4.ldpred2.auto.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/scripts/
sbatch MVP.EUR.HDL.gwas.dbGAP.geno4.ldpred2.auto.sh

```


## T2D
### auto
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 64G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/LDpred2_1_auto.R

Rscript /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/LDpred2_2_auto.R --pheno /home/lezh/snpher/faststorage/biobank/newphens/biomarkerphens/marker19.pheno  --sumstats /faststorage/project/dsmwpred/zly/RA/data/mvp/Takiy/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno4.ss.ldpred.ss  --outputFile  /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno4.ldpred2.auto --ss_type MVP


" > /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/scripts/MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno4_30wan.ldpred2.auto.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/proj1_testprs_finngen_ukbb/ldpred2_all/scripts/
sbatch MVP.T2D.EUR.MAF0.001.combined.dbGaP.geno4_30wan.ldpred2.auto.sh

```
