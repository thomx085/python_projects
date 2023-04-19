# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:44:47 2023

@author: Tanner
"""

import pandas as pd
import numpy as np
import toleranceinterval as ti

#defining the file
file = r'nba.csv'

#reading in the csv
df = pd.read_csv(file, header = None)

#renaming the column
df = df.rename(columns = {0:'wait_times'})

#putting wait times to a list
sample_list = list(df['wait_times'])
sample_array = np.array(sample_list)

#calculating the different measures - central tendencies
mean = round(df['wait_times'].mean(), 3)
mode = max(set(sample_list), key = sample_list.count)
median = df['wait_times'].median()

#calculating the different measures - standard deviation
stdev = round(df['wait_times'].std(),3)

#calculating tolerance intervals
bound_68 = ti.twoside.normal(sample_array, , .95)
bound_95 = ti.twoside.normal(sample_array, .9544, .95)
bound_99 = ti.twoside.normal(sample_array, .9973, .95)

print('Mean is: ' + str(mean))
print('Mode is: ' + str(mode))
print('Median is: ' + str(median))
print('Standard Deviation is: '+ str(stdev))
print('Lower bound at 68.26% interval:', bound_68[:, 0][0].round(3))
print('Upper bound at 68.26% interval:', bound_68[:, 1][0].round(3))
print('Lower bound at 95.44% interval:', bound_95[:, 0][0].round(3))
print('Upper bound at 95.44% interval:', bound_95[:, 1][0].round(3))
print('Lower bound at 99.73% interval:', bound_99[:, 0][0].round(3))
print('Upper bound at 99.73% interval:', bound_99[:, 1][0].round(3))
