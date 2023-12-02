import numpy as np

UsedTime = 0
y,x,inven = map(int, input().split())

def counter(mapdata):
    maxs, mins = 0, 0
    for i in range(y):
        for j in range(x):
            if mapdata[i][j] == np.max(mapdata):
                maxs += 1
            if mapdata[i][j] == np.min(mapdata):
                mins += 1
    return maxs, mins

def dig(mapdata):
    max = np.max(mapdata)
    for i in range(y):
        for j in range(x):
            if mapdata[i][j] == max:
                mapdata[i][j] -= 1
                UsedTime += 2
                inven += 1
    #최대값 다 돌면서 각각 mapdata[i][j]-=1, UsedTime += 2

def inv(mapdata):
    min = np.min(mapdata)
    for i in range(y):
        for j in range(x):
            if mapdata[i][j] == min:
                mapdata[i][j] += 1
                UsedTime -= 2
                inven -= 1
    #최소값 다 돌면서 각각 mapdata[i][j]+=1, UsedTime += 1

mapdata = np.zeros((y,x), dtype=int)

for i in range(y):
    hang = map(int, input().split())
    hang = list(hang)
    for j in range(x):
        mapdata[i][j] = hang[j]

while np.max(mapdata) != np.min(mapdata):
    maxs, mins = counter(mapdata)
    if mins > inven :
        dig(mapdata)
    else:
        if maxs < mins * 2:
            dig(mapdata)
        else:
            inv(mapdata)

print(UsedTime, mapdata[0][0])