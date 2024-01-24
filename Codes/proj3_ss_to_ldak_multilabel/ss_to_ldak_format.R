library(tidyverse)
library(dplyr)

# About Input Argument
args <- commandArgs(trailingOnly = TRUE)

inputFile <- NULL
outputFile <- NULL
bimFile <- NULL
# arg_out <- NULL

for (i in seq_along(args)) {
  if (args[i] == "--inputFile" && i < length(args)) {
    inputFile <- args[i + 1]
  } else if (args[i] == "--outputFile" && i < length(args)) {
    outputFile <- args[i + 1]
  } else if (args[i] == "--bfile" && i < length(args)) {
    bimFile <- args[i + 1]
  }
}


# inputFile <- "./finngen_R10_I9_IHD.addn"
# 
# # inputFile <- "./finngen_R8_ASTHMA_ALLERG.addn"
# outputFile <- "./finngen_R8_VWXY20_SUICI_OTHER_INTENTI_SELF_H.ldak"
# bimFile <- "./geno3"
# 
bimFile <- paste(bimFile, ".bim", sep = "")

# Input File
df_other1 <- read_table(inputFile, col_names = TRUE)
n <- df_other1[1,]$n
# df_ldak1 <- na.omit(df_ldak1)
df_other1 <- na.omit(df_other1)
df_other <- df_other1

beta <- as.numeric(df_other$beta)
df_other$or <- exp(beta)

# Column names could be
# Ref == A2, Alter = A1
names_to_replace <- c("Predictor",
                      
                      "rsids",
                      "SNP", 
                      
                      "#chrom",
                      "chrom",
                      
                      "pos",
                      "BP",
                      "Basepair", 
                      "GENPOS", 
                      
                      "ref",
                      
                      "alt",
                      
                      "zscore",
                      
                      "Direction",
                      
                      "Stat",
                      
                      "pval",
                      
                      "beta",
                      
                      "sebeta",
                      
                      "or"
)

replacement_rules <- c("Predictor" = "Predictor",
                       
                       "rsids" = "rsids",
                       "SNP" = "rsids",
                       
                       "#chrom" = "Chr",
                       "chrom" = "Chr",
                       
                       "pos" = "Pos",
                       "BP" = "Pos",
                       "Basepair" = "Pos", 
                       "GENPOS" = "Pos", 
                       
                       "alt" = "A1",
                       
                       "ref" = "A2",
                       
                       "zscore" = "Z",
                       
                       "Direction" = "Direction",
                       
                       "Stat" = "Stat",
                       
                       "pval" = "P",
                       
                       "beta" = "Beta",
                       
                       "sebeta" = "SEbeta",
                       
                       "or" = "OR"
)

df_other_alt <- df_other %>%
  rename_all(~ ifelse(. %in% names_to_replace, replacement_rules[.], .))
# df_other_alt <- mutate_at(df_other_alt, vars(c("Z", "Stat", "P", "Beta", "SEbeta", "OR")), as.numeric)

# ## I use rsids instead of predictor, for geno3 format
# case_predictor <- c("rsids", "Chr", "Pos")
# if (sum(colnames(df_other_alt) %in% case_predictor) == 3) {
#   df_other_alt$Predictor <- paste(df_other_alt$Chr, ":", df_other_alt$Pos, sep = "")
#   df_other_alt$Predictor <- gsub(" ", "", df_other_alt$Predictor)
# }

df_other_alt$Predictor <- df_other$rsids
df_other_alt$n <- n


case1 <- c("Z")
case2 <- c("Beta", "P")
case3 <- c("OR", "P")
case4 <- c("Beta", "SEbeta")
case5 <- c("OR", "SEbeta")
# case6 <- c("Direction", "Stat")
# case7 <- c("Direction", "P")

if (sum(colnames(df_other_alt) %in% case1) == 1) {
  df_other_alt <- mutate_at(df_other_alt, vars(c("Z")), as.numeric)
  df_other_alt$Z <- df_other_alt$Z
  print("Case 1")
} else if (sum(colnames(df_other_alt) %in% case2) > 1){
  df_other_alt <- mutate_at(df_other_alt, vars(c("P", "Beta")), as.numeric)
  beta <- df_other_alt$Beta
  pval <- df_other_alt$P
  c <- -qnorm(pval/2)
  zscore <- ifelse(beta>0, c, -c)
  df_other_alt$Z <- zscore
  print("Case 2")
} else if (sum(colnames(df_other_alt) %in% case3) > 1){
  df_other_alt <- mutate_at(df_other_alt, vars(c("P","OR")), as.numeric)
  OR <- df_other_alt$OR
  pval <- df_other_alt$P
  c <- qnorm(1-pval/2)
  zscore <- ifelse(or>1, c, -c)
  df_other_alt$Z <- zscore
  print("Case 3")
} else if (sum(colnames(df_other_alt) %in% case4) > 1){
  df_other_alt <- mutate_at(df_other_alt, vars(c("Beta", "SEbeta")), as.numeric)
  beta <- df_other_alt$Beta
  se <- df_other_alt$SEbeta
  zscore <- beta/se
  df_other_alt$Z <- zscore
  print("Case 4")
} else if (sum(colnames(df_other_alt) %in% case5) > 1){
  df_other_alt <- mutate_at(df_other_alt, vars(c("SEbeta", "OR")), as.numeric)
  or <- df_other_alt$OR
  se <- df_other$sebeta
  zscore <- log(or)/se
  df_other_alt$Z <- zscore
  print("Case 5")
}

## Delete len(A1) > 1 and len(A2) > 1
# df_other_alt$Predictor <- df_other_alt$rsids
df_other_alt <- df_other_alt[nchar(df_other_alt$A1) <= 1, ]
df_other_alt <- df_other_alt[nchar(df_other_alt$A2) <= 1, ]
## Delete duplicate rsid
df_other_alt <- df_other_alt[!duplicated(df_other_alt$Predictor), ]


# Output File
df_other_alt <- df_other_alt[, c("Predictor", "A1", "A2", "n","Z")]

# Read bim
bim <- read.table(bimFile)
# colnames(bim) <- c("Chr", "Predictor", "cM", "Pos", "A1", "A2")
bim_pred <- data.frame(bim$V2)
colnames(bim_pred) <- c("Predictor")
df_other_alt <- merge(df_other_alt, bim_pred, by = "Predictor", all.x = TRUE)
bim_pred <- bim
colnames(bim_pred) <- c("Chr","Predictor","cM","Pos","A1","A2")
df_other_alt <- df_other_alt %>%
  inner_join(bim_pred, by = "Predictor") %>% 
  filter((A1.x == A1.y & A2.x == A2.y) | (A1.x == A2.y & A2.x == A1.y)) %>%
  select(c("Predictor", "A1.x","A2.x","n","Z"))
colnames(df_other_alt) <- c("Predictor", "A1", "A2", "n","Z")

write.table(df_other_alt, outputFile, row.names = FALSE, col.names = TRUE, quote = FALSE)

print("============== Mission Completed ==============")