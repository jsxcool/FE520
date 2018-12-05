import numpy as np
import csv
from sklearn import linear_model
from sklearn.model_selection import train_test_split

X = []    # features
Y = []    # sale_price
with open('ultdata.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue;

        X.append([ int(row[1]), int(row[2]), int(row[3]), int(row[4]),
                   int(row[5]), int(row[6])])
        Y.append(int(row[7]))


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
print("Accuracy: ", regr.score(x_test, y_test))
