hg19 <- read.table("./finngen_R8_G6_HEADACHE.hg19", header = TRUE)
cor_bim <- read.table("./geno2_train_cors.cors.bim", header = FALSE, sep = "\t")
colnames(cor_bim) <- c("chr", "Predictor", "Stat", "Pos", "A1", "A2")
cor_bim_pre <- data.frame(cor_bim$Predictor)
colnames(cor_bim_pre) <- "Predictor"
exclude <- cor_bim_pre %>% filter(!(Predictor %in% hg19$Predictor))
write.table(exclude, path, row.names = FALSE, col.names = FALSE, quote = FALSE)