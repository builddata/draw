# -*- coding: utf-8 -*-
"""
散点分布图
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats, integrate
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False


#----------------------------------------------------------------------------------------------
sns.set_theme(style="darkgrid")
tips= pd.read_csv(r"D:\Anaconda3\seaborn-data-master\seaborn-data-master\tips.csv")
print (tips.head())
g = sns.jointplot(x="total_bill", y="tip", data=tips,
                  kind="reg", truncate=False,
                  xlim=(0, 60), ylim=(0, 12),
                  color="m", height=7)


