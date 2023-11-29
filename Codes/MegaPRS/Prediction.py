import numpy as np

def Pred_Pheno(her, genotype):
    # print("shape0: ", genotype.shape[0])
    effects = np.random.normal(size=genotype.shape[1])
    effects = (effects - np.mean(effects)) / np.sqrt(np.var(effects))
    print("genotype: ", genotype)
    print("effects: ", effects)
    genetics = np.dot(genotype, effects)  # genotype * effects
    genetics = (genetics - np.mean(genetics)) / np.sqrt(np.var(genetics))
    print("genotype * effects: ", genetics)
    environments = np.random.normal(size=genotype.shape[0])
    environments = (environments - np.mean(environments)) / np.sqrt(np.var(environments))
    phenotype = np.dot(genetics, (her ** 0.5)) + np.dot(environments, ((1 - her) ** 0.5))
    phenotype = (phenotype - np.mean(phenotype)) / np.sqrt(np.var(phenotype))
    print("phenotype_Predicted: ", phenotype)
    return phenotype