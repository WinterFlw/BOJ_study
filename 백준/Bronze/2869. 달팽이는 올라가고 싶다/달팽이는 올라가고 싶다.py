A, B, C = map(int,input().split())
if (C-A)%(A-B) != 0:
    i = 2
else:
    i = 1
print((C-A)//(A-B)+i)