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

def ReadFile():
    filename = './icdtraits.details'
    icd10 = pd.read_csv(filename, sep=' ')
    icd10 = pd.DataFrame(icd10)
    filename = './R8_manifest.tsv'
    finngen = pd.read_csv(filename, sep='\t')
    finngen = pd.DataFrame(finngen)

    return icd10, finngen

def LCS():
    icd10, finngen = ReadFile()
    # print(finngen)
    icd10["Description"] = icd10["Description"].str.replace(r'^.*?_', '') # delete all chrs before the first "_", which are "AB1" for example
    icd10_pheno = icd10["Description"]
    finngen_pheno = finngen['phenocode']
    # print(finngen_pheno)
    # icd10["Description"] = icd10["Description"].str.replace(r'^.*?_', '')
    finngen_pheno = finngen_pheno.str.replace(r'^.*?_', '')
    icd10_pheno = icd10_pheno.str.lower()
    finngen_pheno = finngen_pheno.str.lower()


    icd10_pheno = icd10_pheno.applymap(lambda x: x.replace('_', '') if isinstance(x, str) else x)
    finngen_pheno = finngen_pheno.applymap(lambda x: x.replace('_', '') if isinstance(x, str) else x)
    print(finngen_pheno)

def main():
    np.random.seed(123)
    LCS()

if __name__ == '__main__':
    main()