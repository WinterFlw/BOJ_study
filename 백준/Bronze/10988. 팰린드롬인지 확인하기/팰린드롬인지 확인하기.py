p = input()
if len(p) == 1:
    print("1")

for i in range(len(p)//2):
    if p[i] != p[-1-i]:
        print("0")
        break
    if i == ((len(p)//2) -1):
        print("1")