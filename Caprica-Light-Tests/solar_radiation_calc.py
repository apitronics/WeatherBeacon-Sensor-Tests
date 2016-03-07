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

csv_file = 'df_pm_all_sensors.csv'

df = pd.read_csv(csv_file, index_col = 'Time', parse_dates = 'Time')
                
#slice the good data
df = df.loc['2016-03-01 13:24:00': '2016-03-01 14:24:00']                
                 
df_stats = df.describe()

print(df_stats)    
                 
df.plot()