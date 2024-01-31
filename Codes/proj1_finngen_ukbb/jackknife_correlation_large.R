

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
outputFile <- NULL

# famFile <- NULL

for (i in seq_along(args)) {
  if (args[i] == "--scoreFile" && i < length(args)) {
    scoreFile <- args[i + 1]
  } else if (args[i] == "--outputFile" && i < length(args)) {
    outputFile <- args[i + 1]
  }
}

# scoreFile <- "finngen_R10_RX_ANTIHYP"
# scoreFile <- paste(scoreFile, ".megaprs.new.jackknife.bestpheno", sep = "")

df_score <- read.delim(scoreFile, header = TRUE, sep = " ")
if (df_score$Correlation > 0.1) {
  write.table(df_score, outputFile, row.names = FALSE, col.names = TRUE, quote = FALSE)
}
# print(which.max(df_out$Correlation))
# print(max(df_out$Correlation))
print("============== Mission Completed ==============")
