data = [
           [0,1,1],
           [0,0,0],
           [0,0,0],
           [0,0,1],
           [0,1,0],
           [0,1,0],
           [1,1,1],
           [1,1,0],
           [0,1,1],
           [0,0,0],
           [0,1,0],
           [0,1,0],
           [0,1,1],
           [0,0,0],
           [0,1,0],
           [0,1,0],
           [0,1,1],
           [1,1,0]
           ]

x = [i[0] for i in data]
y = [i[1] for i in data]
label = [i[2] for i in data]
import matplotlib.pyplot as plt
plt.scatter(x,y,c=label)
plt.show()

import math
def dist(testRow, trainRow):
    d = 0.0
    for i in range(0,len(trainRow)-1):
        d += (testRow[i]-trainRow[i])**2
    return math.sqrt(d)

print("Enter the point to classify")
test = [int(i) for i in input().split()]
print("Enter the k")
k = int(input())

plt.scatter(x,y,c=label)
plt.scatter(test[0],test[1],c='red')
plt.show()

d = list()
for row in data:
    temp = dist(test,row)
    d.append((temp,row))
d.sort(key = lambda x: x[0]) 
knn = list()
print("K nearest neighbours")
for i in range(k):
    print("point: ("+str(d[i][1][0])+", "+str(d[i][1][1])+") with distance: "+str(d[i][0])+" and class: "+str(d[i][1][-1]))
    knn.append(d[i][1])

labels = [label[-1] for label in knn]
pred = max(set(labels), key=labels.count)
print('prediction: '+str(pred))