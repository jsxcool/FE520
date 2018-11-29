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
                  'EASE-MENT', 'ADDRESS', 'APARTMENT NUMBER', 'TOTAL UNITS', 'YEAR BUILT', 'SALE DATE',
                  'BUILDING CLASS AT TIME OF SALE'], axis=1)
#print(data.head())
#print(data.corr())

data.to_csv("newdata.csv")

X = []
Y = []
with open('newdata.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue;
        # missing value 
        # 7, 8 are areas, 10 is house price
        if row[7]==' -  ' or row[8] == ' -  ' or row[10] == ' -  ':
            continue;
        # outlier
        if int(row[7])==0 or int(row[8])==0 or int(row[10]) < 100000:
            continue;
# borouch, neighborhood, building category, zip code, residental units,
# commercial units, land square, gross square, tax class, building class
# sale price
        X.append([row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                  row[8], row[9], row[10]])
        Y.append(row[10])

print(len(X))

df = pd.DataFrame(X, columns=['borouch', 'neighborhood', 'building category',
                              'zipCode', 'residental units', 'commercial units',
                              'land square', 'gross square', 'taxClass',
                              'sale price'])
df = df.drop(df.columns[1], axis=1)
df.to_csv("newnewdata.csv")



