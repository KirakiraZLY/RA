import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# 创建一个示例的 DataFrame，其中一列缺失列名
data = pd.DataFrame({'V1': [1, 2, 3],
                     'V2': ['A', 'B', 'C'],
                     'V3': [4.5, 5.2, 6.0],
                     'V4': ['X', 'Y', 'Z'],
                     '': [7, 8, 9]})

# 划分数据集
X = data.drop('', axis=1)  # 特征
y = data['']  # 目标变量

# 使用LabelEncoder将目标变量转换为数字
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 使用决策树分类器进行训练
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
classification_report_result = classification_report(y_test, y_pred)

# 打印结果
print("Accuracy:", accuracy)
print("Classification Report:\n", classification_report_result)

# 使用模型预测缺失列名
missing_data = data[data[''] == '']
missing_data_features = missing_data.drop('', axis=1)
predicted_colname_encoded = model.predict(missing_data_features)
predicted_colname = label_encoder.inverse_transform(predicted_colname_encoded)

# 将预测的列名填充到DataFrame中
data.loc[data[''] == '', ''] = predicted_colname

# 打印更新后的 DataFrame
print("\nDataFrame with Predicted Colname:")
print(data)
