total = int(input())
items = int(input())
cost_sum = 0
for i in range(items):
    cost, EA = map(int,input().split())
    cost_sum += cost * EA

if cost_sum == total:
    print("Yes")
else:
    print("No")