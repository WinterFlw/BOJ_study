plate = str(input())
hight = 0
for i in range(len(plate)):
    if i == 0:
        hight += 10
    else:
        if plate[i-1] == plate[i]:
            hight += 5
        else: hight += 10
print(hight)