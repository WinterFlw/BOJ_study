N,M = map(int,input().split())
arr = []
for n in range(N):
    arr.append(0)

for m in range(M):
    i,j,k = map(int,input().split())
    for ij in range(i-1,j,1):
        del arr[ij]
        arr.insert(ij,k)
    
for array in range(len(arr)):
    if array == len(arr) - 1:
        print(arr[array])
    else:
        print(arr[array],end=" ")