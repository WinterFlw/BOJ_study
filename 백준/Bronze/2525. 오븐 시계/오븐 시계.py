H, M = map(int,input().split())
P = int(input())
M += P
if M >= 60:
    while (M >= 60):
        M -= 60
        H += 1
    if H >= 24:
        H -= 24
        print(H,M)
    else:
        print(H,M)
else:
    print(H,M)