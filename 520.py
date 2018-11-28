from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import csv

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
data = data.drop([data.columns[0], 'BLOCK', 'LOT', 'TAX CLASS AT PRESENT', 'BUILDING CLASS AT PRESENT',
                  'EASE-MENT', 'ADDRESS', 'APARTMENT NUMBER', 'TOTAL UNITS', 'YEAR BUILT', 'SALE DATE'], axis=1)
#print(data.head())
#print(data.corr())
'''correlation = data.corr()
fig, ax = plt.subplots(figsize=(20, 20))
ax.matshow(correlation)
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.show()'''
data.to_csv("newdata.csv")

X = []
Y = []
with open('newdata.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue;
        # missing value 
        if row[7]==' -  ' or row[8] == ' -  ' or row[11] == ' -  ':
            continue;
        # outlier
        if int(row[11]) < 5000:
            continue;
# borouch, neighborhood, building category, zip code, residental units,
# commercial units, land square, gross square, tax class, building class
# sale price
        X.append([row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                  row[8], row[9], row[10], row[11]])
        Y.append(row[11])

print(len(X))

df = pd.DataFrame(X, columns=['borouch', 'neighborhood', 'building category',
                              'zipCode', 'residental units', 'commercial units',
                              'land square', 'gross square', 'taxClass',
                              'buildingClass', 'sale price'])
df.to_csv("newnewdata.csv")






