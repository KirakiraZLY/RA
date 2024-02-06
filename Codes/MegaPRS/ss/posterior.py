import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Simulated Data
np.random.seed(42)
data = np.random.normal(loc=5.0, scale=2.0, size=1000)

# Init prior
prior_mean = np.array([0])
prior_precision = np.array([1])

# print(prior_mean, prior_precision)

# init posterior
posterior_mean = np.array([0])
posterior_precision = np.array([1])

# iter
num_iterations = 1000


for _ in range(num_iterations):
    posterior_precision = prior_precision + len(data)
    posterior_mean = (prior_precision * prior_mean + np.sum(data)) / posterior_precision

    # Elbo
    elbo = 0.5 * np.log(posterior_precision) - 0.5 * posterior_precision * (
            np.var(data) + (1 / posterior_precision) * np.sum((data - posterior_mean) ** 2)
    ) + 0.5 * np.log(prior_precision) - 0.5 * prior_precision * (
                   (1 / prior_precision) * np.sum((posterior_mean - prior_mean) ** 2)
           ) + 0.5 * np.log(2 * np.pi)

    # print("ELBO:", elbo)

# Plot
x = np.linspace(0, 10, 1000)
plt.plot(x, norm.pdf(x, loc=5.0, scale=2.0), label='True Distribution')
plt.plot(x, norm.pdf(x, loc=posterior_mean, scale=np.sqrt(1 / posterior_precision)), label='Estimated Posterior')
plt.legend()
plt.xlabel('x')
plt.ylabel('Density')
plt.title('True vs Estimated Posterior Distribution')
plt.show()
