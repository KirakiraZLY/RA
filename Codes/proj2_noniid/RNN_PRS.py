import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# 假设基因型数据是一个时间序列，每个时间步代表一个基因
# 这里使用随机数据来模拟
np.random.seed(0)
n_samples = 10
n_genes = 500
time_steps = 10

# 生成输入数据，每个时间步代表一个基因的基因型
X = np.random.randint(3, size=(n_samples, time_steps, n_genes))  # 0, 1, 2表示基因型
X_test = np.random.randint(3, size=(n_samples, time_steps, n_genes))  # 0, 1, 2表示基因型
# 随机生成每个基因的权重
gene_weights = np.random.randn(n_genes)

# print(X, gene_weights)

# 计算每个样本的基因型分数（加权和）
prs_scores = np.sum(X * gene_weights, axis=(1, 2)) # Real phenotypes
prs_scores_test = np.sum(X_test * gene_weights, axis=(1, 2)) # Real phenotypes


# 构建RNN模型
model = Sequential()
model.add(SimpleRNN(10, activation='relu', input_shape=(time_steps, n_genes)))
model.add(Dense(1, activation='linear'))  # linear output, for regression

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X, prs_scores, epochs=10, batch_size=32, validation_split=0.2)

# Predicting PRS
predicted_prs = model.predict(X_test)

print("PRS_Score: ", prs_scores_test)
print("Predicted_PRS: ", predicted_prs)
