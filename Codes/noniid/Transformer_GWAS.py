import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, MultiHeadAttention, GlobalAveragePooling1D

np.random.seed(0)
num_samples = 100 # inds
sequence_length = 1000 # SNPs
num_features = 1

# genotype and phenotype
X = np.random.randn(num_samples, sequence_length, num_features)
y = np.random.randint(2, size=(num_samples, 1))  # Binary Phenotypes

num_train = int(num_samples * 0.8)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Transformer
inputs = Input(shape=(sequence_length, num_features))
attention_output = MultiHeadAttention(num_heads=1, key_dim=1)(inputs, inputs)
pooling_output = GlobalAveragePooling1D()(attention_output)
outputs = Dense(1, activation='-')(pooling_output)

model = Model(inputs, outputs)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

y_pred = model.predict(X_test)

print(y_pred) # Classification

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
