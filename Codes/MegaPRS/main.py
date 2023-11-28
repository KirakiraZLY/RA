"""
This is a code to simulate phenotypes. It supports to select the number of individuals, the number of genotypes,
the tau (which represents the h2 in GCTA model, and tau1 in LDAK-thin model). You can choose heritability models
between GCTA and LDAK-thin by commenting in def Simulated_Phenotype. If you choose the LDAK-thin model, then the
maf (1*M) is calculated based on the genotype simulation, and W for LD is simulated randomly between 0 and 1, or a vector
of values (1*M) taking from the mean of each column in LD score matrix.
"""

import numpy as np
import pandas as pd
import time
import MakePheno
import SNP_SNP_Correlation


def main():
    start_time = time.time()
    np.random.seed(123)
    ## To generate some genotype and phenotype data.
    genotype, phenotype, phenotype_file = MakePheno.Simulated_Phenotype(n_inds = 5, n_snps = 10, tau = 0.7)
    print(genotype, "\n\n", phenotype, '\n\n')
    # SNP_SNP_Correlation
    SNP_SNP_Correlation.Calc_Cor(genotype)

    print("Time Usage: %s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()