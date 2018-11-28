import point
import generator
gen = generator.LCG(1,12496158,16166518,2000000)     
ls = gen.listRandom(20000000)
length = len(ls)
for i in range(5000000, 12500000):
    ls[i] = -ls[i]
for i in range(15000000, 17500000):
    ls[i] = -ls[i]
    
gen2 = generator.SCG(2,12496158,161665188,20000000)     
ls2 = gen.listRandom(20000000)
length2 = len(ls2)
for i in range(5000000, 12500000):
    ls2[i] = -ls2[i]
for i in range(15000000, 17500000):
    ls2[i] = -ls2[i]

lsPoint = []
left = 0
right = length - 1
while left < right : 
    lsPoint.append(point.Point(ls[left], ls[right]))
    left += 1
    right -= 1
    
lsPoint2 = []
left2 = 0
right2 = length2 - 1
while left2 < right2 : 
    lsPoint.append(point.Point(ls2[left], ls2[right]))
    left2 += 1
    right2 -= 1

count2 = 0
for ele in lsPoint:
    if ele.distance() < 1:
        count2 += 1  
        
count = 0
for ele in lsPoint:
    if ele.distance() < 1:
        count += 1  

print("ratio for LCG: ", 2*count/length)
print("ratio for SCG: ", 2*count2/length2)
