# -*- coding: utf-8 -*-
"""
热力图
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

flights_long = pd.read_csv(r"D:\Anaconda3\seaborn-data-master\seaborn-data-master\flights.csv")
flights = flights_long.pivot("month", "year", "passengers")
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=False, fmt="d", linewidths=.5, ax=ax,cmap="YlGnBu")
# plt.savefig(r'D:\Anaconda3\seaborn-data-master\jpg\test.jpg')