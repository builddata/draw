# -*- coding: utf-8 -*-
"""
密度图

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
g = sns.JointGrid(data=df, x="body_mass_g", y="bill_depth_mm", space=0)
g.plot_joint(sns.kdeplot,
             fill=True, clip=((2200, 6800), (10, 25)),
             thresh=0, levels=100, cmap="rocket")
g.plot_marginals(sns.histplot, color="#03051A", alpha=1, bins=25)