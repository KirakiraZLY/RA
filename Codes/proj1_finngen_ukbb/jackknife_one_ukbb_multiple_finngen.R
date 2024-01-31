


library(matrixStats)
library(pROC)
library(data.table)

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

# for (i in seq_along(args)) {
#   if (args[i] == "--scoreFile" && i < length(args)) {
#     scoreFile <- args[i + 1]
#   } else if (args[i] == "--phenoFile" && i < length(args)) {
#     phenoFile <- args[i + 1]
#   } else if (args[i] == "--outputFile" && i < length(args)) {
#     outputFile <- args[i + 1]
#   }
# }

phenoFile <- "./ukbb_phenotype_948_all.pheno"
scoreFile <- "./megaprs_new_pred_merged.txt"
outputFile <- "./pheno_to_finngen.jackknife.score"

df_prs <- read.delim(scoreFile, header = TRUE, sep = "\t")
new_column_names <- paste0("PRS_", 1:ncol(df_prs))
colnames(df_prs)[1:ncol(df_prs)] <- new_column_names

df_pheno <- read.delim(phenoFile, header = TRUE, sep = "\t")
# df_pheno <- df_prs[,c("ID1","ID2","Profile_1")]
# colnames(df_pheno) <- c("FID", "IID", "PRS")
df_pheno <- subset(df_pheno, FID %in% df_score$FID)

for (i in 3:col(df_pheno)) {
  # Data Prepara
  pheno <- df_pheno[,i]
  colnames(pheno) <- "Phenotype"
  df_score <- cbind(pheno, df_prs)
  df_score <- na.omit(df_score)
  
  
  cor_function <- function(x, y) {
    cor_value <- cor(x, y)
    return(cor_value)
  }
  
  all_auc_values <- numeric(ncol(df_score) - 1)
  # Calculate AUC values for each column (excluding the first column)
  all_auc_values <- sapply(df_score[, -1, drop = FALSE], function(column) auc_function(df_score$PRS, column))
  
  
  all_cor_values <- as.numeric(cor_function(df_score$PRS, df_score[, -1, drop = FALSE]))
  # all_auc_values <- auc_function(df_score$PRS, df_score[, -1, drop = FALSE])
  se_cor_values <- as.numeric(sqrt((1-all_cor_values) / (nrow(df_score) - 2)))
  # df_out <- data.frame(Correlation = all_cor_values, SE = se_cor_values, AUC = all_auc_values)
  
  df_out <- data.frame(Correlation = all_cor_values, SE = se_cor_values)
  
  best_prs <- data.frame(Index = which.max(df_out$Correlation), Correlation = max(df_out$Correlation))
  
  
  write.table(best_pheno, outputFile_pheno, row.names = FALSE, col.names = TRUE, quote = FALSE, append = TRUE)
  
  cat("Phenotype ", i, " has been written", "\n")
}

print("============== Mission Completed ==============")
