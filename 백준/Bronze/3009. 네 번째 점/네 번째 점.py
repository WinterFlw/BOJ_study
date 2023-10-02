dot = []
for i in range(3):
    x, y= map(int,input().split())
    dot.append([x,y])

if dot[0][0] == dot[1][0]:
    x = dot[2][0]
elif dot[1][0] == dot[2][0]:
    x = dot[0][0]
elif dot[0][0] == dot[2][0]:
    x = dot[1][0]
if dot[0][1] == dot[1][1]:
    y = dot[2][1]
elif dot[1][1] == dot[2][1]:
    y = dot[0][1]
elif dot[0][1] == dot[2][1]:
    y = dot[1][1]

print(x,y)