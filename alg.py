from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import csv
from sklearn import linear_model

X = []    # features
Y = []    # sale_price
with open('newnewdata.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue;
        
        row[2] = dic[row[2]] 

        X.append([ int(row[1]), row[2], int(row[3]), int(row[4]),
                   int(row[5]), int(row[6]), int(row[7]), int(row[8]) ])
        Y.append(int(row[9]))

# X, Y need to be converted to array ???

regr = linear_model.LinearRegression()
regr.fit(X, Y)

