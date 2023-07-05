N,M = map(int,input().split())
arr = []
for n in range(N):
    arr.append(n+1)

for m in range(M):
    i,j = map(int,input().split())
    temp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = temp
    
#출력 함수
for array in range(len(arr)):
    if array == len(arr) - 1:
        print(arr[array])
    else:
        print(arr[array],end=" ")
