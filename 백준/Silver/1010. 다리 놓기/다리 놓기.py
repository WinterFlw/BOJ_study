def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def comb(r,n):
    #n!/r!(n-r)!
    print(int((factorial(n)/(factorial(r)*factorial(n-r)))))
    
X = int(input())
for i in range(X):
    A, B = map(int,input().split())
    comb(A,B)
