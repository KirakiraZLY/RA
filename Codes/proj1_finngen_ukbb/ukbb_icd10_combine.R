library(tidyverse)
library(dplyr)

args <- commandArgs(trailingOnly = TRUE)

inputFile <- NULL
outputFile <- NULL
famFile <- NULL

for (i in seq_along(args)) {
  if (args[i] == "--inputFile" && i < length(args)) {
    inputFile <- args[i + 1]
  } else if (args[i] == "--outputFile" && i < length(args)) {
    outputFile <- args[i + 1]
  } else if (args[i] == "--bfile" && i < length(args)) {
    famFile <- args[i + 1]
  }
}

# inputFile <- "./icd10_alltraits_test.txt"
# outputFile <- "./ukbb_pheno_test.txt"
# famFile <- "./geno3"
# famFile <- paste(famFile, ".fam", sep = "")

fam <- read.table(famFile)
colnames(fam) <- c("FID", "IID", "PID", "MID", "GENDER", "Phenotype")


read_list <- readLines(inputFile)

out_table <- read.table(read_list[1])
colnames(out_table) <- c("FID", "IID", "Phenotype1")

out_table <- subset(out_table, FID %in% fam$FID)


index <- 2
while (index <= length(read_list)) {
  tmp_table <- read.table(read_list[index])
  # colnames(tmp_table) <- c("FID", "IID", paste("Phenotype", index, sep = ""))
  tmp_table <- subset(tmp_table, V1 %in% fam$FID)
  
  tmp <- data.frame(tmp_table$V3)
  colnames(tmp) <- paste("Phenotype", index, sep = "")
  out_table <- cbind(out_table, tmp)
  cat("File ", index, " has completed", "\n")
  index <- index + 1
}


write.table(out_table, outputFile, row.names = FALSE, col.names = TRUE, quote = FALSE)

print("========== Mission Completed ==========")
