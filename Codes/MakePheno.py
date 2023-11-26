import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def Basic_Simulated_Phenotype(n_inds = 5, n_snps = 10, her = 0.7):
    genotype = np.random.choice([0,1,2], size=(n_inds, n_snps), replace=True)
    effects = np.random.normal(size=n_snps)
    genetics = np.dot(genotype,effects) # genotype * effects
    # print(genetics)
    environments = np.random.normal(size=n_inds)
    phenotype = np.sqrt(her)*genetics + np.sqrt(1-her) * environments
    phenotype_file = pd.DataFrame({'FID': range(1,n_inds+1),'IID': range(1,n_inds+1),"Phenotype": phenotype})
    return phenotype_file

def main():
    np.random.seed(123)
    pheno_simulated = Basic_Simulated_Phenotype()
    print(pheno_simulated)

if __name__ == '__main__':
    main()