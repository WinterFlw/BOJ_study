star = int(input())

for i in range(star):
    print(" " * (star -1 -i),end="")
    print("*" * (2 * (i + 1)-1))
    
for j in range(star - 1):
    print(" " * (j + 1),end="")
    print("*" * (2 *(star - 1 - j)-1))