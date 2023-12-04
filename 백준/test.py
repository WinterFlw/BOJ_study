y,x,inven = map(int, input().split())

class MineCraft:
    def __init__(self, y, x, inven):
        self.y = y
        self.x = x
        self.inven = inven
        self.UsedTime = 0
        self.mapdata = self.arrMake()

    def arrMake(self):
        data = []
        for i in range(y):
            data.append([])
            hang = map(int, input().split())
            hang = list(hang)
            for j in range(x):
                data[i].append(hang[j])
        print("\n",data)
        return data

    def realMax(self):
        rMax = 0
        for i in range(y):
            if rMax < max(self.mapdata[i]):
                rMax = max(self.mapdata[i])
        return rMax
    
    def realMin(self):
        rMin = 0
        for i in range(y):
            if rMin < min(self.mapdata[i]):
                rMin = min(self.mapdata[i])
        return rMin

    def counter(self):
        maxs, mins = 0, 0
        for i in range(y):
            for j in range(x):
                if self.mapdata[i][j] == self.realMax():
                    maxs += 1
                if self.mapdata[i][j] == self.realMin():
                    mins += 1
        return maxs, mins
    
    def dig(self):
        maxs = self.realMax()
        for i in range(y):
            for j in range(x):
                if self.mapdata[i][j] == maxs:
                    self.mapdata[i][j] -= 1
                    self.UsedTime += 2
                    self.inven += 1
                    print("Dig:",self.UsedTime, self.inven)
        #최대값 다 돌면서 각각 mapdata[i][j]-=1, UsedTime += 2

    def inv(self):
        mins = self.realMin()
        for i in range(y):
            for j in range(x):
                if self.mapdata[i][j] == mins:
                    self.mapdata[i][j] += 1
                    self.UsedTime += 1
                    self.inven -= 1
                    print("Inv:",self.UsedTime, self.inven)
        #최소값 다 돌면서 각각 mapdata[i][j]+=1, UsedTime += 1

    def settler(self):
        while self.realMax() != self.realMin():
            maxs, mins = self.counter()
            if mins > self.inven :
                self.dig()
            else:
                if maxs < mins * 2:
                    self.dig()
                else:
                    self.inv()

    def __str__(self):
        return f"{self.UsedTime} {self.mapdata[0][0]}"

mine = MineCraft(y,x,inven)
mine.settler()
print(mine)