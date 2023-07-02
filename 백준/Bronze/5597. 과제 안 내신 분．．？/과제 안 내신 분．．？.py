task = []
for i in range(28):
    k = int(input())
    task.append(k)

for i in range(30):
    if (i + 1 in task) == 0:
        print(i+1)