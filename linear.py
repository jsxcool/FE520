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
regr.fit(X, Y)
print(regr.score(X, Y))  # 0.6714874629993289


# draw scatter between predicted and real 
y_pred = regr.predict(X)
plt.scatter(Y, y_pred)
y_arr = np.array(Y)
plt.plot([y_arr.min(), y_arr.max()], [y_arr.min(), y_arr.max()], color='red', lw=2)
plt.xlabel('Real sale_price $')
plt.ylabel('Predicted sale_price $')
plt.title('Predict NYC House Price by linear regression')
plt.xlim(0, 5000000)
plt.ylim(0, 5000000)
plt.show()


