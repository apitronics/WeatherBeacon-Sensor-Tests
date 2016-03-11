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
matplotlib.style.use('ggplot')
plt.close("all")


#am data:
csv_file = 'df_am_all_sensors.csv'

df_am = pd.read_csv(csv_file, index_col = 'Time', parse_dates = 'Time')

#slice the good data
df_am = df_am.loc['2016-03-01 11:00:00': '2016-03-01 12:50:00']                

df_am.to_csv('df_am_slice.csv')
df_stats = df_am.describe()
df_stats.to_csv('df_am_stats.csv')

#print(df_stats)



######## AM UNIT POSITIONS LOOKING SOUTH ############
#EAST -- 8 - 7 - 6 - 5 - 4 - 3 - 2 - 1 - AG -- WEST#
####################################################
unit_positions = [1, 2, 3, 4, 5, 6, 7, 8]

col_titles = ['Cap 1 pyranometer (mV)','Cap 2 pyranometer (mV)','Cap 3 pyranometer (mV)', \
             'Cap 4 pyranometer (mV)','Cap 5 pyranometer (mV)','Cap 6 pyranometer (mV)', \
             'Cap 7 pyranometer (mV)', 'Cap 8 pyranometer (mV)']
             
delta_col_titles = [] 
position_col_titles = [] 
error_col_titles = [] 

#build new columns of calculated difference between pyranometers and Apogee
itera = 0
for col_name in col_titles:
    delta_col_titles.append(col_name[:5]+' delta')
    df_am[delta_col_titles[-1]] =  (df_am['Apogee pyranometer (mV)'] - df_am[col_name])
    #add error columns
    error_col_titles.append(col_name[:5]+' error')
    df_am[error_col_titles[-1]] =  abs(df_am['Apogee pyranometer (mV)'] - df_am[col_name])/df_am['Apogee pyranometer (mV)']     
    #add positions columns
    position_col_titles.append(col_name[:5]+' position')
    df_am[position_col_titles[-1]] =  unit_positions[itera]
    itera += 1
    
#delta_col_titles.append('AG 5pcnt delta')
#df_am['AG 5pcnt delta'] = df_am['Apogee pyranometer (mV)']* 0.05  

##plot deltas to AG mV
#df_am.plot(x=df_am['Apogee pyranometer (mV)'], y=delta_col_titles, title='pyranometer AM plot') \
#    .legend(loc='best',prop={'size':8})
#    
##plot error to AG mV
#df_am.plot(x=df_am['Apogee pyranometer (mV)'], y=error_col_titles, title='pyranometer AM plot') \
#    .legend(loc='best',prop={'size':8})

#plot all pyranometer data
df_am.filter(regex = 'pyranometer').plot(title='AM Pyranometer slice').legend(loc='best',prop={'size':8})
plt.ylabel('milliVolts')
#plot all delta data
df_am.filter(regex='delta').plot(title='AM Pyranometer delta').legend(loc='best',prop={'size':8})
plt.ylabel('milliVolts')
#plot all error data
#y_range = np.arange(-0.03, 0.11, 0.01)
df_am.filter(regex='error').plot(title='AM Pyranometer Error').legend(loc='best',prop={'size':8})
plt.ylabel('Percent Error to Apogee')

#######################################################
############ same calc as above but for PM ############
#######################################################

#pm data:
csv_file = 'df_pm_all_sensors.csv'

df_pm = pd.read_csv(csv_file, index_col = 'Time', parse_dates = 'Time')

#slice the good data
df_pm = df_pm.loc['2016-03-01 13:24:00': '2016-03-01 14:24:00']                

df_pm.to_csv('df_pm_slice.csv')
df_stats = df_pm.describe()
df_stats.to_csv('df_pm_stats.csv')

#print(df_stats)

######## PM UNIT POSITIONS LOOKING SOUTH ############
#EAST -- 2 - 3 - 4 - 5 - 6 - 7 - 8 - 1 - AG -- WEST#
####################################################
unit_positions = [1, 8, 7, 6, 5, 4, 3, 2]

col_titles = ['Cap 1 pyranometer (mV)','Cap 2 pyranometer (mV)','Cap 3 pyranometer (mV)', \
             'Cap 4 pyranometer (mV)','Cap 5 pyranometer (mV)','Cap 6 pyranometer (mV)', \
             'Cap 7 pyranometer (mV)', 'Cap 8 pyranometer (mV)']
             
delta_col_titles = [] 
position_col_titles = [] 
error_col_titles = [] 

#build new columns of calculated difference between pyranometers and Apogee
itera = 0
for col_name in col_titles:
    delta_col_titles.append(col_name[:5]+' delta')
    df_pm[delta_col_titles[-1]] =  (df_pm['Apogee pyranometer (mV)'] - df_pm[col_name])
    #add error columns
    error_col_titles.append(col_name[:5]+' error')
    df_pm[error_col_titles[-1]] =  abs(df_pm['Apogee pyranometer (mV)'] - df_pm[col_name])/df_pm['Apogee pyranometer (mV)']         
    #add positions columns
    position_col_titles.append(col_name[:5]+' position')
    df_pm[position_col_titles[-1]] =  unit_positions[itera]
    itera += 1

#delta_col_titles.append('AG 5pcnt delta')
#df_pm['AG 5pcnt delta'] = df_pm['Apogee pyranometer (mV)']* 0.05  

##plot delta to AG mV
#df_pm.plot(x=df_pm['Apogee pyranometer (mV)'], y=delta_col_titles, title='pyranometer PM plot'). \
#    legend(loc='best',prop={'size':8})
#
##plot error to AG mV
#df_pm.plot(x=df_pm['Apogee pyranometer (mV)'], y=error_col_titles, title='pyranometer PM plot') \
#    .legend(loc='best',prop={'size':8})

#plot all pyranometer data
df_pm.filter(regex = 'pyranometer').plot(title='PM Pyranometer slice').legend(loc='best',prop={'size':8})
plt.ylabel('milliVolts')
#plot all delta data
df_pm.filter(regex='delta').plot(title='PM Pyranometer delta').legend(loc='best',prop={'size':8})
plt.ylabel('milliVolts')
#plot all error data
df_pm.filter(regex='error').plot(title='PM Pyranometer Error').legend(loc='best',prop={'size':8});
plt.ylabel('Percent Error to Apogee');


############ combine AM and PM ############
#get stats on am error data
df_am_errstats = df_am.filter(regex='error').describe()
#transpose data and rename columns
df_am_errstats = df_am_errstats.transpose()
df_am_errstats = df_am_errstats.rename(columns={'std': 'AM std'})
df_am_errstats = df_am_errstats.rename(columns={'mean': 'AM mean'})

#get stats on pm error data
df_pm_errstats = df_pm.filter(regex='error').describe()
#transpose data and rename columns
df_pm_errstats = df_pm_errstats.transpose()
df_pm_errstats = df_pm_errstats.rename(columns={'std': 'PM std'})
df_pm_errstats = df_pm_errstats.rename(columns={'mean': 'PM mean'})

#combine AM and PM stats
df_all_errstats = pd.concat([df_pm_errstats, df_am_errstats],axis=1)


df_all_errstats.loc[:,['AM std', 'PM std']].plot(kind='bar',title='Pyranometers Error STD').legend(loc='best',prop={'size':8});
plt.ylabel('Standard Deviation');

df_all_errstats.loc[:,['AM mean', 'PM mean']].plot(kind='bar',title='Pyranometers Error Mean').legend(loc='best',prop={'size':8});
plt.ylabel('Mean');
