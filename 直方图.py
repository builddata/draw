# -*- coding: utf-8 -*-
"""
直方图
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


name_list = ['a','b','c','d']
time_list = [20,30,40,30]

plt.legend()  # 让图例生效
plt.grid()
plt.xlabel(u"名字")
plt.ylabel(u"本周迟到时长/min")
sns.barplot(x=name_list, y=time_list, ci=10)
plt.show()
