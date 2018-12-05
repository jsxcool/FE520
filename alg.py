from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import csv
from sklearn import linear_model

#Do 1~9 have a sequence ? eg, from cheap - expensive 
dic = {"01 ONE FAMILY DWELLINGS                    ":1, 
       "02 TWO FAMILY DWELLINGS                    ":1,
       "03 THREE FAMILY DWELLINGS                  ":1,
	   "04 TAX CLASS 1 CONDOS                      ":2,
	   "05 TAX CLASS 1 VACANT LAND                 ":3,
	   "06 TAX CLASS 1 - OTHER                     ":4,
	   "07 RENTALS - WALKUP APARTMENTS             ":5,
	   "08 RENTALS - ELEVATOR APARTMENTS           ":5,
	   "09 COOPS - WALKUP APARTMENTS               ":6,
	   "10 COOPS - ELEVATOR APARTMENTS             ":6,
	   "11 SPECIAL CONDO BILLING LOTS              ":2,
	   "11A CONDO-RENTALS                           ":2,
	   "12 CONDOS - WALKUP APARTMENTS              ":2,
	   "13 CONDOS - ELEVATOR APARTMENTS            ":2,
	   "14 RENTALS - 4-10 UNIT                     ":5,
	   "15 CONDOS - 2-10 UNIT RESIDENTIAL          ":2,
	   "16 CONDOS - 2-10 UNIT WITH COMMERCIAL UNIT ":2,
	   "17 CONDO COOPS                             ":2,
	   "18 TAX CLASS 3 - UNTILITY PROPERTIES       ":3,
	   "21 OFFICE BUILDINGS                        ":7,
	   "22 STORE BUILDINGS                         ":7,
	   "23 LOFT BUILDINGS                          ":7,
	   "25 LUXURY HOTELS                           ":7,
	   "26 OTHER HOTELS                            ":7,
	   "27 FACTORIES                               ":7,
	   "28 COMMERCIAL CONDOS                       ":7,
	   "29 COMMERCIAL GARAGES                      ":7,
	   "30 WAREHOUSES                              ":7,
	   "31 COMMERCIAL VACANT LAND                  ":7,
	   "32 HOSPITAL AND HEALTH FACILITIES          ":7,
	   "33 EDUCATIONAL FACILITIES                  ":3,
	   "34 THEATRES                                ":7,
	   "35 INDOOR PUBLIC AND CULTURAL FACILITIES   ":8,
	   "36 OUTDOOR RECREATIONAL FACILITIES         ":8,
	   "37 RELIGIOUS FACILITIES                    ":9,
	   "38 ASYLUMS AND HOMES                       ":8,
	   "39 TRANSPORTATION FACILITIES               ":3,
	   "40 SELECTED GOVERNMENTAL FACILITIES        ":3,
	   "41 TAX CLASS 4 - OTHER                     ":4,
	   "42 CONDO CULTURAL/MEDICAL/EDUCATIONAL/ETC  ":2,
	   "42 CONDO CULTURAL/MEDICAL/EDUCATIONAL/ETC  ":2,
	   "44 CONDO PARKING                           ":2,
	   "45 CONDO HOTELS                            ":2,
	   "46 CONDO STORE BUILDINGS                   ":2,
	   "47 CONDO NON-BUSINESS STORAGE              ":2,
	   "48 CONDO TERRACES/GARDENS/CABANAS          ":2,
	   "49 CONDO WAREHOUSES/FACTORY/INDUS          ":2,
       }

# 1 = Dewellings , 2 = Condos , 3 = Goverment , 4 = Other , 5 = Rentals, #
# 6 = Coops , 7 = Commercial , 8 = Livilyhood , 9 = Religious # 


X = []    # features
Y = []    # sale_price
with open('newnewdata.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue;
        
        row[2] = dic[row[2]] 

        X.append([ int(row[1]), row[2], int(row[3]), int(row[4]),
                   int(row[5]), int(row[6]), int(row[7]), 
                   int(row[8]), int(row[9]) ])
        Y.append(int(row[9]))

df = pd.DataFrame(X, columns=['borouch', 'building category','zipCode', 
							  'residental units', 'commercial units',
                              'land square', 'gross square', 'taxClass',
                              'sale price'])
df.to_csv("newnewnewdata.csv")        


data2 = pd.read_csv('newnewnewdata.csv')
correlation = data2.corr()
print(correlation)
fig, ax = plt.subplots(figsize=(9,9))
#ax.matshow(correlation)
cax = ax.matshow(correlation, interpolation='nearest')
fig.colorbar(cax)
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
#plt.show()

data2 = data2.drop([data2.columns[0], 'commercial units', 'land square'], axis=1)
data2.to_csv("ultdata.csv")

#regr = linear_model.LinearRegression()
#regr.fit(X, Y)

