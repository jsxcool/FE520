'''
Data Processing I: The raw dataset has 84549 rows * 22 columns.  --too much data
(1) eliminate features we think useless or hard to utilize 
(2) eliminate missing data and outliers
'''
from pandas import DataFrame
import pandas as pd
import csv



# eliminate some features that are useless or hard to utilize 
data = pd.read_csv('nyc-rolling-sales.csv')
data = data.drop([data.columns[0], 'NEIGHBORHOOD', 'BLOCK', 'LOT', 'TAX CLASS AT PRESENT', 'BUILDING CLASS AT PRESENT',
                  'EASE-MENT', 'ADDRESS', 'APARTMENT NUMBER', 'TOTAL UNITS', 'YEAR BUILT', 'SALE DATE',
                  'BUILDING CLASS AT TIME OF SALE'], axis=1)

data.to_csv("newdata.csv")




# eliminate missing data and outliers
X = []
with open('newdata.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue;
        # missing value 
        # 6, 7 are areas, 9 is house price
        if row[6]==' -  ' or row[7] == ' -  ' or row[9] == ' -  ':
            continue;
        # outlier: areas couldn't be zero; price under 200000 is not reasonable
        if int(row[6])==0 or int(row[7])==0 or int(row[9]) < 200000:
            continue;

        X.append([row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                  row[8], row[9] ])

# features left
# borouch, building category, zip code, residental units,
# commercial units, land square, gross square, tax class, building class
# sale price

df = pd.DataFrame(X, columns=['borouch', 'building category',
                              'zipCode', 'residental units', 'commercial units',
                              'land square', 'gross square', 'taxClass',
                              'sale price'])
df.to_csv("newnewdata.csv")



