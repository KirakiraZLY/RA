
import numpy as np
import pandas as pd
import time
import MakePheno
import SNP_SNP_Correlation
import Read_File
import SumHer
import Prediction


def main():
    file_path = "finngen_R10_Z21_TOBAC_USE.ldak.1ksubset"
    df = pd.read_csv(file_path, sep=' ')
    df = pd.DataFrame(df)
    # print(df.head(10))
    # print(df['Predictor'])
    # print(df.iloc[0:6, 1])

if __name__ == '__main__':
    main()