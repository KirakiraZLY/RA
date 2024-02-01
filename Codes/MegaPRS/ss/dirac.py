import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-3, 3, 1000)

delta_function = np.zeros_like(x)
delta_function[len(x)//2] = 1.0

# Normal
normal_distribution = norm.pdf(x, loc=0, scale=1)

# Combine
result = 0.9 * delta_function + 0.1 * normal_distribution

plt.plot(x, delta_function, label='Dirac Delta Function')
plt.plot(x, normal_distribution, label='N(0, 1)')
plt.plot(x, result, label='$\delta_0 + N(0, 1)$')
plt.title('$\delta_0 + N(0, 1)$')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
