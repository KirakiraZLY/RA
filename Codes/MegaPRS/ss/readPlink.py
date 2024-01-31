import hail as hl
import numpy as np

def read_plink_hail(bed_file, bim_file, fam_file):
    hl.init()
    mt = hl.import_plink(bed_file, bim_file, fam_file)
    return mt

def hail_to_numpy(matrix_table):
    # Collect genotype values as a NumPy array
    call_array = np.array(matrix_table.GT.collect())

    # Extract the numeric representation of alleles
    numeric_array = np.array([call[0] for call in call_array])

    # Reshape the array based on the number of alleles
    num_variants = matrix_table.count_rows()
    num_individuals = matrix_table.count_cols()
    reshaped_array = numeric_array.reshape((num_variants, num_individuals))

    return reshaped_array

def ReadFile(bed_file, bim_file, fam_file):
    plink_mt = read_plink_hail(bed_file, bim_file, fam_file)
    # Convert Hail MatrixTable to NumPy array
    plink_np_array = hail_to_numpy(plink_mt)
    return plink_np_array

if __name__ == '__main__':
    # File paths
    bed_file = './data/smallset.bed'
    bim_file = './data/smallset.bim'
    fam_file = './data/smallset.fam'
    plink_np_array = ReadFile(bed_file, bim_file, fam_file)
    # Display the shape and a sample of the NumPy array
    print("Shape of the NumPy array:", plink_np_array.shape)
    print("Sample of the NumPy array:")
    print(plink_np_array[:, :5])  # Displaying the first 5 rows and 5 columns as a sample