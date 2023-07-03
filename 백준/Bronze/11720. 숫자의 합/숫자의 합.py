N = int(input())
S = input()
SUM = 0
for i in range(N):
    SUM += int(S[i-1])
print(SUM)