
# library(qqman)
library(tidyverse)
library(tidyr)

snps <- read_table("/home/lezh/dsmwpred/ml/mhc.bim", col_names = FALSE)
snps_1to12 <- subset(snps, snps$X1 == 6)
snps_1to12 <- snps_1to12$X2
write.table(snps_1to12,"/faststorage/project/dsmwpred/zly/RA/proj2_noniid_problem/mhc_phenotype/snps_only_chr6_mhc.txt",row.names = FALSE, col.names = FALSE, quote = FALSE)
# write.table(snps_1to12,"/faststorage/project/dsmwpred/zly/RA/proj2_noniid_problem/mhc_phenotype/snps_only_chr6_mhc_withlabel.txt",row.names = FALSE, col.names = TRUE, quote = FALSE)