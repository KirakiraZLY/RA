list_fg <- read_table2("/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt", col_names = FALSE)
# list_fg <- read_table2("./list_100_ss_phenocode_withprefix.txt", col_names = FALSE)

for (j in list_fg$X1) {
  j <- trimws(j)
  sumstat = fread(j)
  outfile = paste(j, ".qc", sep='')
  setnames(sumstat,"#chrom","chrom")
  summary(sumstat)
  # some qc (remove non SNP varaints, MAF <0.01, info if available)
  sumstat_qc1 = sumstat[nchar(ref)==1 & nchar(alt)==1 & (af_alt_cases>=0.01 & af_alt_cases<=0.99) & (af_alt_controls>=0.01 & af_alt_controls<=0.99),]
  write.table(sumstat_qc1, outfile, col.names = TRUE, )
}