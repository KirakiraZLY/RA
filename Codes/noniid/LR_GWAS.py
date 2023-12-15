import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(0)
num_samples = 100 # inds
num_snps = 10000 # SNPs

X = np.random.randn(num_samples, num_snps)
true_effect = np.random.randn(num_snps) # Effect size
y = np.dot(X, true_effect) + np.random.randn(num_samples)  # Y = Xb + e

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# linear regression
model = LinearRegression()
model.fit(X_train, y_train)

# Test
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Coefficient, as the effect size of each SNP
print("Estimated SNP Effects:")
print(model.coef_)
