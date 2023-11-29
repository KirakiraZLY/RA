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

    centered_genotype = genotype - ( np.mean(genotype, axis=0) / 2.0 * 2.0 )
    covariance_matrix = np.cov(centered_genotype, rowvar=False)
    # print(covariance_matrix)
    sd = np.sqrt(np.diag(covariance_matrix))
    # print("sd: ", sd)
    ld_score_matrix = covariance_matrix / np.outer(sd, sd)
    print("LD_score_matrix: ", "\n", ld_score_matrix) ## Cov(Xi,Xj) / sqrt(Var(Xi))sqrt(Var(Xj))
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
    # W = np.random.choice([1,1], size=(1, genotype.shape[1]), replace=True) # To represent the regions with high or low LD
    # W = np.ones((genotype.shape[1]))
    print("LD Weighting: ", W)
    # W = Calc_LD(genotype)
    maf = Calc_MAF(genotype)
    # print("maf: ", maf)
    # print(np.sum(maf))
    her = tau * W * ((maf * (1-maf)) ** 0.75)
    print((maf * (1-maf)) ** 0.75)
    print("her: ", her)
    return her

def Check(phenotype, genetics, h2):
    hXb = genetics * (h2 ** 0.5)
    var_delta = np.var(phenotype - hXb)
    # print("varY, varhXb: ", np.var(phenotype), np.var(hXb))
    print("Observed h2, Set h2: ", 1-var_delta, h2)


def Simulated_Phenotype(n_inds = 5, n_snps = 4, tau = 0.7):
    genotype = np.random.choice([0,1,2], size=(n_inds, n_snps), replace=True)
    for j in range(genotype.shape[0]):
        genotype[j] = (genotype[j] - np.mean(genotype[j])) / np.sqrt(np.var(genotype[j]))
        # print(np.var(genotype[j]))
    genotype1 = genotype.T
    for j in range(genotype1.shape[0]):
        genotype1[j] = (genotype1[j] - np.mean(genotype1[j])) / np.sqrt(np.var(genotype1[j]))
        # print(np.var(genotype1[j]))
    genotype = genotype1.T
    # print(np.mean(genotype))
    print("genotype: ", "\n", genotype)
    effects = np.random.normal(size=n_snps)
    effects = (effects - np.mean(effects)) / np.sqrt(np.var(effects))
    print("effects: ", effects)
    genetics = np.dot(genotype,effects) # genotype * effects
    genetics = (genetics - np.mean(genetics)) / np.sqrt(np.var(genetics))
    print("genotype * effects: ", genetics)
    environments = np.random.normal(size=n_inds)
    environments = (environments - np.mean(environments)) / np.sqrt(np.var(environments))
    her = np.zeros((1,n_inds))

    # her[0][0] = tau # GCTA model
    her = LDAK_thin(genotype, tau) # LDAK-thin model

    h2 = np.sum(her)
    # print("heritability: ", h2)
    phenotype = np.dot(genetics,(h2 ** 0.5)) + np.dot(environments,((1-h2) ** 0.5))
    phenotype = (phenotype - np.mean(phenotype)) / np.sqrt(np.var(phenotype))


    Check(phenotype, genetics, h2) # Check if Var(Y-G) matches with 1-h2
    # print(1 - var_delta, h2)



    phenotype_file = pd.DataFrame({'FID': range(1,n_inds+1),'IID': range(1,n_inds+1),"Phenotype": phenotype})
    return phenotype_file

def main():
    start_time = time.time()
    np.random.seed(123)
    pheno_simulated = Simulated_Phenotype()
    print(pheno_simulated)
    print("Time Usage: %s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()