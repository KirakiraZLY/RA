# Commands during RA
# Week8

1/22/2024


# 33KG with 1000 Genome
## MAF comparison
```python

echo "#"'!'"/bin/bash
#SBATCH --mem 128G
#SBATCH -t 30:0:0
#SBATCH -c 8
#SBATCH -A dsmwpred
source /home/lezh/miniconda3/etc/profile.d/conda.sh

/faststorage/project/dsmwpred/zly/software/plink --bfile /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1 --freq --out /faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_maf


" > /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/33kg_geno_fin_1_maf.sh

# I am doing blabla
cd /faststorage/project/dsmwpred/zly/RA/data/33KG/scripts/
sbatch 33kg_geno_fin_1_maf.sh

```


## ggplot

```python
conda activate zly2
R
```

```python
library(tidyverse)

print("Data Loading")
df <- read_table("/faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_maf.frq")
df_sampled <- df %>% sample_frac(0.001)

print("Plotting")
p <- ggplot(df_sampled, aes(x = SNP, y = MAF)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Minor Allele Frequency (MAF) for SNPs",
       x = "SNP ID",
       y = "MAF") +
  theme_minimal()

print("Data Saving")
ggsave("/faststorage/project/dsmwpred/zly/RA/data/33KG/33kg_geno_fin_1_maf_plot.png", plot = p, width = 10, height = 6)
```