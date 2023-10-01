numA, numB = 0, 0
len = int(input())
string = str(input())

for i in string:
    if i == "A": numA += 1
    elif i == "B": numB += 1
if numA == numB: print("Tie")
else: print("A" if numA > numB else "B")