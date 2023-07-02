max_num = 0
max_where = 0
for i in range(9):
    n = int(input())
    if n > max_num:
        max_num = n
        max_where = i+1
print(max_num)
print(max_where)