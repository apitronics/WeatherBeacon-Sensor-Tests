# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:49:50 2016

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

csv_file = '208-Mark V.csv'

#read csv file, index by timestamp, take only March 1st data
df = pd.read_csv(csv_file, index_col = 'Time', 
                 parse_dates = 'Time', date_parser=parser).loc[:, 'Solar Watts (mW)']
                 
df.plot()