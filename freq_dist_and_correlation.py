# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:33:02 2023

@author: Tanner
"""

import pandas as pd
import matplotlib.pyplot as plt


file = r'C:\Users\Tanner\Downloads\cf_ANLT5010_DataFiles\cf_ANLT5010_DataFiles\cf_ANLT5010_W2_InvoiceDayAndAmount.csv'

df = pd.read_csv(file)

df_list = list(df['Days until Invoice Paid'])

#setting the class_length
class_length = 2

#getting the range
class_range = max(df['Days until Invoice Paid']) - min(df['Days until Invoice Paid'])

#number of classes
class_number = round(class_range/class_length, 0)

#creating empty lists
class1 = []
class2 = []
class3 = []
class4 = []
class5 = []
class6 = []
class7 = []

#looping through and creating the values list
for value in df_list:
    if 10 <= value <= 12:
        class1.append(value)
    elif 13 <= value <= 15:
        class2.append(value)
    elif 16 <= value <= 18:
        class3.append(value)
    elif 19 <= value <= 21:
        class4.append(value)
    elif 22 <= value <= 24:
        class5.append(value)
    elif 25 <= value <= 27:
        class6.append(value)
    elif 28 <= value <= 30:
        class7.append(value)
     
#getting the count of values
class1 = len(class1)
class2 = len(class2)
class3 = len(class3)
class4 = len(class4)
class5 = len(class5)
class6 = len(class6)
class7 = len(class7)

#getting the classes and bin numbers
class_count = [class1,class2,class3,class4,class5,class6,class7]
bin_numbers = [1,2,3,4,5,6,7]

#creating the histogram
plt.bar(bin_numbers, class_count)
plt.ylabel('Count')
plt.xlabel('Bin Number')
plt.title('Days Until Patient Paid Distribution')
plt.show()


#starting to calculate the skewness of payment days
df_skew = round(df['Days until Invoice Paid'].skew(), 3)
df_kurtosis = round(df['Days until Invoice Paid'].kurtosis(), 3)
print('The skew of the days until Invoice Paid:', df_skew)
print('The kurtosis of the days until Invoice Paid:', df_kurtosis)

#calculating the correlation
df_corr = df.corr(method = 'pearson')
print('Correlation table:\n', df_corr)

