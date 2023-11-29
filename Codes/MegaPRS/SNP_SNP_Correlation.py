

import numpy as np
import pandas as pd
import time


def Calc_Cor(genotype_matrix):
    correlation_matrix = np.corrcoef(genotype_matrix, rowvar=False)
    print(correlation_matrix)