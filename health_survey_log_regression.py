# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:58:10 2023

@author: Tanner
"""

import pandas as pd
import statsmodels.api as sm

file = r'C:\Users\Tanner\Downloads\cf_ANLT5010_DataFiles\cf_ANLT5010_DataFiles\cf_ANLT5010_W10_Penalties_ClarionCourt.csv'

df = pd.read_csv(file)

# #creating the dummy variables
df['ANYULCER'] = (df['ULCERHI'] < 8) & (df['ULCERHI'] > 0)
df['ANYULCER'] = df['ANYULCER'].astype(int)
df['ANYFALL'] = df['ANYFALLS'] == 1
df['ANYFALL'] = df['ANYFALL'].astype(int)

#creating the correlation matrix
corr_matrix = abs(df.corr())

# #sorting by highest correlation
print('Corrlation Matrix for Any Falls:\n',corr_matrix['ANYFALL'].sort_values(ascending=False)[1:15])
print('Corrlation Matrix for Any Ulcers:\n',corr_matrix['ANYULCER'].sort_values(ascending=False)[1:15])


#creating the initial ulcer variable list
ulcer_df = df[['ANYULCER', 'BEDMOBIL', 'BOWLCONT', 'BLADCONT', 'RDEMEN', 'ARTNUTR', 'OTHNUTRI', 'ANYNUTRL', 'HYDRATE', 'AGEATADM', 'SEX',
               'COMOTOSE', 'EAT', 'ANYFALL', 'WHRLIVE', 'RCONTIN', 'SPECUNIT', 'RENDLIFE', 'TRANSFER', 'HYGIENE', 'DRESS', 'SUBTHER']]

#creating the initial falls variable list
falls_df = df[['ANYFALL', 'BEDMOBIL', 'BATH', 'DRESS', 'BOWLCONT', 'HIPFRACT', 'TRANSFER', 'EAT', 'TOILET', 'WGTGAIN', 'HSPCELOS', 
               'CONDSPEC', 'HOSPADM', 'OTHFRACT', 'WGTLOSS', 'WALKING', 'HPICECOV', 'HOSPNUM']]

#creating the correlation matrix
corr_matrix_ulcers = abs(ulcer_df.corr())
corr_matrix_falls = abs(falls_df.corr())

#getting the correlation values
print('Corrlation Matrix for Any Ulcers:\n',corr_matrix_ulcers['ANYULCER'].sort_values(ascending=False))
print('Corrlation Matrix for Any Falls:\n',corr_matrix_falls['ANYFALL'].sort_values(ascending=False))


#filter out any variables that are obscure or unwanted
df = df.loc[((df['RENDLIFE'] == 1)|(df['RENDLIFE'] == 2)|(df['RENDLIFE'] == 3))]
df = df.loc[((df['WHRLIVE'] != 88)|(df['WHRLIVE'] != 99))]
df = df.loc[((df['BOWLCONT'] != 8)|(df['BOWLCONT'] != 9))]
df = df.loc[((df['RCONTIN'] != 8)|(df['RCONTIN'] != 9))]
df = df.loc[((df['RDEMEN'] != 8)|(df['RDEMEN'] != 9))]
df = df.loc[((df['BEDMOBIL'] != 88)|(df['BEDMOBIL'] != 99)|(df['BEDMOBIL'] != 8))]
df = df.loc[(df['AGEATADM'] != 999)]
df = df.loc[((df['HYGIENE'] != 88)|(df['HYGIENE'] != 99))]
df = df.loc[((df['EAT'] != 88)|(df['EAT'] != 99))]
df = df.loc[((df['DRESS'] != 88)|(df['DRESS'] != 99))]
df = df.loc[((df['TRANSFER'] != 88)|(df['TRANSFER'] != 99))]
df = df.loc[((df['SPECUNIT'] != 8)|(df['SPECUNIT'] != 9))]
df = df.loc[((df['HOSPADM'] != 8)|(df['HOSPADM'] != 9))]
df = df.loc[((df['WALKING'] != 8)|(df['WALKING'] != 9))]
df = df.loc[((df['BATH'] != 88)|(df['BATH'] != 99))]
df = df.loc[((df['HIPFRACT'] != 8)|(df['HIPFRACT'] != 9))]
df = df.loc[((df['OTHFRACT'] != 8)|(df['OTHFRACT'] != 9))]
df = df.loc[((df['TOILET'] != 88)|(df['TOILET'] != 99))]
df = df.loc[((df['WGTGAIN'] != 8)|(df['WGTGAIN'] != 9))]
df = df.loc[((df['WGTLOSS'] != 8)|(df['WGTLOSS'] != 9))]
df = df.loc[((df['BLADCONT'] != 8)|(df['BLADCONT'] != 9))]
df = df.loc[((df['ARTNUTR'] != 8)|(df['ARTNUTR'] != 9))]
df = df.loc[((df['OTHNUTRI'] != 8)|(df['OTHNUTRI'] != 9))]
df = df.loc[((df['ANYNUTRL'] != 8)|(df['ANYNUTRL'] != 9))]
df = df.loc[((df['HYDRATE'] != 8)|(df['HYDRATE'] != 9))]
df = df.loc[((df['COMOTOSE'] != 8)|(df['COMOTOSE'] != 9))]
df = df.loc[((df['SUBTHER'] != 8)|(df['SUBTHER'] != 9))]
df = df.loc[((df['HSPCELOS'] != 8888)|(df['HSPCELOS'] != 9999))]
df = df.loc[(df['CONDSPEC'] != 99)]
df = df.loc[((df['HPICECOV'] != 8)|(df['HPICECOV'] != 9))]
df = df.loc[((df['HOSPNUM'] != 8)|(df['HOSPNUM'] != 9))]

# # #check correlation matrix again
corr_matrix = abs(df.corr())
print(corr_matrix['ANYULCER'].sort_values(ascending=False))

# # #start model creation
y_ulcer = df['ANYULCER']
# x_ulcer1 = df[['BEDMOBIL', 'BOWLCONT', 'BLADCONT', 'RDEMEN', 'OTHNUTRI', 'ANYNUTRL', 'AGEATADM', 'SEX',
#                 'EAT', 'ANYFALL', 'WHRLIVE', 'RCONTIN', 'SPECUNIT', 'RENDLIFE', 'TRANSFER', 'HYGIENE', 'DRESS']]

x_ulcer2 = df[['BOWLCONT', 'BLADCONT', 'ANYNUTRL', 'SPECUNIT', 'TRANSFER', 'HYGIENE']]

# #fitting the ulcer model
x_ulcer = sm.add_constant(x_ulcer2)
ulcer_regr = sm.Logit(y_ulcer, x_ulcer).fit()
print(ulcer_regr.summary())

#2nd model iteration
x_ulcer2 = ulcer_df[['BOWLCONT', 'WHRLIVE', 'SPECUNIT', 'HYGIENE', 'TRANSFER', 'WALKING']]

# defining variables
y_fall = df['ANYFALL']
x_fall1 = df[['BEDMOBIL', 'BATH', 'DRESS', 'BOWLCONT', 'HIPFRACT', 'TRANSFER', 'EAT', 'TOILET', 'WGTGAIN', 
                'HOSPADM', 'WGTLOSS', 'WALKING']]

#second iteration of variable selection
x_fall2 = df[['TRANSFER', 'WGTGAIN', 'HOSPADM', 'DRESS', 'EAT']]

#model creation
x_fall = sm.add_constant(x_fall2)
falls_regr = sm.Logit(y_fall, x_fall).fit()

print(falls_regr.summary())
