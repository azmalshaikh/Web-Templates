dataset = [
           [0,1,0,1],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,1],
           [0,1,0,0],
           [0,1,0,0],
           [1,1,1,1],
           [1,1,1,0],
           [0,1,0,1],
           [0,0,0,0],
           [0,1,0,0],
           [0,1,1,0],
           [0,1,0,1],
           [0,0,0,0],
           [0,1,0,0],
           [0,1,0,0],
           [0,1,0,1],
           [1,1,1,0]
           ]

mp = dict()
for i in range(len(dataset)):
    row = dataset[i]
    y = row[-1]
    if (y not in mp):
        mp[y] = list()
    mp[y].append(row)
for label in mp:
    print(label)
    for row in mp[label]:
        print(row)

test = [1,1,0]

probYes = 1

count = 0
total = 0
for row in dataset:
    if(row[-1] == 1):
        count+=1
    total+=1
print("Total yes: "+str(count)+" / "+str(total))
probYes *= count/total
for i in range(len(test)):
    count = 0
    total = 0
    for row in mp[1]:
        if(test[i] == row[i]):
            count += 1
        total += 1
    print('for feature '+str(i+1))
    print(str(count)+" / "+str(total))
    probYes *= count/total

probNo = 1
count = 0
total = 0
for row in dataset:
    if(row[-1] == 0):
        count+=1
    total+=1
probNo *= count/total
print("Total no: "+str(count)+" / "+str(total))
for i in range(len(test)):
    count = 0
    total = 0
    for row in mp[0]:
        if(test[i] == row[i]):
            count += 1
        total += 1
    print('for feature '+str(i+1))
    print(str(count)+" / "+str(total))
    probNo *= count/total

print(probYes)
print(probNo)

prob = probNo/(probYes+probNo)
prob1 = probYes/(probYes+probNo)
print("Probability of being non-mammal: "+str(prob*100)+"%")
print("Probability of being mammal: "+str(prob1*100)+"%")