# -*- coding: utf-8 -*-
"""
箱型图
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


#-------------------------------------------------------------------------------------------


f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("log")
planets= pd.read_csv(r"D:\Anaconda3\seaborn-data-master\seaborn-data-master\planets.csv")

sns.boxplot(x="distance", y="method", data=planets,
            whis=[0, 100], width=.6, palette="vlag")

sns.stripplot(x="distance", y="method", data=planets,
              size=4, color=".3", linewidth=0)

ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)