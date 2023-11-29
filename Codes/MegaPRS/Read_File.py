import numpy as np
import pandas as pd
import time
import MakePheno
import SNP_SNP_Correlation
import pysnptools.pstreader as psr
import pysnptools.util as pstutil
from pysnptools.snpreader import Bed

def Read_File():
    plink_file_prefix = 'snps_t'
    bed_file = plink_file_prefix + '.bed'
    # Read PLINK files using pysnptools
    bed_reader = Bed(bed_file,count_A1=False)
    # print(bed_reader)
    snpdata1 = bed_reader.read()
    print(snpdata1)


if __name__ == '__main__':
    Read_File()