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
#matplotlib.style.use('ggplot')

#The timezone and UTC offset break our timedate, so just ignore them
parser = lambda date: pd.datetime.strptime(date[:-9], '%Y-%m-%d %H:%M:%S')  #2016-02-25 16:42:28 PST-0800

csv_files = ['224-Cap 1.csv', '225-Cap 2.csv', '226-Cap 3.csv', '227-Cap 4.csv',
             '236-Cap 5.csv', '237-Cap 6.csv', '238-Cap 7.csv', '228-Cap 8.csv']

csv_file = csv_files[0]

#read csv file, index by timestamp, take only March 1st data
df = pd.read_csv(csv_file, index_col = 'Time', 
                 parse_dates = 'Time', date_parser=parser).loc[
                 '2016-03-01 08:00:00':]
                 

                
#find all the resets that occured
df_restarts = df.loc[df['Status ()']>0].index    
#take all from start to one before reset
df_am_all_sensors = df.loc[:df_restarts[-1],['Analog 3 (mV)','Solar Radiation (W/m²)']].iloc[:-1]
#take all from last reset to end
df_pm_all_sensors = df.loc[df_restarts[-1]:,['Analog 3 (mV)','Solar Radiation (W/m²)']]


#df_pm_all_sensors.loc[:,'Solar Radiation (W/m²)'].plot()

#rename columns
df_am_all_sensors = df_am_all_sensors.rename(columns={'Analog 3 (mV)':'Cap 1 Apogee (mV)',
'Solar Radiation (W/m²)':csv_file[4:-4]+' pyranometer (mV)'})
df_pm_all_sensors = df_pm_all_sensors.rename(columns={'Analog 3 (mV)':'Cap 1 Apogee (mV)',
'Solar Radiation (W/m²)':csv_file[4:-4]+' pyranometer (mV)'})


for csv_file in csv_files[1:]:
    #read csv file, index by timestamp, take only March 1st data
    df = pd.read_csv(csv_file, index_col = 'Time', 
                     parse_dates = 'Time', date_parser=parser).loc[
                     '2016-03-01 08:00:00':]
                    
    #find all the resets that occured
    df_restarts = df.loc[df['Status ()']>0].index    
    #take all from start to one before the last reset (when we moved all the units)
    df_am_slice = df.loc[:df_restarts[-1],['Solar Radiation (W/m²)']].iloc[:-1]
    #take all from last reset to end
    df_pm_slice = df.loc[df_restarts[-1]:,['Solar Radiation (W/m²)']]
    
    
    #df_pm_slice.loc[:,'Solar Radiation (W/m²)'].plot()
    #df_am_slice.loc[:,'Solar Radiation (W/m²)'].plot()
    
    #add data slices to all_sensors dataframe
    df_pm_all_sensors = pd.concat([df_pm_all_sensors, df_pm_slice], axis=1) 
    df_pm_all_sensors = df_pm_all_sensors.rename(columns={'Solar Radiation (W/m²)':csv_file[4:-4]+' pyranometer (mV)'})    
    
    df_am_all_sensors = pd.concat([df_am_all_sensors, df_am_slice], axis=1) 
    df_am_all_sensors = df_am_all_sensors.rename(columns={'Solar Radiation (W/m²)':csv_file[4:-4]+' pyranometer (mV)'})    
     

df_am_all_sensors = df_am_all_sensors.interpolate(method='time')
df_pm_all_sensors = df_pm_all_sensors.interpolate(method='time')

df_am_all_sensors.plot()

df_pm_all_sensors.plot()
plt.xlabel('Time')
plt.ylabel('Raw Solar Radiation (mV)')


df_am_all_sensors.to_csv('df_am_all_sensors.csv')
df_pm_all_sensors.to_csv('df_pm_all_sensors.csv')