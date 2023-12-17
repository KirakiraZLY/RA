
library(readr)
library(data.table)
library(dplyr)


args <- commandArgs(trailingOnly = TRUE)

list_fg <- read_table2("/home/lezh/dsmwpred/zly/RA/data/FinnGen/summarystatistics/list_100_ss_phenocode_withprefix.txt", col_names = FALSE)
# list_fg <- read_table("./list_100_ss_phenocode_withprefix.txt", col_names = FALSE)


j <- list_fg$X1[as.numeric(args[1])]
liftover_path <- paste(j, ".lifted", sep = "")
liftover <- read_table(liftover_path, col_names = FALSE)
colnames(liftover) <- c("chrom", "pos_start", "pos", "rsid")

sumstat_path <- paste(j, ".qc", sep = "")
sumstat <- read_table(sumstat_path)
# tagging <- read.table("./ldak.thin.genotyped.gbr.tagging", header = TRUE, sep=" ")

sumstat <- distinct(sumstat, rsids, .keep_all = TRUE)

df_liftover_1 <- paste(liftover$chrom, liftover$pos, sep = ":")
liftover$predictor <- df_liftover_1
df_ss_1 <- paste(sumstat$chrom, sumstat$pos, sep = ":")
sumstat$predictor <- df_ss_1
liftover$predictor <- substr(liftover$predictor, start = 4, stop = nchar(liftover$predictor))
colnames(liftover)[colnames(liftover) == "rsid"] <- "rsids"
sumstat1 <- sumstat[sumstat$rsids %in% liftover$rsids, ]
# sumstat1$predictor <- liftover$predictor

liftover_pre <- data.frame(liftover$predictor)
colnames(liftover_pre) <- "predictor"
sumstat1 <- merge(sumstat1, liftover_pre, by = "predictor", all.x = TRUE)

# tagging_ed <- sumstat1[sumstat1$predictor %in% tagging$Predictor, ]
# any(duplicated(sumstat$rsids))

hg19_path <- paste(j, ".hg19", sep = "")
write.table(sumstat1, hg19_path, row.names = FALSE, col.names = FALSE, quote = FALSE)
