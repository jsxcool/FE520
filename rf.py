# Ensemble learning: average the outputs of many decision trees
# For every decision tree, classify every attribute into several categories,
# then for the same category, average the target value as output
import numpy as np
import csv
from sklearn.ensemble import RandomForestRegressor
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

# gridSearch to get the best parameter
def myGridSearch(estimator, treeDepth):
	maxScore = -10000
	bestI = 0
	bestJ = 0
	for i in range(len(estimator)):
		for j in range(len(treeDepth)):
			regr = RandomForestRegressor(n_estimators=estimator[i], max_depth=treeDepth[j])
			regr.fit(X, Y)
			s = regr.score(X, Y)
			if s > maxScore:
				maxScore = s
				bestI = estimator[i]
				bestJ = treeDepth[j]
	print('maxScore: ', maxScore, ' estimator: ', bestI, ' max_depth: ', bestJ) 

n_estimators = [1,2,3,4,5,10,20,30,40,50]
max_depth = [2,3,4,5,6]
myGridSearch(n_estimators, max_depth)           


# draw scatter between predicted and real with best parameter
regr = RandomForestRegressor(n_estimators=3, max_depth=6)
regr.fit(X, Y)
print(regr.score(X, Y)) #0.868
y_pred = regr.predict(X) 
plt.scatter(Y, y_pred)
y_arr = np.array(Y)
plt.plot([y_arr.min(), y_arr.max()], [y_arr.min(), y_arr.max()], color='red', lw=2)
plt.xlabel('Real sale_price $')
plt.ylabel('Predicted sale_price $')
plt.title('Predict NYC House Price by RF')
plt.xlim(0, 5000000)
plt.ylim(0, 5000000)
plt.show()


