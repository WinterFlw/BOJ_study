atime = 300
btime = 60
ctime = 10

A, B, C = 0, 0, 0
t = int(input())

while t > 0:
    if t < ctime:
        C = -1
        break
    else :   
        if t >= atime:
            t -= atime
            A += 1
        elif t >= btime:
            t -= btime
            B += 1
        elif t >= ctime:
            t -= ctime
            C += 1
    
if C != -1: print(A,B,C)
else: print(C)