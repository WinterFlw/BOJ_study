a = int(input())
nums = set()

for i in range(a):
    nums.add(int(input()))

nums_sort = sorted(nums)

for j in nums_sort:
    print(j)