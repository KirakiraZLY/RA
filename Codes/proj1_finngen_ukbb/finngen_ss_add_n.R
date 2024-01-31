library(tidyverse)
library(dplyr)

args <- commandArgs(trailingOnly = TRUE)

inputFile <- NULL
fileName <- NULL
outputFile <- NULL

for (i in seq_along(args)) {
  if (args[i] == "--inputFile" && i < length(args)) {
    inputFile <- args[i + 1]
  } else if (args[i] == "--outputFile" && i < length(args)) {
    outputFile <- args[i + 1]
  } else if (args[i] == "--fileName" && i < length(args)) {
    fileName <- args[i + 1]
  }
}

# inputFile <- "./finngen_R8_VWXY20_SUICI_OTHER_INTENTI_SELF_H"
# fileName <- "VWXY20_SUICI_OTHER_INTENTI_SELF_H"
# outputFile <- "./finngen_R8_VWXY20_SUICI_OTHER_INTENTI_SELF_H.addn"

finngen_total <- read_tsv("/faststorage/project/dsmwpred/zly/RA/data/FinnGen/R8_manifest.tsv")
# finngen_total <- read_tsv("./R8_manifest.tsv")
finngen_total <- finngen_total[finngen_total$phenocode == fileName, ]
finngen_total$N <- finngen_total$num_cases + finngen_total$num_controls

n <- finngen_total$N

df_finngen_ss <- read_tsv(inputFile, col_names = TRUE) 
df_finngen_ss$n <- n

write.table(df_finngen_ss, outputFile, row.names = FALSE, col.names = TRUE, quote = FALSE)
