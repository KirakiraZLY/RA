import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.nn import Transformer
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import accuracy_score

mlb = MultiLabelBinarizer()
class CustomDataset(Dataset):
    def __init__(self, dataframe1, dataframe2):
        self.data1 = dataframe1
        self.data2 = dataframe2

    def __len__(self):
        return len(self.data1)

    def __getitem__(self, idx):
        features1 = torch.tensor(self.data1.iloc[idx][['feature1_data1', 'feature2_data1', 'feature3_data1']].values,
                                 dtype=torch.float32)
        features2 = torch.tensor(self.data2.iloc[idx][['feature1_data2', 'feature2_data2', 'feature3_data2']].values,
                                 dtype=torch.float32)
        labels1 = torch.tensor(self.data1.iloc[idx][mlb.classes_].values, dtype=torch.float32)
        labels2 = torch.tensor(self.data2.iloc[idx][mlb.classes_].values, dtype=torch.float32)

        return features1, features2, labels1, labels2

class TransformerModel(nn.Module):
    def __init__(self, input_size, output_size, num_layers, heads, hidden_size, dropout):
        super(TransformerModel, self).__init__()
        self.transformer = Transformer(d_model=input_size, nhead=heads, num_encoder_layers=num_layers,
                                       dim_feedforward=hidden_size, dropout=dropout)
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        x1, x2 = x
        x1 = self.transformer(x1)
        x1 = x1.mean(dim=1)

        x2 = self.transformer(x2)
        x2 = x2.mean(dim=1)

        x = torch.cat([x1, x2], dim=1)
        x = self.fc(x)
        return x


def Tran(df1, df2):
    mlb = MultiLabelBinarizer()
    df1_labels = pd.DataFrame(mlb.fit_transform(df1['labels_data1'].apply(lambda x: x.split(','))),
                              columns=mlb.classes_)
    df1 = pd.concat([df1, df1_labels], axis=1)

    df1_labels = pd.DataFrame(mlb.fit_transform(df1['labels_data1'].apply(lambda x: x.split(','))),
                              columns=mlb.classes_)
    df2_labels = pd.DataFrame(mlb.transform(df2['labels_data2'].apply(lambda x: x.split(','))), columns=mlb.classes_)

    df1 = pd.concat([df1, df1_labels], axis=1)
    df2 = pd.concat([df2, df2_labels], axis=1)

    train_df1, test_df1 = train_test_split(df1, test_size=0.2, random_state=42)
    train_df2, test_df2 = train_test_split(df2, test_size=0.2, random_state=42)

    train_dataset = CustomDataset(train_df1, train_df2)
    test_dataset = CustomDataset(test_df1, test_df2)
    print(train_dataset[0][0])

    """
    train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=2, shuffle=False)

    input_size = len(train_dataset[0][0])
    output_size = len(mlb.classes_)
    num_layers = 2
    heads = 2
    hidden_size = 16
    dropout = 0.1

    transformer_model = TransformerModel(input_size, output_size, num_layers, heads, hidden_size, dropout)


    ######## Loss Function and Optimizer
    criterion = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(transformer_model.parameters(), lr=0.001)

    ######## Train

    num_epochs = 5
    for epoch in range(num_epochs):
        transformer_model.train()
        for features1, features2, labels1, labels2 in train_loader:
            optimizer.zero_grad()
            outputs = transformer_model([features1, features2])
            loss1 = criterion(outputs[:, :output_size], labels1)
            loss2 = criterion(outputs[:, output_size:], labels2)
            loss = loss1 + loss2
            loss.backward()
            optimizer.step()

        transformer_model.eval()
        with torch.no_grad():
            predictions = torch.sigmoid(transformer_model([test_dataset[:][0], test_dataset[:][1]]))
            predictions[predictions >= 0.5] = 1
            predictions[predictions < 0.5] = 0
            acc = accuracy_score(test_dataset[:][2].numpy(), predictions[:, :output_size].numpy())
            print(f'Epoch [{epoch + 1}/{num_epochs}], Accuracy: {acc:.4f}')

    transformer_model.eval()
    with torch.no_grad():
        predictions = torch.sigmoid(transformer_model([test_dataset[:][0], test_dataset[:][1]]))
        predictions[predictions >= 0.5] = 1
        predictions[predictions < 0.5] = 0
        acc = accuracy_score(test_dataset[:][2].numpy(), predictions[:, :output_size].numpy())
        print(f'Final Accuracy on Test Set: {acc:.4f}')
    
    """