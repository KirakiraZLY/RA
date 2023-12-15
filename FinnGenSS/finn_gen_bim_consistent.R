
library(readr)
library(data.table)
library(dplyr)
library(tidyverse)


extract <- read.table("./finngen_R8_G6_HEADACHE.extrac", header = FALSE)
anyDuplicated(extract$V1)
bimfile <- read.table("./geno2.bim", header = FALSE)
colnames(bimfile) <- c("chr", "Predictor", "Stat", "Pos", "A1", "A2")
bimfile1 <- bimfile[((bimfile$A1 == 'A' & !(bimfile$A2 == 'T'))|
                       (bimfile$A1 == 'T' & !(bimfile$A2 == 'A'))|
                       (bimfile$A1 == 'C' & !(bimfile$A2 == 'G'))|
                       (bimfile$A1 == 'G' & !(bimfile$A2 == 'C'))
), ]

write.table(bimfile1, "./geno2_consistent.bim", row.names = FALSE, col.names = FALSE, quote = FALSE)