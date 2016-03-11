# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:18:56 2016

@author: Colin
"""



import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
plt.close("all")

#The timezone and UTC offset break our timedate, so just ignore them
parser = lambda date: pd.datetime.strptime(date[:-9], '%Y-%m-%d %H:%M:%S')  #2016-02-25 16:42:28 PST-0800

csv_files = ['224-Cap 1.csv', '225-Cap 2.csv', '226-Cap 3.csv', '227-Cap 4.csv',
             '236-Cap 5.csv', '237-Cap 6.csv', '238-Cap 7.csv', '228-Cap 8.csv']


for csv_file in csv_files:
    #read csv file, index by timestamp, take only March 1st data
    df = pd.read_csv(csv_file, index_col = 'Time', 
                     parse_dates = 'Time', date_parser=parser).loc[
                     '2016-03-01 08:00:00':]
    
    plt.subplot(3, 1, 1) 
    df.loc[:,'Air Temperature (C)'].plot(sharex=True)
    plt.ylabel('Temp (C)');
    plt.subplot(3, 1, 2) 
    df.loc[:,'Relative Humidity (%)'].plot(sharex=True)
    plt.ylabel('RH (%)');
    plt.subplot(3, 1, 3) 
    df.loc[:,'Atmospheric Pressure (hPa)'].plot()
    plt.ylabel('Pressure (hPa)');