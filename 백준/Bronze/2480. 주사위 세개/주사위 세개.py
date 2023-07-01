A, B, C = map(int,input().split())
rst= []
for i in range(0,6,1):
    rst.append(0)
    if A == (i+1):
        rst[i]+=1
    if B == (i+1):
        rst[i]+=1
    if C == (i+1):
        rst[i]+=1

count = 1      #같은 갯수
count_num = 0  #같은 갯수가 가장 많은 눈의 수
max_num = 0    #나온 눈 중 가장 높은 수

for i in range(0,6,1):
    if count < rst[i]:
        count = rst[i]
        count_num = i+1
    if rst[i] != 0:
        max_num = i+1
if count == 3:
    print(10000 + count_num * 1000)
elif count == 2:
    print(1000 + count_num * 100)
elif count == 1:
    print(max_num * 100)