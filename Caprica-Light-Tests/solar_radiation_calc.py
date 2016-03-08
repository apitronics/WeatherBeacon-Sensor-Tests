# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 16:07:17 2016

@author: Colin
"""


import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#pm data:
csv_file = 'df_pm_all_sensors.csv'

df_pm = pd.read_csv(csv_file, index_col = 'Time', parse_dates = 'Time')

#slice the good data
df_pm = df_pm.loc['2016-03-01 13:24:00': '2016-03-01 14:24:00']                

df_pm.to_csv('df_pm_slice.csv')
df_stats = df_pm.describe()
df_stats.to_csv('df_pm_stats.csv')

#print(df_stats)

df_pm_delta = df_pm.loc[:,'Cap 1 Apogee (mV)']

df_delta =  df_pm.loc[:,'Cap 1 Apogee (mV)'] - df_pm.loc[:,'Cap 1 pyranometer (mV)']

df_pm_delta['cap 1 delta'] = df_delta
         
print(df_pm_delta)