import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from scipy.stats import entropy
import math

def Posterior(beta_prior, z, n):
    ## Prior
    beta_prior_mean = np.mean(beta_prior)
    beta_prior_precision = 1 / np.var(beta_prior)

    ## Init Posterior
    beta_post_mean = np.array([0])
    beta_post_precision = np.array([1])

    n_sqrt = n.apply(np.sqrt)
    beta_obs = np.divide(z, n_sqrt)

    num_iter = 1000
    for i in range(num_iter):
        beta_post_precision = beta_prior_precision + len(beta_obs)
        beta_post_mean = (beta_prior_precision * beta_prior_mean + np.sum(beta_obs)) / beta_post_precision

        elbo = 0.5 * np.log(beta_post_precision) - 0.5 * beta_post_precision * (
                np.var(beta_obs) + (1 / beta_post_precision) * np.sum((beta_obs - beta_post_mean) ** 2)
        ) + 0.5 * np.log(beta_prior_precision) - 0.5 * beta_prior_precision * (
                       (1 / beta_prior_precision) * np.sum((beta_post_mean - beta_prior_mean) ** 2)
               ) + 0.5 * np.log(2 * np.pi)

    x = np.linspace(0, 10, 1000)
    plt.plot(x, norm.pdf(x, loc=beta_prior_mean, scale=beta_prior_precision), label='True Distribution')
    plt.plot(x, norm.pdf(x, loc=beta_post_mean, scale=np.sqrt(1 / beta_post_precision)), label='Estimated Posterior')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.title('True vs Estimated Posterior Distribution')
    plt.show()

def KL(P,Q):
    P = np.asarray(P)
    Q = np.asarray(Q)
    epsilon = 0.00001

    # You may want to instead make copies to avoid changing the np arrays.
    P = P+epsilon
    Q = Q+epsilon

    divergence = np.sum(P*np.log(P/Q))
    return divergence

def KL_Diverg(beta, z, n):
    n_sqrt = n.apply(np.sqrt)
    # print("N sqrt: ", n_sqrt.head())
    beta_obs = np.divide(z, n_sqrt)
    # print("Z/n: ", beta_obs.head())

    beta = pd.Series(beta)
    beta = beta.to_numpy()
    beta_obs = beta_obs.to_numpy()
    beta_obs = np.random.choice(beta_obs, size=1000, replace=False)
    print("Beta: ", beta[:5])
    print("Beta Obs: ", beta_obs[:5])
    print("Data Type: ", type(beta), type(beta_obs))
    dist = KL(beta, beta_obs)
    print("distance: ", dist, type(dist))
    return dist


def Distance(beta, z, n):
    n_sqrt = n.apply(np.sqrt)
    beta_obs = np.divide(z, n_sqrt)
    beta = pd.Series(beta)
    beta = beta.to_numpy()
    beta_obs = beta_obs.to_numpy()
    beta_obs = np.random.choice(beta_obs, size=1000, replace=False)

    # return np.mean((beta - beta_obs)**2)
    return np.corrcoef(beta, beta_obs)[0, 1]
def Prior(s,h2,p1,p2,p3,p4):
    x = np.linspace(-3, 3, 1000)

    delta_function = np.zeros_like(x)
    delta_function[len(x) // 2] = 1.0

    # Normal
    normal_distribution = p2 * norm.pdf(x, loc=0, scale=s*h2/100) + p3 * norm.pdf(x, loc=0, scale=s*h2/10) + p4 * norm.pdf(x, loc=0, scale=s*h2)

    result = p1 * delta_function + normal_distribution
    # print(result)

    """
    plt.plot(x, delta_function, label='Dirac Delta Function')
    plt.plot(x, normal_distribution, label='N(0, 1)')
    plt.plot(x, result, label='$\delta_0 + N(0, 1)$')
    plt.title('$\delta_0 + N(0, 1)$')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()
    """
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

    ## Read Summary Statistics

    ss_file_path = "D:\Aarhus_RA\Project\RA\Codes\MegaPRS\ss\\finngen_R10_AB1_MYSOSIS_NOS.ldak"
    ss = pd.read_csv(ss_file_path, sep=' ')
    ss_train, ss_test = train_test_split(ss, test_size=0.2, random_state=42)
    # print(ss_train["Z"].head())
    # print(ss_train.head())

    tau_list = [0.1, 0.3, 0.5]
    pi_list = [0,0.01,0.05,0.1,0.2]
    ld_val = 0

    # dist_distrib = float('inf') # Distance in finding best Beta Prior, by using KL divergence
    dist_distrib = 0
    # print(dist_distrib)

    best_model = 0
    best_beta_prior = 0
    best_tau = 0

    model_count = 0

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
        # print(s)

        beta_prior = Prior(s,h2,p1,p2,p3,p4)
        # dist = KL_Diverg(beta_prior, ss["Z"],ss["n"])
        dist = Distance(beta_prior, ss["Z"],ss["n"])
        print("Distance: ", dist, dist_distrib)
        model_count += 1
        if abs(dist) > abs(dist_distrib):
            dist_distrib = dist
            best_beta_prior = beta_prior
            best_model = model_count
            best_tau = tau

        print("Model: ", model_count, " tau: ", tau, " p2: ", p2, " p3: ", p3, " p4: ", p4)


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
                    beta_prior = Prior(s, h2, p1, p2, p3, p4)
                    # dist = KL_Diverg(beta_prior, ss["Z"],ss["n"])
                    dist = Distance(beta_prior, ss["Z"], ss["n"])
                    print("Distance: ", dist, dist_distrib)
                    model_count += 1
                    if abs(dist) > abs(dist_distrib):
                        dist_distrib = dist
                        best_beta_prior = beta_prior
                        best_model = model_count
                        best_tau = tau

                    print("Model: ", model_count, " tau: ", tau, " p2: ", p2, " p3: ", p3, " p4: ", p4)

    print("Best Beta Prior Model: ", best_model)

    Posterior(beta_prior, ss["Z"],ss["n"])

if __name__ == '__main__':
    SumHer()