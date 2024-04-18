# Commands during RA


dir="/home/lezh/dsmwpred/zly"
dir_RA="/home/lezh/dsmwpred/zly/RA"
dir_data="/home/lezh/dsmwpred/data/ukbb"
dir_LDAK="/home/lezh/snpher/faststorage/ldak5.2.linux"

file_bfile="/faststorage/project/dsmwpred/data/ukbb/geno4"
file_sumstat="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/gwas/ukbb/ss/geno4_height_regenie_Phenotype.ldpred.ss"
file_outname="/faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/ukbb/geno4_height_regenie_Phenotype"
file_pheno="/faststorage/project/dsmwpred/zly/RA/data/ukbb_pheno/height.label.test"


echo "0.001 0 0.001" > /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/geno4_range_list 
echo "0.05 0 0.05" >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/geno4_range_list 
echo "0.1 0 0.1" >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/geno4_range_list 
echo "0.2 0 0.2" >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/geno4_range_list 
echo "0.3 0 0.3" >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/geno4_range_list 
echo "0.4 0 0.4" >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/geno4_range_list 
echo "0.5 0 0.5" >> /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/geno4_range_list 


${dir}/software/plink \
    --bfile ${file_bfile} \
    --clump-p1 1 \
    --clump-r2 0.1 \
    --clump-kb 250 \
    --clump ${file_sumstat} \
    --clump-snp-field Predictor \
    --clump-field P \
    --out ${file_outname}.classicalprs

awk 'NR!=1{print $3}' ${file_outname}.classicalprs.clumped  >  ${file_outname}.classicalprs.valid.snp
awk '{print $1,$10}' ${file_sumstat} > ${file_outname}.SNP.pvalue



${dir}/software/plink \
    --bfile ${file_bfile} \
    --score ${file_sumstat} 1 4 8 header \
    --q-score-range /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/geno4_range_list  ${file_outname}.SNP.pvalue \
    --extract ${file_outname}.classicalprs.valid.snp \
    --pheno ${file_pheno} \
    --out ${file_outname}.classicalprs

awk 'NR>1{temp=$5; $5=$6; $6=temp; $4=0; $6="NA"; print} NR==1{$1="ID1"; $2="ID2"; $3="Phenotype"; $4="Covariates"; $5="Profile_1"; $6="BLANK"; print}' ${file_outname}.classicalprs.0.001.profile > ${file_outname}.0.001.temp_file && mv ${file_outname}.0.001.temp_file ${file_outname}.classicalprs.0.001.profile
awk 'NR>1{temp=$5; $5=$6; $6=temp; $4=0; $6="NA"; print} NR==1{$1="ID1"; $2="ID2"; $3="Phenotype"; $4="Covariates"; $5="Profile_1"; $6="BLANK"; print}' ${file_outname}.classicalprs.0.05.profile > ${file_outname}.0.05.temp_file && mv ${file_outname}.0.05.temp_file ${file_outname}.classicalprs.0.05.profile
awk 'NR>1{temp=$5; $5=$6; $6=temp; $4=0; $6="NA"; print} NR==1{$1="ID1"; $2="ID2"; $3="Phenotype"; $4="Covariates"; $5="Profile_1"; $6="BLANK"; print}' ${file_outname}.classicalprs.0.1.profile > ${file_outname}.0.1.temp_file && mv ${file_outname}.0.1.temp_file ${file_outname}.classicalprs.0.1.profile
awk 'NR>1{temp=$5; $5=$6; $6=temp; $4=0; $6="NA"; print} NR==1{$1="ID1"; $2="ID2"; $3="Phenotype"; $4="Covariates"; $5="Profile_1"; $6="BLANK"; print}' ${file_outname}.classicalprs.0.2.profile > ${file_outname}.0.2.temp_file && mv ${file_outname}.0.2.temp_file ${file_outname}.classicalprs.0.2.profile
awk 'NR>1{temp=$5; $5=$6; $6=temp; $4=0; $6="NA"; print} NR==1{$1="ID1"; $2="ID2"; $3="Phenotype"; $4="Covariates"; $5="Profile_1"; $6="BLANK"; print}' ${file_outname}.classicalprs.0.3.profile > ${file_outname}.0.3.temp_file && mv ${file_outname}.0.3.temp_file ${file_outname}.classicalprs.0.3.profile
awk 'NR>1{temp=$5; $5=$6; $6=temp; $4=0; $6="NA"; print} NR==1{$1="ID1"; $2="ID2"; $3="Phenotype"; $4="Covariates"; $5="Profile_1"; $6="BLANK"; print}' ${file_outname}.classicalprs.0.4.profile > ${file_outname}.0.4.temp_file && mv ${file_outname}.0.4.temp_file ${file_outname}.classicalprs.0.4.profile
awk 'NR>1{temp=$5; $5=$6; $6=temp; $4=0; $6="NA"; print} NR==1{$1="ID1"; $2="ID2"; $3="Phenotype"; $4="Covariates"; $5="Profile_1"; $6="BLANK"; print}' ${file_outname}.classicalprs.0.5.profile > ${file_outname}.0.5.temp_file && mv ${file_outname}.0.5.temp_file ${file_outname}.classicalprs.0.5.profile


conda activate zly2

Rscript /faststorage/project/dsmwpred/zly/RA/proj0_megaprs_test/full_analysis_classicalprs/plink_ct_r2.R --pheno ${file_pheno}  --outputFile ${file_outname}






${dir_LDAK} --jackknife ${file_outname}.classicalprs.0.001.jackknife --profile ${file_outname}.classicalprs.0.001.profile  --num-blocks 200
${dir_LDAK} --jackknife ${file_outname}.classicalprs.0.05.jackknife --profile ${file_outname}.classicalprs.0.05.profile  --num-blocks 200
${dir_LDAK} --jackknife ${file_outname}.classicalprs.0.1.jackknife --profile ${file_outname}.classicalprs.0.1.profile  --num-blocks 200
${dir_LDAK} --jackknife ${file_outname}.classicalprs.0.2.jackknife --profile ${file_outname}.classicalprs.0.2.profile  --num-blocks 200
${dir_LDAK} --jackknife ${file_outname}.classicalprs.0.3.jackknife --profile ${file_outname}.classicalprs.0.3.profile  --num-blocks 200
${dir_LDAK} --jackknife ${file_outname}.classicalprs.0.4.jackknife --profile ${file_outname}.classicalprs.0.4.profile  --num-blocks 200
${dir_LDAK} --jackknife ${file_outname}.classicalprs.0.5.jackknife --profile ${file_outname}.classicalprs.0.5.profile  --num-blocks 200

