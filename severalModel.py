import numpy as np
import csv
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

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

'''
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
print("Linear Accuracy: ", regr.score(x_test, y_test))

regr3 = MLPRegressor()  # not converge sometimes
regr3.fit(x_train, y_train)
print("MLP Accuracy: ", regr3.score(x_test, y_test))
'''

<<<<<<< HEAD
# ensemble learning: average the outputs of many decision trees
regr2 = RandomForestRegressor()
=======
# Ensemble learning: average the outputs of many decision trees
# For every decision tree, classify every attribute into several categories,
# then for the same category, average the target values as output 
regr2 = RandomForestRegressor(max_depth=2, random_state=0,
                              n_estimators=100)
>>>>>>> e2c828152ef1909f5e7c4b313799fced95b71738
'''
regr2.fit(x_train, y_train)
print("RF Accuracy: ", regr2.score(x_test, y_test))


regr3 = MLPRegressor()
regr3.fit(x_train, y_train)
print("MLP Accuracy: ", regr3.score(x_test, y_test))
'''
<<<<<<< HEAD

param_grid = {'n_estimators': [10,20,30,40,50,60,70,80,90,100],
              'max_depth': [2,3,4,5],
              }
gs = GridSearchCV(regr2, param_grid, cv=5) # 20 folds cross-validation
gs.fit(X,Y)

maxMean = 0
param = {}
for ele in gs.grid_scores_:
    if ele[1] > maxMean:
        maxMean = ele[1]
        param = ele[0]
print(maxMean, param)

=======
param_grid = {'n_estimators': [10,20,30,40,50,60,70,80,90,100],
              'max_depth': [2:3:4:5],
              }
>>>>>>> e2c828152ef1909f5e7c4b313799fced95b71738

maxMean = 0
param = {}
for ele in gs.grid_scores_:
    if ele[1] > maxMean:
        maxMean = ele[1]
        param = ele[0]
print(maxMean, param)


#print(cross_val_score(regr, X, Y, cv=5))
#print(cross_val_score(regr2, X, Y, cv=5))
#print(cross_val_score(regr3, X, Y, cv=5))
