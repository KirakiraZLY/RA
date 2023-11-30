
import numpy as np
import pandas as pd
import time
import MakePheno
import SNP_SNP_Correlation
import Read_File
import SumHer
import Prediction

def Check(pheno_pred, phenotype):
    return np.var(phenotype - pheno_pred)



def main():
    start_time = time.time()
    np.random.seed(123)
    ## To generate some genotype and phenotype data, standardized.
    genotype, phenotype, phenotype_file = MakePheno.Simulated_Phenotype(n_inds = 5, n_snps = 10, tau = 0.7)
    # genotype = Read_File.Read_File()
    # print(genotype, "\n\n", phenotype, '\n\n')
    # SNP_SNP_Correlation
    cor_matrix = SNP_SNP_Correlation.Calc_Cor(genotype) # cjl
    her = SumHer.SumHer(genotype, phenotype, cor_matrix)
    print("her: ", her)
    pheno_pred = Prediction.Pred_Pheno(her, genotype) # Since I don't have the effect sizes from Summary Statistics, I simulate some by normal distribution
    print("Var: ",Check(pheno_pred, phenotype))
    # print(np.var(phenotype), np.var(pheno_obs))
    # print(phenotype)



    # print("Time Usage: %s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()