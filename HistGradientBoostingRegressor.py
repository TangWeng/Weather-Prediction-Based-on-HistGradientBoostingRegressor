import pandas as pd
import numpy as np
from sklearnex import patch_sklearn
patch_sklearn()

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
from tqdm import tqdm

# 加载数据集
train_dataSet = pd.read_csv('modified_数据集Time_Series448_detail.dat')  # 从文件中加载训练数据集
test_dataSet = pd.read_csv('modified_数据集Time_Series660_detail.dat')  # 从文件中加载测试数据集

# 定义列名，原始数据列名和添加噪声后的列名
columns = ['T_SONIC', 'CO2_density', 'CO2_density_fast_tmpr', 'H2O_density', 'H2O_sig_strgth', 'CO2_sig_strgth', 'RECORD']
noise_columns = ['Error_T_SONIC', 'Error_CO2_density', 'Error_CO2_density_fast_tmpr', 'Error_H2O_density', 'Error_H2O_sig_strgth', 'Error_CO2_sig_strgth', 'Error_RECORD']

# 确认列名存在
assert all(col in train_dataSet.columns for col in noise_columns + columns), "训练数据集的列名不匹配"
assert all(col in test_dataSet.columns for col in noise_columns + columns), "测试数据集的列名不匹配"

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(train_dataSet[noise_columns], train_dataSet[columns], test_size=0.2, random_state=42)

# 确保索引匹配
y_test = y_test.reset_index(drop=True)
X_test = X_test.reset_index(drop=True)

# 定义模型列表
models = {col: HistGradientBoostingRegressor() for col in columns}

# 训练多个单目标回归模型，并显示训练进度
for col in tqdm(columns, desc="Training models"):
    models[col].fit(X_train, y_train[col])

# 预测并计算误差
predictions = pd.DataFrame({col: models[col].predict(X_test) for col in columns})
errors = np.abs(y_test.values - predictions.values)

# 确保所有列名正确
assert all(col in y_test.columns for col in columns), "y_test列名不匹配"
assert all(col in predictions.columns for col in columns), "预测结果列名不匹配"

# 将结果写入CSV文件
results = pd.DataFrame({
    'True_Value': y_test.apply(lambda row: ' '.join(map(str, row)), axis=1),
    'Predicted_Value': predictions.apply(lambda row: ' '.join(map(str, row)), axis=1),
    'Error': pd.DataFrame(errors, columns=columns).apply(lambda row: ' '.join(map(str, row)), axis=1)
})

# 将结果保存为CSV
results.to_csv("result_HistGBDT.csv", index=False)
