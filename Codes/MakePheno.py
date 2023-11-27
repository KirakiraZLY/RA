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

def Calc_MAF(gen):
    genotype = gen.T
    total_alleles = genotype.shape[1] * 2
    maf = np.zeros((1,genotype.shape[0]))
    # print(total_alleles, maf)
    for j in range(0,genotype.shape[0]):
        n_a = np.sum(genotype[j] == 0)
        n_u = np.sum(genotype[j] == 2)
        n_m = np.sum(genotype[j] == 1)
        minor = min(n_a, n_u)
        maf[0][j] = (minor * 2 + n_m) / total_alleles
    print("MAF: ", maf)
    return maf

def Calc_LD(genotype):
    allele_freq = np.mean(genotype, axis=0) / 2.0 * 2.0
    centered_genotype = genotype - allele_freq
    ld_score_matrix = np.square(np.cov(centered_genotype, rowvar=False))
    # print("LD_score_matrix: ", "\n", ld_score_matrix)
    return ld_score_matrix

def LDAK_thin(genotype,tau):
    W = np.zeros((1,genotype.shape[1]))
    ld_matrix = Calc_LD(genotype)
    ld_vector = np.sum(ld_matrix, axis=1) / ld_matrix.shape[1] # I arbitrarily calculated the mean of each column as weighting
    """
    for j in range(ld_matrix.shape[1]):
        if ld_vector[j] >= 0.5:
            W[0][j] = 1
        else:
            W[0][j] = 0
    """

    W = ld_vector
    # W = np.random.choice([0,1], size=(1, genotype.shape[1]), replace=True) # To represent the regions with high or low LD
    print("LD Weighting: ", W)
    # W = Calc_LD(genotype)
    maf = Calc_MAF(genotype)
    # print("maf: ", maf)
    her = tau * W * (maf * (1-maf)) ** 0.75
    # print("her: ", her)
    return her


def Simulated_Phenotype(n_inds = 5, n_snps = 8, tau = 0.7):
    genotype = np.random.choice([0,1,2], size=(n_inds, n_snps), replace=True)
    print("genotype: ", "\n", genotype)
    effects = np.random.normal(size=n_snps)
    print("effects: ", effects)
    genetics = np.dot(genotype,effects) # genotype * effects
    print("genotype * effects: ", genetics)
    environments = np.random.normal(size=n_inds)

    her = np.zeros((1,n_inds))
    # her[0] = tau # GCTA model
    her = LDAK_thin(genotype, tau) # LDAK-thin model
    h2 = np.sum(her) / her.shape[1]
    print("h2: ", h2, her.shape[1])
    phenotype = np.dot(genetics,(h2 ** 0.5)) + np.dot(environments,((1-h2) ** 0.5))


    phenotype_file = pd.DataFrame({'FID': range(1,n_inds+1),'IID': range(1,n_inds+1),"Phenotype": phenotype})
    return phenotype_file

def main():
    np.random.seed(123)
    pheno_simulated = Simulated_Phenotype()
    print(pheno_simulated)

if __name__ == '__main__':
    main()