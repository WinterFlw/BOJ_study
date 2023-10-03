n = int(input())
temp = 2
while n != 1:
    if n % temp == 0:
        n = n//temp
        print(temp)
        temp = 2
    else:
        temp += 1