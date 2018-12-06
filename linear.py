import numpy as np
import csv
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# every time, different accuracy, depending on training dataset and test dataset
# data normalization, same quantity, every catagory

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
print("Linear Accuracy: ", regr.score(x_test, y_test))

regr2 = RandomForestRegressor(max_depth=2, random_state=0,
                              n_estimators=100)
regr2.fit(x_train, y_train)
print("RF Accuracy: ", regr2.score(x_test, y_test))
