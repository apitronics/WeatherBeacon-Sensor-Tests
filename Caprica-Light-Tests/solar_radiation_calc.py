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

plt.close("all")

#pm data:
csv_file = 'df_pm_all_sensors.csv'

df_pm = pd.read_csv(csv_file, index_col = 'Time', parse_dates = 'Time')

#slice the good data
df_pm = df_pm.loc['2016-03-01 13:24:00': '2016-03-01 14:24:00']                

df_pm.to_csv('df_pm_slice.csv')
df_stats = df_pm.describe()
df_stats.to_csv('df_pm_stats.csv')

#print(df_stats)

col_titles = ['Cap 1 pyranometer (mV)','Cap 2 pyranometer (mV)','Cap 3 pyranometer (mV)', \
             'Cap 4 pyranometer (mV)','Cap 5 pyranometer (mV)','Cap 6 pyranometer (mV)', \
             'Cap 7 pyranometer (mV)']
             
delta_col_titles = [] 
#build new columns of calculated difference between pyranometers and Apogee
for col_name in col_titles:
    delta_col_titles.append(col_name[:5]+' delta')
    df_pm[delta_col_titles[-1]] =  abs(df_pm['Apogee pyranometer (mV)'] - df_pm[col_name])
    #df_pm.plot(x=col_name, y=delta_col_titles[-1])


#plot pyranometer vs delta for each
df_pm.plot(x=df_pm['Apogee pyranometer (mV)'], y=delta_col_titles, title='pyranometer PM plot'). \
    legend(loc='best',prop={'size':8})

#plot all pyranometer data
df_pm.filter(regex = 'pyranometer').plot(title='pyranometer PM plot').legend(loc='best',prop={'size':8})
#plot all delta data
df_pm.filter(regex='delta').plot(title='pyranometer PM plot').legend(loc='best',prop={'size':8})

############ same calc as above but for AM ############

#am data:
csv_file = 'df_am_all_sensors.csv'

df_am = pd.read_csv(csv_file, index_col = 'Time', parse_dates = 'Time')

#slice the good data
df_am = df_am.loc['2016-03-01 11:00:00': '2016-03-01 12:50:00']                

df_am.to_csv('df_am_slice.csv')
df_stats = df_am.describe()
df_stats.to_csv('df_am_stats.csv')

#print(df_stats)

col_titles = ['Cap 1 pyranometer (mV)','Cap 2 pyranometer (mV)','Cap 3 pyranometer (mV)', \
             'Cap 4 pyranometer (mV)','Cap 5 pyranometer (mV)','Cap 6 pyranometer (mV)', \
             'Cap 7 pyranometer (mV)']
             
delta_col_titles = [] 
#build new columns of calculated difference between pyranometers and Apogee
for col_name in col_titles:
    delta_col_titles.append(col_name[:5]+' delta')
    df_am[delta_col_titles[-1]] =  abs(df_am['Apogee pyranometer (mV)'] - df_am[col_name])
    #df_am.plot(x=col_name, y=delta_col_titles[-1])

df_am.plot(x=df_am['Apogee pyranometer (mV)'], y=delta_col_titles, title='pyranometer AM plot') \
    .legend(loc='best',prop={'size':8})

#plot all pyranometer data
df_am.filter(regex = 'pyranometer').plot(title='pyranometer AM plot').legend(loc='best',prop={'size':8})
#plot all delta data
df_am.filter(regex='delta').plot(title='pyranometer AM plot').legend(loc='best',prop={'size':8})