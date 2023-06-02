# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:09:39 2023

@author: tanne
"""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

file = r'C:\Users\tanne\Downloads\cf_ANLT5010_DataFiles\cf_ANLT5010_W8_ Height_Shoe_Size.txt.TXT'

df = pd.read_csv(file, sep = '\t')

#defining the dependent and independent variables
x = df['Height']
y = df['Shoe Size']

print(df.head())

#creating the scatter plot
plt.scatter(x, y, s = 1, c = "purple")
plt.xlabel('Height')
plt.ylabel('Shoe Size')

# #investigating the scatter plot results
df_height49 = df.loc[df['Height'] == 49]
df_shoe_list = list(df_height49['Shoe Size'])
shoe_size_list = [4.0,5.0,7.5,6.5,5.5]
for shoe_size in shoe_size_list:
    temp_count = df_shoe_list.count(shoe_size)
    print('Number of entries for height 49 and shoe size',shoe_size,':',temp_count)

#calculating the pearson coefficient
corr = df.corr()
print('The correlation between the two variables is:', round(corr.loc['Shoe Size', 'Height'],4))

#running the simple linear regression
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())

#predicting the shoe size given the height
shoe_size_pred = -5.9747 + 0.2314*(49)
print(shoe_size_pred)
print('Average Shoe Size for Height 49:', df_height49['Shoe Size'].mean())





