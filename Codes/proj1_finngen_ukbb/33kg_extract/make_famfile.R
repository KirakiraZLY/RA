
N <- 3529

famfile <- data.frame(
  Column1 = 1:N,
  Column2 = 1:N,
  Column3 = rep(0, N),
  Column4 = rep(0, N),
  Column5 = rep(0, N),
  Column6 = rep(-9, N),
  stringsAsFactors = FALSE
)

write.table(famfile, "33kg_geno_fin.fam", row.names = FALSE, col.names = FALSE, quote = FALSE)