
import numpy as np
import pandas as pd
import time
import readPlink



def main():
    file_path = "finngen_R10_Z21_TOBAC_USE.ldak.1ksubset"
    df = pd.read_csv(file_path, sep=' ')
    df = pd.DataFrame(df)

    bed_file = './geno3_1000.bed'
    bim_file = './geno3_1000.bim'
    fam_file = './geno3_1000.fam'
    plink_np_array = readPlink.ReadFile(bed_file, bim_file, fam_file)
    print(plink_np_array[:, :5])

if __name__ == '__main__':
    main()