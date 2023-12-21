import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np

# Define a transformer-based regression model for sequential data
class TransformerLinearRegression(nn.Module):
    def __init__(self, input_dim, hidden_dim=64, num_layers=2):
        super(TransformerLinearRegression, self).__init__()
        self.embedding = nn.Linear(input_dim, hidden_dim)
        self.transformer_layers = nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=4)
        self.transformer = nn.TransformerEncoder(self.transformer_layers, num_layers=num_layers)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        embedded = self.embedding(x)
        embedded = embedded.permute(1, 0, 2)  # Change the sequence dimension
        transformer_output = self.transformer(embedded)
        transformer_output = transformer_output.permute(1, 0, 2)  # Restore the sequence dimension
        output = self.fc(transformer_output[:, -1, :])  # Use the last transformer layer output
        return output

# Generate synthetic sequential numerical data
np.random.seed(42)
seq_length = 3
X_seq = np.random.rand(5, seq_length, 1)  # 1000 samples, 10 time steps, 1 feature
y_seq = np.sum(X_seq, axis=(1, 2)) + np.random.normal(0, 0.1, size=X_seq.shape[0])  # Regression task with noise
print(X_seq)
print(y_seq)
print(X_seq.shape)
print(y_seq.shape)
"""
# Split the data into training, validation, and testing sets
X_train, X_temp, y_train, y_temp = train_test_split(X_seq, y_seq, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
# print(X_val)


# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.reshape(-1, 1)).reshape(X_train.shape)
X_val_scaled = scaler.transform(X_val.reshape(-1, 1)).reshape(X_val.shape)
X_test_scaled = scaler.transform(X_test.reshape(-1, 1)).reshape(X_test.shape)

# Convert the data to PyTorch tensors
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
X_val_tensor = torch.tensor(X_val_scaled, dtype=torch.float32)
y_val_tensor = torch.tensor(y_val, dtype=torch.float32).view(-1, 1)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)

# Create DataLoader for training, validation, and testing
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
val_dataset = TensorDataset(X_val_tensor, y_val_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Initialize the sequential transformer linear regression model
input_dim_seq = X_train.shape[-1]
model_seq = TransformerLinearRegression(input_dim=input_dim_seq)

# Loss function and optimizer
criterion_seq = nn.MSELoss()
optimizer_seq = torch.optim.Adam(model_seq.parameters(), lr=0.001)

# Training loop
epochs_seq = 10
for epoch_seq in range(epochs_seq):
    model_seq.train()
    for inputs_seq, targets_seq in train_loader:
        optimizer_seq.zero_grad()
        outputs_seq = model_seq(inputs_seq)
        loss_seq = criterion_seq(outputs_seq, targets_seq)
        loss_seq.backward()
        optimizer_seq.step()

    # Evaluation on the validation set
    model_seq.eval()
    with torch.no_grad():
        predictions_val_seq = model_seq(X_val_tensor)
        mse_val_seq = mean_squared_error(y_val, predictions_val_seq.numpy())
        print(f"Epoch {epoch_seq + 1}/{epochs_seq}, MSE on Validation Set: {mse_val_seq}")

# Evaluation on the test set
model_seq.eval()
with torch.no_grad():
    predictions_test_seq = model_seq(X_test_tensor)
    mse_test_seq = mean_squared_error(y_test, predictions_test_seq.numpy())
    print(f"MSE on Test Set: {mse_test_seq}")
"""