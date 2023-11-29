import pandas as pd
import numpy as np
import time
import MakePheno
import SNP_SNP_Correlation
import Read_File

def ChisqTest(genotype, phenotype):
    # print("genotype: ", genotype, "\n" ,"phenotype: ", phenotype)
    n = np.linalg.norm(phenotype)
    r = np.dot(genotype.T, phenotype) / n
    S = n * r * r / (1 - r*r)
    # print(S)
    return S