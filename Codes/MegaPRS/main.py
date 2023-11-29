
import numpy as np
import pandas as pd
import time
import MakePheno
import SNP_SNP_Correlation
import Read_File
import SumHer

def main():
    start_time = time.time()
    np.random.seed(123)
    ## To generate some genotype and phenotype data, standardized.
    genotype, phenotype, phenotype_file = MakePheno.Simulated_Phenotype(n_inds = 5, n_snps = 10, tau = 0.7)
    # genotype = Read_File.Read_File()
    # print(genotype, "\n\n", phenotype, '\n\n')
    # SNP_SNP_Correlation
    SNP_SNP_Correlation.Calc_Cor(genotype) # cjl
    ES = SumHer.ChisqTest(genotype,phenotype)


    # print("Time Usage: %s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()