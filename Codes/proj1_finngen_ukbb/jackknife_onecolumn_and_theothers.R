

library(matrixStats)
library(pROC)
library(data.table)
library(tidyverse)
library(dplyr)

# set.seed(123)
# 
# df <- data.frame(
#   X1 = rnorm(100),
#   X2 = rnorm(100),
#   X3 = rnorm(100),
#   X4 = rnorm(100)
# )
# 
# 
# cor_function <- function(x, y) {
#   cor_value <- cor(x, y)
#   return(cor_value)
# }
# 
# all_cor_values <- as.numeric(cor_function(df$X1, df[, -1, drop = FALSE]))
# # jackknife_cor_values <- numeric(nrow(df))
# se_cor_values <- as.numeric(sqrt((1-all_cor_values) / (nrow(df) - 2)))
# # for (i in 1:nrow(df)) {
# #   jackknife_cor_values[i] <- cor_function(df$X1[-i], df[-i, -1, drop = FALSE])
# # }
# # se_cor_values <- sqrt((nrow(df) - 1) / nrow(df) * mean((jackknife_cor_values - mean(jackknife_cor_values))^2, na.rm = TRUE))
# df_out <- data.frame(Correlation = all_cor_values, SE = se_cor_values)
# # df_out$Correlation <- all_cor_values
# # df_out$SE <- se_cor_values
# # colnames(df_out) <- c("Correlation", "SE")
# 
# print(all_cor_values)
# print(se_cor_values)
# print(df_out)




args <- commandArgs(trailingOnly = TRUE)

scoreFile <- NULL
phenoFile <- NULL
outputFile <- NULL
# famFile <- NULL

for (i in seq_along(args)) {
  if (args[i] == "--scoreFile" && i < length(args)) {
    scoreFile <- args[i + 1]
  } else if (args[i] == "--phenoFile" && i < length(args)) {
    phenoFile <- args[i + 1]
  } else if (args[i] == "--outputFile" && i < length(args)) {
    outputFile <- args[i + 1]
  }
}

# scoreFile <- "./finngen_R10_.profile"
# phenoFile <- "./ukbb_phenotype_948_all.pheno"
# outputFile <- "Finngen_Name.jackknife.score"

df_score <- read.delim(phenoFile, header = TRUE, sep = " ")


df_prs <- read.delim(scoreFile, header = TRUE, sep = "\t")
df_prs <- df_prs[,c("ID1","ID2","Profile_1")]
colnames(df_prs) <- c("FID", "IID", "PRS")
df_prs <- subset(df_prs, FID %in% df_score$FID)
PRS <- df_prs$PRS

df_score <- df_score[,-c(1,2)]
df_score <- cbind(PRS, df_score)

df_score <- na.omit(df_score)

# df_score <- data.frame(lapply(df_score, bit64::integer64))


# cor_function <- function(data, indices) {
#   subset_data <- data[indices, ]
#   cor_values <- cor(subset_data[, 1], subset_data[, 2])
#   return(cor_values)
# }
# 
# range <- 1000
# # range <- nrow(df_score)
# result <- boot(df_score, statistic = cor_function, R = range)


# write.table(df_other_alt, outputFile, row.names = FALSE, col.names = TRUE, quote = FALSE)

# print("============== Mission Completed ==============")


# auc_function <- function(x, y) {
#   roc_obj <- roc(response = as.numeric(factor(x)), predictor = y)
#   auc_value <- auc(roc_obj)
#   return(auc_value)
# }


auc_function <- function(x, y) {
  roc_obj <- roc(response = as.numeric(factor(x)), predictor = y)
  auc_value <- auc(roc_obj)
  return(auc_value)
}

cor_function <- function(x, y) {
  cor_value <- cor(x, y)
  return(cor_value)
}

all_auc_values <- numeric(ncol(df_score) - 1)
# Calculate AUC values for each column (excluding the first column)
# all_auc_values <- sapply(df_score[, -1, drop = FALSE], function(column) auc_function(df_score$PRS, column))


all_cor_values <- as.numeric(cor_function(df_score$PRS, df_score[, -1, drop = FALSE]))
# all_auc_values <- auc_function(df_score$PRS, df_score[, -1, drop = FALSE])
se_cor_values <- as.numeric(sqrt((1-all_cor_values) / (nrow(df_score) - 2)))
# df_out <- data.frame(Correlation = all_cor_values, SE = se_cor_values, AUC = all_auc_values)
df_out <- data.frame(Correlation = all_cor_values, SE = se_cor_values)

# print(jackknife_cor_values)
# print(se_cor_values)

# write.table(df_out, outputFile, row.names = FALSE, col.names = TRUE, quote = FALSE)

# Output the UKBB phenotype which is the highest correlated with the FinnGen Summary Statistics
outputFile_pheno <- paste(outputFile,".bestpheno", sep = "")

best_pheno <- data.frame(Index = which.max(df_out$Correlation), Correlation = max(df_out$Correlation))

ukbb_table <- read_table("./icdtraits.details")
ukbb_pheno <- ukbb_table[ukbb_table$Index == best_pheno$Index,]$Description

best_pheno$ukbb_pheno <- ukbb_pheno

write.table(best_pheno, outputFile_pheno, row.names = FALSE, col.names = TRUE, quote = FALSE)
# print(which.max(df_out$Correlation))
# print(max(df_out$Correlation))
print("============== Mission Completed ==============")
