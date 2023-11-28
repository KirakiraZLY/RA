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


def Calc_Cor(genotype_matrix):
    correlation_matrix = np.corrcoef(genotype_matrix, rowvar=False)
    print(correlation_matrix)