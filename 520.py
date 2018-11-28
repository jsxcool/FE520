from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt

'''
x = [90,61,24,53,94,5]
X = np.array(x)
y = [1,40,82,31,4,52]
Y = np.array(y)
z = [3,11,52,53,49,5]

O = 2*X + Y
#print(O)
data = { 'X': X, 'Y': Y, 'Z': z, 'O': O }
df = DataFrame(data)
print(df.corr())
'''

data = pd.read_csv('nyc-rolling-sales.csv')
data = data.drop([data.columns[0], 'APARTMENT NUMBER'], axis=1)
#print(data.head())
#print(data.corr())
correlation = data.corr()
fig, ax = plt.subplots(figsize=(20, 20))
ax.matshow(correlation)
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.show()



'''

'''
