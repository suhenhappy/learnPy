from numpy import array
from numpy.random import normal, randint

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.ndim)


#使用List来创造一组数据
data = [1, 2, 3]
print(data)
#使用ndarray来创造一组数据
data = array([1, 2, 3])
print(data)
#创造一组服从正态分布的定量数据
data = normal(0, 10, size=10)
print(data)
#创造一组服从均匀分布的定性数据
data = randint(0, 10, size=10)
print(data)

from numpy import mean, median

#计算均值
print(mean(data))
#计算中位数
print(median(data))

import pandas as pd

from pandas import Series, DataFrame

score_list = np.random.randint(30, 100, size=20)
print(score_list)

bins=[0,59,70,80,100]

score_cat = pd.cut(score_list, bins)
print(pd.value_counts(score_cat))