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
# Do 1~9 have a sequence ? eg, from cheap - expensive 
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
        "10044": 4,
        "10451": 5,
	   "10452":5,
	   "10453":5,
	   "10454":5,
	   "10455":5,
	   "10456":5,
	   "10457":5,
	   "10458":5,
	   "10459":5,
	   "10460":5,
	   "10461":5,
	   "10462":5,
	   "10463":5,
	   "10464":5,
	   "10465":5,
	   "10466":5,
	   "10467":5,
	   "10468":5,
	   "10469":5,
	   "10470":5,
	   "10471":5,
	   "10472":5,
	   "10473":5,
	   "10474":5,
	   "10475":5,
	   "10803":5,
	   "11102":6,
	   "11103":6,
	   "11104":6,
	   "11105":6,
	   "11201":6,
	   "11102":6,
	   "11202":6,
	   "11203":6,
	   "11204":6,
	   "11205":6,
	   "11206":6,
	   "11207":6,
	   "11208":6,
	   "11209":6,
	   "11210":6,
	   "11211":6,
	   "11212":6,
	   "11213":6,
	   "11214":6,
	   "11215":6,
	   "11216":6,
	   "11217":6,
	   "11218":6,
	   "11219":6,
	   "11220":6,
	   "11221":6,
	   "11222":6,
	   "11223":6,
	   "11224":6,
	   "11225":6,
	   "11226":6,
	   "11227":6,
	   "11228":6,
	   "11229":6,
	   "11230":6,
	   "11231":6,
	   "11232":6,
	   "11233":6,
	   "11234":6,
	   "11235":6,
	   "11236":6,
	   "11237":6,
	   "11238":6,
	   "11249":6,
	   "11369":6,
	   "11370":6,
	   "11371":6,
	   "11372":6,
	   "11373":6,
	   "11374":6,
	   "11375":6,
	   "11376":6,
	   "11377":6,
	   "11378":6,
	   "11420":6,
	   "11001":7,
	   "11004":7,
	   "11362":7,
	   "11363":7,
	   "11426":7,
	   "11354":7,
	   "11355":7,
	   "11356":7,
	   "11357":7,
	   "11358":7,
	   "11359":7,
	   "11360":7,
	   "11361":7,
	   "11364":7,
	   "11365":7,
	   "11366":7,
	   "11367":7,
	   "11368":7,
	   "11411":7,
	   "11691":7,
	   "11692":7,
	   "11693":7,
	   "11694":7,
    }


# Read in data, storing string as int 
X = []    # features and label
with open('newnewdata.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue;
        row[2] = dic[row[2]]
        row[3] = dic2[row[3]]
        X.append([ int(row[1]), row[2], row[3], int(row[4]),
                   int(row[5]), int(row[6]), int(row[7]), 
                   int(row[8]), int(row[9]) ])


df = pd.DataFrame(X, columns=['borouch', 'building category','zipCode', 
							  'residental units', 'commercial units',
                              'land square', 'gross square', 'taxClass',
                              'sale price'])
df.to_csv("newnewnewdata.csv")        



#Implement correlation analysis to eleminate some features unrelated to sale_price
data2 = pd.read_csv('newnewnewdata.csv')
data2 = data2.drop([data2.columns[0]], axis=1 )
correlation = data2.corr()
print(correlation)
fig, ax = plt.subplots(figsize=(9,9))
cax = ax.matshow(correlation, interpolation='nearest')
fig.colorbar(cax)
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.show()


# drop two features with low correlation value
data2 = data2.drop(['commercial units', 'land square'], axis=1)

# delete 'building catagory', because it's almost 100% relevent to 'tax_class'
data2 = data2.drop(['building category'], axis=1)

data2.to_csv("ultdata.csv")

