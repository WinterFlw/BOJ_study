N = int(input())
players = [100,100]
for i in range(N):
    A, B = map(int,input().split())
    if A < B:
        players[0] -= B 
    elif A > B:
        players[1] -= A
        
for i in players:
    print(i)