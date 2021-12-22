# -*- coding: utf-8 -*-
"""
散点图
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats, integrate

df = pd.read_csv(r"D:\Anaconda3\seaborn-data-master\seaborn-data-master\penguins.csv")
print (df.head())
sns.set_theme()
sns.pairplot(df, hue="species")
# plt.savefig(r'D:\Anaconda3\seaborn-data-master\jpg\test.jpg')