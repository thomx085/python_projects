import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import collections

file = r'nhl.csv'

df = pd.read_csv(file)

df_list = list(df['points'])

#getting the frequency
frequency = Counter(df_list)
freq = collections.OrderedDict(sorted(frequency.items()))
freq_days = list(freq.keys())

freq_count = list(freq.values())

#creating the histogram
plt.bar(range(len(frequency)), freq_count, tick_label = freq_days)
plt.ylabel('Frequency')
plt.xlabel('Number of Days')
plt.title('Days Until Patient Paid Distribution')
plt.show()


#starting to calculate the skewness of payment days
df_skew = round(df['points'].skew(), 3)
df_kurtosis = round(df['points'].kurtosis(), 3)


#calculating the correlation
df_corr = df.corr(method = 'pearson')
print('Correlation table:\n', df_corr)
print('The skew of the days until Invoice Paid:', df_skew)
print('The kurtosis of the days until Invoice Paid:', df_kurtosis)
print('The number of classes in this dataset are:', len(freq_days))
