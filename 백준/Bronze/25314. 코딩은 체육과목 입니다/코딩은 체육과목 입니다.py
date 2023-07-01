N = int(input())
long_num = 0
if N % 4 == 0 :
    long_num = N // 4
else:
    long_num = N // 4 + 1
    
for i in range (long_num):
    print("long ", end="")
print("int")