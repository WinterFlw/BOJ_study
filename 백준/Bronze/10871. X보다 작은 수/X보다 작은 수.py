N, small = map(int,input().split())
nums = list(map(int,input().split()))
small_list = []
for i in range(N):
    if nums[i] < small:
        small_list.append(nums[i])

for j in range(len(small_list)):
    if j != len(small_list) -1:
        print(small_list[j],end=" ")
    else:
        print(small_list[j])