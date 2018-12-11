import numpy as np
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

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


# ensemble learning: average the outputs of many decision trees
regr2 = RandomForestRegressor()
param_grid = {'n_estimators': [1,2,3,4,5,10,20,40],
              'max_depth': [2,3,4,5,6],
              }
gs = GridSearchCV(regr2, param_grid, cv=5) # 5 folds cross-validation
gs.fit(X,Y)

'''
maxMean = -10000
param = {}
for ele in gs.grid_scores_:
    if ele[1] > maxMean:
        maxMean = ele[1]
        param = ele[0]
print(maxMean, param)
# best parameter: {'max_depth': 3, 'n_estimators': 5}
# R^2 varience: -0.1781369139974362

'''
# draw scatter between predicted and real with best parameter
regr = RandomForestRegressor(max_depth=3, n_estimators=5)
y_pred = cross_val_predict(regr, X, Y, cv=5)
plt.scatter(Y, y_pred)
y_arr = np.array(Y)
plt.plot([y_arr.min(), y_arr.max()], [y_arr.min(), y_arr.max()], color='red', lw=2)
plt.xlabel('Real sale_price $')
plt.ylabel('Predicted sale_price $')
plt.title('Predict NYC House Price by RF')
plt.xlim(0, 5000000)
plt.ylim(0, 5000000)
plt.show()



