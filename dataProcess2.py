'''
Data Processing II: some features are text data, but very important; some features
are not explicitly relevant or not to sale_price 
(1) Convert text data to numerical data, or normaliza some features with large number
(2) Eliminate unrelated features by correlation analysis
'''
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import csv


# convert text data to numerical data by dictionary (hashmap) 
# 1 = Dewellings , 2 = Condos , 3 = Goverment , 4 = Other , 5 = Rentals, #
# 6 = Coops , 7 = Commercial , 8 = Livilyhood , 9 = Religious # 
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

# 1 = midtown, 2 = downtown, 3 = east and west uptown(near central park), 
# 4 = uptown, 5 = bronx, 6 = brooklyn, 7 = queens
dic2 = {"10001":1,
	   "10010":1,
	   "10011":1,
	   "10022":1,
	   "10016":1,
	   "10036":1,
	   "10017":1,
	   "10167":1,
	   "10018":1,
	   "10019":1,
	   "10002":2,
	   "10003":2,
	   "10004":2,
	   "10005":2,
	   "10006":2,
	   "10007":2,
	   "10008":2,
	   "10009":2,
	   "10012":2,
	   "10013":2,
	   "10014":2,
	   "10038":2,
	   "10021":3,
	   "10023":3,
	   "10024":3,
	   "10025":3,
	   "10028":3,
	   "10029":3,
	   "10065":3,
	   "10075":3,
	   "10128":3,
	   "10026":4,
	   "10027":4,
	   "10035":4,
	   "10037":4,
	   "10030":4,
	   "10031":4,
	   "10039":4,
	   "10032":4,
	   "10033":4,
	   "10034":4,
	   "10040":4,
	   "10044":4
	   }
for i in range(10200, 11695):
    if i < 10476:
        dic2[str(i)] = 5
    elif i < 11250:
        dic2[str(i)] = 6
    else:
        dic2[str(i)] = 7


# Read in data, storing string as int 
X = []    # features and label
with open('newnewdata.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue;
        row[2] = dic[row[2]] 
        row[5] = dic2[row[5]]
        X.append([ int(row[1]), row[2], int(row[3]), int(row[4]),
                   row[5], int(row[6]), int(row[7]), int(row[8]), 
                   int(row[9]), int(row[10]), int(row[11]), int(row[12]) ])


#Implement correlation analysis to eleminate some features unrelated to sale_price
df = pd.DataFrame(X, columns=['borouch', 'building category', 'block', 'lot',
							'zipCode', 'residental units', 'commercial units',
                              'land square', 'gross square', 'year built','taxClass',
                              'sale price'])       
correlation = df.corr()
print(correlation)
fig, ax = plt.subplots(figsize=(12,12))
cax = ax.matshow(correlation, interpolation='nearest')
fig.colorbar(cax)
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.show()


# drop some features with low correlation value
df = df.drop(['lot', 'commercial units', 'land square', 'year built'], axis=1)
# drop one of the features that is highly relevant to each other
df = df.drop(['building category'], axis=1)
# 'building class' is almost totally dependent to 'taxClass'

df.to_csv("newnewnewdata.csv")




