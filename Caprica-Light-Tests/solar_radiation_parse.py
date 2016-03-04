# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 11:03:48 2016

@author: Colin
"""


import pandas as pd

import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

#The timezone and UTC offset break our timedate, so just ignore them
parser = lambda date: pd.datetime.strptime(date[:-9], '%Y-%m-%d %H:%M:%S')  #2016-03-01 12:16:04

csv_files = ['224-Cap 1.csv', '225-Cap 2.csv', '226-Cap 3.csv', '227-Cap 4.csv',
             '236-Cap 5.csv', '237-Cap 6.csv', '238-Cap 7.csv', '228-Cap 8.csv']

for csv_file in csv_files:
    #print(csv_file)
    #read csv file, index by timestamp, take only March 1st data
    df = pd.read_csv(csv_file, index_col = 'Time', 
                     parse_dates = 'Time', date_parser=parser).loc['2016-03-01 08:00:00':]
                    
    #find all the resets that occured
    df_restarts = df.loc[df['Status ()']>0].index
    
    
    #take all from start to one before reset
    df_am_slice = df.loc[:df_restarts[-1]].iloc[:-1]
    
    #print(df_am_slice['Status ()'].tail())
    
    #take all from last reset to end
    df_pm_slice = df.loc[df_restarts[-1]:]
    
    
    df_am_slice['Solar Radiation (W/m²)'].plot()
    #df_pm_slice['Solar Radiation (W/m²)'].plot()


plt.xlabel('Time')
plt.ylabel('Solar Radiation (W/m²)')