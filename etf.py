
#part2 etf
#build the buy and sell signal model based on macd theory
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt

data = DataFrame(pd.read_csv('CVX.csv'))#read Data
price = DataFrame(data.Close)
ema = DataFrame(np.zeros((503,1)))#creat a new colums with 0
data.insert(7,"ema",ema)#combine data with ema
ema = DataFrame(data.ema)

# EMA formula
def get_EMA(data,N):
    for i in range(len(data)):
        if i==0:
            data.ix[i,"ema"] = price.ix[i,"Close"]
        if i>0:
            data.ix[i,"ema"] = (2*price.ix[i,"Close"]+(N-1)*data.ix[i-1,"ema"])/(N+1)

    return data #return a data with ema

short = get_EMA(data,12)
short = DataFrame(short["ema"])
long = get_EMA(data,26)
long = DataFrame(long["ema"])
diff = short - long
data.insert(8,"diff",diff)
#macd formula
def get_MACD(data,M):
    for i in range(len(data)):
        if i==0:
            data.ix[i,'dea']=diff.ix[i,'ema']
        if i>0:
            data.ix[i,'dea']=(2*diff.ix[i,'ema']+(M-1)*data.ix[i-1,'dea'])/(M+1)
    data['macd']=2*(data['diff']-data['dea'])
    return data
get_MACD(data,9)
macd = DataFrame(data.macd)

#build a new colums signal
signal = DataFrame(np.zeros((503,1)))
data.insert(11,"signal",signal)

def signal1(data):#1-9 signal equal to macd
    for i in range(len(data)):
        if i<9:
            data.ix[i,"signal"]=macd.ix[i,"macd"]
    return data

signal1(data)
mydata = signal1(data)#new data named mydata

length = len(mydata)

for i in range(length-9):#mean of every 9 macd(the defination of signaline)
    sum = 0
    j = i
    while j<i+9:
        sum += mydata.ix[j, "macd"]
        j += 1
    sum /= 9
    mydata.ix[j, "signal"] = sum

signal = DataFrame(mydata.signal)#get signal data
plt.plot(signal)#plot macd with signal line
plt.plot(macd)


dif = DataFrame(np.zeros((503,1)))# to give a buy and sell signal
for i in range(len(mydata)):#
    if mydata.ix[i,"macd"]>mydata.ix[i,"signal"]:
        mydata.ix[i,"dif"]=1
    else:
        mydata.ix[i,"dif"]= -1


for i in range(len(mydata)):
    if mydata.ix[i+1,"dif"]>mydata.ix[i,"dif"]:
        mydata.ix[i,"buysell"]="buy"
    else:
        mydata.ix[i,"buysell"]="sell"

#end
