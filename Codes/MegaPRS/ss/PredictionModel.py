import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

def Prior(s,h2,p1,p2,p3,p4):
    x = np.linspace(-3, 3, 1000)

    delta_function = np.zeros_like(x)
    delta_function[len(x) // 2] = 1.0

    # Normal
    normal_distribution = p2 * norm.pdf(x, loc=0, scale=s*h2/100) + p3 * norm.pdf(x, loc=0, scale=s*h2/10) + p4 * norm.pdf(x, loc=0, scale=s*h2)

    result = p1 * delta_function + normal_distribution
    # print(result)


    plt.plot(x, delta_function, label='Dirac Delta Function')
    plt.plot(x, normal_distribution, label='N(0, 1)')
    plt.plot(x, result, label='$\delta_0 + N(0, 1)$')
    plt.title('$\delta_0 + N(0, 1)$')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()

    return result

def SumHer():
    ## Read MAF
    maf_file_path = "D:\Aarhus_RA\Project\RA\Codes\MegaPRS\ss\matrix\cors_geno3_1000.cors.bim"
    maf = pd.read_csv(maf_file_path, sep='\t', header=None)
    custom_column_names = ['Chr', 'Predictor', 'Frq', 'Pos', 'A1', 'A2']
    maf.columns = custom_column_names
    # print(maf.head())
    # print(len(maf))

    ## Pseudo MAF matrix
    np.random.seed(42)
    random_numbers = np.random.rand(1000)
    matrix_of_random_numbers = np.tile(random_numbers, (1000, 1))
    noise_matrix = 0.2 * np.random.randn(1000, 1000)
    correlated_matrix = matrix_of_random_numbers + noise_matrix
    correlation_matrix = np.corrcoef(correlated_matrix)
    # print(correlation_matrix)
    # print(len(correlated_matrix))

    ## Read LD
    ld_file_path = "D:\Aarhus_RA\Project\RA\Codes\MegaPRS\ss\matrix\highld_geno3_1000\genes.predictors"
    ld = pd.read_csv(ld_file_path, sep='\t', header=None)
    custom_column_names = ['Predictor']
    ld.columns = custom_column_names
    # print(ld.head())

    tau_list = [0.1, 0.3, 0.5]
    pi_list = [0,0.01,0.05,0.1,0.2]
    ld_val = 0
    for t in range(len(tau_list)):
        tau = tau_list[t]
        # print(tau)
        her_df = pd.DataFrame()

        ## To get h2
        for i in range(0,len(maf)):
            frq = np.mean(correlation_matrix[i,:])
            # print(frq)
            if maf.iloc[i, maf.columns.get_loc('Predictor')] in ld['Predictor'].values:
                ld_val = 1
            else:
                ld_val = 0
            her = tau*ld_val*(frq*(1-frq))**0.75
            row_data = pd.DataFrame({'Predictor': maf.iloc[i, maf.columns.get_loc('Predictor')], 'Her': her}, index=[0])
            her_df = pd.concat([her_df,row_data],ignore_index=True)
        # print(her_df.head())
        h2 = her_df['Her'].mean()  ## h2 = sum(Her)/m
        # print(h2)

        ## Calculating the Prior(beta)
        ### The first model
        p2 = 0; p3 = 0; p4 = 1;
        p1 = 1 - (p2 + p3 + p4)
        # print(p1, p2 ,p3, p4)
        s = (p2/100 + p3/10 + p4)**(-1)
        print(s)

        beta_prior = Prior(s,h2,p1,p2,p3,p4)

        ### 34 models
        for i in range(4,-1,-1):
            p2 = pi_list[i]
            for j in range(i,-1,-1):
                p3 = pi_list[j]
                for k in range(j,-1,-1):
                    p4 = pi_list[k]
                    if(p2+p3+p4 == 0):
                        continue
                    p1 = 1 - (p2 + p3 + p4)
                    s = (p2 / 100 + p3 / 10 + p4) ** (-1)


if __name__ == '__main__':
    SumHer()