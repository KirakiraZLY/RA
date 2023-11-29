import pandas as pd
import numpy as np
import time
import MakePheno
import SNP_SNP_Correlation
import Read_File
from sklearn.linear_model import LinearRegression
import MakePheno

def LR(ES, cor_matrix):
    # for i in range(cor_matrix.shape[0]):
    #     reg = LinearRegression().fit(cor_matrix[i],ES[i])
    #     print(reg.score(cor_matrix[i],ES[i]))
    # cor = np.dot(cor_matrix,cor_matrix)
    cor = cor_matrix
    reg = LinearRegression().fit(cor, ES)
    # print(reg.coef_)
    return reg.coef_

def ChisqTest(genotype, phenotype):
    # print("genotype: ", genotype, "\n" ,"phenotype: ", phenotype)
    n = np.linalg.norm(phenotype)
    r = np.dot(genotype.T, phenotype) / n
    S = n * r * r / (1 - r*r)
    print("Sj: ", S)
    return S

def SumHer(genotype, phenotype, cor_matrix):
    ES = ChisqTest(genotype, phenotype)
    tau = LR(ES,cor_matrix)
    her = MakePheno.LDAK_thin(genotype, tau)
    return np.sum(her)
