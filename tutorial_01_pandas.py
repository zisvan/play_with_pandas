# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:10:25 2017

@author: ZIsvan
"""

import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 12, 31)

df = web.DataReader("XOM", "yahoo", start, end)

#print(df)
print(df.head())


# plot the data
style.use('fivethirtyeight')
df['High'].plot()
df['Low'].plot()
plt.legend()
#plt.show()
