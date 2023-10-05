lens = int(input())
nums = list(map(int,input().split()))
max_num = max(nums)
sums = 0
for i in nums:
    sums += i/max_num*100
print(sums / lens)