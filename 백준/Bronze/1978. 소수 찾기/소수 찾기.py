import math

num = int(input())
num_list = list(map(int, input().split()))
prime_num = 0

def is_prime(number):
    for i in range (2, (int(math.sqrt(number) + 1))):
    	if number % i == 0:
        	return False
    return True

for i in range(num):
    if num_list[i] > 1:
        if num_list[i] == 2:
            prime_num += 1
        elif num_list[i] % 2 == 1:
            prime_num += int(is_prime(num_list[i]))
                
print(prime_num)