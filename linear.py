import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict


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


regr = linear_model.LinearRegression()

'''
# n-folds cross-validation
n_fold = np.arange(5, 100)
score = [] 
for i in n_fold:
	 score.append(cross_val_score(regr, X, Y, cv=i).mean())
plt.plot(n_fold, score)
plt.xlabel('n-folds') 
plt.ylabel('Variance score')
plt.grid(True)
plt.show()
'''


# draw scatter between predicted and real with best n-folds
y_pred = cross_val_predict(regr, X, Y, cv=5)
plt.scatter(Y, y_pred)
y_arr = np.array(Y)
plt.plot([y_arr.min(), y_arr.max()], [y_arr.min(), y_arr.max()], color='red', lw=2)
plt.xlabel('Real sale_price $')
plt.ylabel('Predicted sale_price $')
plt.title('Predict NYC House Price by Cross-Validation')
plt.xlim(0, 5000000)
plt.ylim(0, 5000000)
plt.show()


