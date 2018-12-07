from pandas import DataFrame
import pandas as pd
import numpy as np
import csv

X = []
#verylow  low     median  high      veryhigh 
#20w~40w 40w~65w 65w~100w 100w~200w >200w
count1 = count2 = count3 = count4 = count5 = 0
with open("ultdata.csv") as f:
	reader = csv.reader(f)
	for row in reader:
		if reader.line_num == 1:
			continue
		if 200000<=int(row[7])<=400000:
			count1 += 1
		if count1 > 2000:
			continue
		if 400000<int(row[7])<=650000:
			count2 += 1
			if count2 > 2000:
				continue
		if 650000<int(row[7])<=1000000:
			count3 += 1
			if count3 > 2000:
				continue
		if 1000000<int(row[7])<=2000000:
			count4 += 1
			if count4 > 2000:
				continue
		if int(row[7])>2000000:
			count5 += 1
			if count5 > 2000:
				continue
		X.append([ int(row[1]), int(row[2]), int(row[3]), int(row[4]),			
               	   int(row[5]), int(row[6]), int(row[7])])

df = pd.DataFrame(X, columns=['borouch', 'building category','zipCode', 
							  'residental units', 'gross square', 'taxClass',
                              'sale price'])
df.to_csv("ourdata.csv")        


        
