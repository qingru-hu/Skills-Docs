from asyncio.base_subprocess import BaseSubprocessTransport
from functools import _lru_cache_wrapper
from sklearn.datasets import load_boston
bostonHouse = load_boston()
x = bostonHouse.data
y = bostonHouse.target
# import pandas as pd
# import numpy as np


# data_url = "http://lib.stat.cmu.edu/datasets/boston"
# raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
# x = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
# y = raw_df.values[1::2, 2]
# print(len(x)) 
# print(len(y))
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
print(len(x_train))
print(len(y_train))
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)
lr_predict_y = lr.predict(x_test)

from sklearn.metrics import mean_squared_error
print(f"MES:{mean_squared_error(y_test, lr_predict_y)}")
