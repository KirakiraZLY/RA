"""
This is a code to simulate phenotypes. It supports to select the number of individuals, the number of genotypes,
the tau (which represents the h2 in GCTA model, and tau1 in LDAK-thin model). You can choose heritability models
between GCTA and LDAK-thin by commenting in def Simulated_Phenotype. If you choose the LDAK-thin model, then the
maf is calculated based on the genotype simulation, and W for LD is simulated randomly between 0 and 1 (Can only
calculate ld_score_matrix by now).

Question: if maf 1...j corresponds to SNP 1...j, then how were these values calculated?
"""

import numpy as np
import pandas as pd

def Calc_MAF(genotype):
    total_alleles = genotype.shape[1] * 2
    maf = np.zeros((1,genotype.shape[0]))
    for j in range(0,genotype.shape[0]):
        n_a = np.sum(genotype[j] == 0)
        n_u = np.sum(genotype[j] == 2)
        n_m = np.sum(genotype[j] == 1)
        minor = min(n_a, n_u)
        maf[0][j] = (minor * 2 + n_m) / total_alleles

    return maf

def Calc_LD(genotype):
    allele_freq = np.mean(genotype, axis=0) / 2.0 * 2.0
    centered_genotype = genotype - allele_freq
    ld_score_matrix = np.square(np.cov(centered_genotype, rowvar=False))
    print("LD_score_matrix: ", "\n", ld_score_matrix)
    return ld_score_matrix

def LDAK_thin(genotype,tau):
    Calc_LD(genotype)
    W = np.random.choice([0,1], size=(1, genotype.shape[0]), replace=True) # To represent the regions with high or low LD
    # W = Calc_LD(genotype)
    maf = Calc_MAF(genotype)
    print("maf: ", maf)
    her = tau * W * (maf * (1-maf)) ** 0.75
    print("her: ", her)
    return her


def Simulated_Phenotype(n_inds = 5, n_snps = 10, tau = 0.7):
    genotype = np.random.choice([0,1,2], size=(n_inds, n_snps), replace=True)
    effects = np.random.normal(size=n_snps)
    genetics = np.dot(genotype,effects) # genotype * effects
    print("genetics: ", genetics)
    environments = np.random.normal(size=n_inds)

    her = np.zeros((1,n_inds))
    # her[0] = tau # GCTA model
    her = LDAK_thin(genotype, tau) # LDAK-thin model

    phenotype = her[0]*genetics + (1-her[0]) * environments


    phenotype_file = pd.DataFrame({'FID': range(1,n_inds+1),'IID': range(1,n_inds+1),"Phenotype": phenotype})
    return phenotype_file

def main():
    np.random.seed(123)
    pheno_simulated = Simulated_Phenotype()
    print(pheno_simulated)

if __name__ == '__main__':
    main()