star = int(input())

for j in range(star):
    print(" " * (j),end="")
    print("*" * (2 *(star - j)-1))