import numpy as np
import math

#(1)
arr1 = np.zeros((3, 4), dtype = np.float64)
print("(1)")
print(arr1)

#(2)
data = np.random.randn(100)
count = 0.
for i in range(0, 100) :
    if data[i] < 0.4 :
        count += 1
ratio = count / 100
print("(2)")
print("ratio is: ",ratio)

#(3)
data2 = np.random.uniform(-10, 10, (7,7))
newData = np.zeros((7,7))
for i in range(0, 7):
    for j in range(0, 7):
        if data2[i][j] == int(data2[i][j]):
            newData[i][j] = data2[i][j];
            continue;
        if data2[i][j] < 0:
            newData[i][j] = int(data2[i][j])-1
        else:
            newData[i][j] = int(data2[i][j])+1
print("(3)")
print(newData)

#(4)
# standard distribution N(1, 2)  mean-variance
data3 = math.sqrt(2)*np.random.randn(1000) + 1
summ = sum(data3)
mean = summ/1000
print("(4)")
print("mean is: ", mean)

variance = 0.0
for i in range(0, 1000): 
    variance += (data3[i] - mean)**2
variance /= 1000
print("variance is: ", variance)
sd = math.sqrt(variance)   # standard derivation

skewness = 0.0
for i in range(0, 1000): 
    skewness += ((data3[i]-mean)/sd)**3
skewness /= 1000
print("skewness is: ", skewness)

kurtosis = 0.0
for i in range(0, 1000): 
    kurtosis += ((data3[i]-mean)/sd)**4
kurtosis /= 1000
print("kurtosis is: ", kurtosis)

#(5)
data4 = np.random.randint(100, size=100)  #high = 100
max = min = data4[0]      
for i in range(1,100):
    if data4[i] > max:
        max = data4[i]
    if data4[i] < min:
        min = data4[i]
print("(5)")
print("max is:", max, "  min is: ", min)


#(6)
x = np.array([0, 1, 2, 3])
y = np.array([-2.4, 0.5, 1.9, 4.1])
# y = mx + c = A * x
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=-1)[0]
print("(6)")
print("coefficients for y=mx+c are: ", m, c)

