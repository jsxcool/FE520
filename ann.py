import numpy as np
import csv
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def scoreOneLayer(n):
	regr = MLPRegressor(hidden_layer_sizes=(n))
	regr.fit(X, Y)
	return regr.score(x_test, y_test)

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
regr = MLPRegressor(hidden_layer_sizes=(50))
param_grid = {'activation': ['logistic', 'tanh', 'relu'],
              'solver': ['sgd', 'adam'],
              }
gs = GridSearchCV(regr, param_grid, cv=5) # 5 folds cross-validation
gs.fit(X,Y)

maxMean = -10000
param = {}
for ele in gs.grid_scores_:
    if ele[1] > maxMean:
        maxMean = ele[1]
        param = ele[0]
print(maxMean, param)
# best parameter {'activation': 'relu', 'solver': 'adam'}, the same as default 
# R^2 covirance: 0.14600261914616436
'''

units = np.arange(20,150,5)
score = []
for i in units:
	score.append(scoreOneLayer(i))

plt.plot(units, score, marker='o')
plt.xlabel('n hidden units')
plt.ylabel('R^2 variance')
plt.title('One hidden layer ANN')
plt.grid(True)
plt.show()

