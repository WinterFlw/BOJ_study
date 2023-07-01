N = int(input())

if N % 2 == 1:
    print(int(((N-1) / 2) * (N + 1) +((N+1) / 2)))
else:
    print(int((N / 2) * (N + 1)))