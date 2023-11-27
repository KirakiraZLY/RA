import pandas as pd

# Example genomic data (replace with your actual data)
data = {
    'SNP_ID': ['rs1', 'rs2', 'rs3', 'rs4'],
    'Sample1': ['AA', 'AG', 'GG', 'AG'],
    'Sample2': ['AA', 'AA', 'GG', 'AG'],
    'Sample3': ['GG', 'GG', 'AA', 'AA'],
}

df = pd.DataFrame(data)

# Function to calculate MAF for each SNP
def calculate_maf(snp_column):
    # Flatten the list of genotypes
    genotypes = [allele for genotype in snp_column for allele in genotype]

    # Count the occurrences of each allele
    allele_counts = {'A': genotypes.count('A'), 'G': genotypes.count('G')}

    # Determine the minor allele
    minor_allele = min(allele_counts, key=allele_counts.get)

    # Calculate MAF
    maf = allele_counts[minor_allele] / len(genotypes)

    return maf

# Calculate MAF for each SNP in the dataframe
maf_values = df.iloc[:, 1:].apply(calculate_maf, axis=0)

# Combine SNP IDs with MAF values
result_df = pd.DataFrame({'SNP_ID': df['SNP_ID'], 'MAF': maf_values})

# Print the result
print(result_df)
