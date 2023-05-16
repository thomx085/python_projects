# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:47:33 2023

@author: Tanner
"""

#import libraries
import pandas as pd
from scipy import stats
import numpy as np

#define and read in data source
file = r'C:\Users\Tanner\Downloads\cf_ANLT5010_DataFiles\cf_ANLT5010_DataFiles\cf_ANLT5010_W5_Sales_Data.csv'
df = pd.read_csv(file)

#separating the dataframe by store type
store_a = df.loc[df['Store'] == 'A']
store_b = df.loc[df['Store'] == 'B']

#creating a list to iterate over for each store
store_a_list = list(store_a['Sales'])
store_b_list = list(store_b['Sales'])

#calculating central tendencies
average_sales_a = store_a['Sales'].mean()
median_sales_a = store_a['Sales'].median()
mode_sales_a = max(set(store_a_list), key = store_a_list.count)
average_sales_b = store_b['Sales'].mean()
median_sales_b = store_b['Sales'].median()
mode_sales_b = max(set(store_b_list), key = store_b_list.count)
print('Average Sales for Store A:', round(average_sales_a,3))
print('Average Sales for Store B:', round(average_sales_b,3))
print('Median Sales for Store A:', median_sales_a)
print('Median Sales for Store B:', median_sales_b)
print('Mode Sales for Store A:', mode_sales_a)
print('Mode Sales for Store B:', mode_sales_b)

# #creating the 95% confidence level
stdev_a = round(store_a['Sales'].std(),3)
stdev_b = round(store_b['Sales'].std(),3)
upper_95_a = round(average_sales_a + (stdev_a)*2, 3)
upper_95_b = round(average_sales_b + (stdev_b)*2, 3)
lower_95_a = round(average_sales_a - (stdev_a)*2, 3)
lower_95_b = round(average_sales_b - (stdev_b)*2, 3)
print('Upper bound at a 95% Confidence Level for Store A:', upper_95_a)
print('Lower bound at a 95% Confidence Level for Store A:', lower_95_a)
print('Upper bound at a 95% Confidence Level for Store B:', upper_95_b)
print('Lower bound at a 95% Confidence Level for Store B:', lower_95_b)

#H0: Store A's average daily sales for the year will significantly exceed $4900 at a 90% confidence level
#H1: Store A's average daily sales for the year will not significantly exceed $4900 at a 90% confidence level

#Performing the sample test on store A
ttest_a = stats.ttest_1samp(a=store_a['Sales'], popmean=4900)
print('Store A ttest results:', ttest_a)

#H0: Store B's average daily sales for the year will significantly exceed $4900 at a 90% confidence level
#H1: Store B's average daily sales for the year will not significantly exceed $4900 at a 90% confidence level

#Performing the sample test on store B
ttest_b = stats.ttest_1samp(a=store_b['Sales'], popmean=4900)
print('Store B ttest results:', ttest_b)

#H0: Store A's average daily sales < store B's average daily sales at a 90% confidence level
#H1: Store A's average daily sales >= store B's average daily sales at a 90% confidence level

#ensuring the population variances are equal or less than 4:1
print('The variance between samples is:',np.var(np.array(store_a_list))/np.var(np.array(store_b_list)))

#conducting the ttest between the stores
ttest = stats.ttest_ind(a=store_a['Sales'], b=store_b['Sales'], equal_var=True)
print(ttest)




