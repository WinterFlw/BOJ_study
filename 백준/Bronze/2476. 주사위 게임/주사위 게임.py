price = []
for i in range(int(input())):
    a, b, c = map(int,input().split())
    if a == b == c: price.append(10000 + a * 1000)
    elif a == b or b == c or a == c:
        if a == b: price.append(1000 + a * 100)
        elif b == c: price.append(1000 + b * 100)
        elif a == c: price.append(1000 + c * 100)
    else: price.append(max(a,b,c)*100)
print(max(price))
