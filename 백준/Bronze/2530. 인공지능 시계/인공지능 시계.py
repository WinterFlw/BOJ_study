HOUR = 24
MINUTE = 60
SECOND = 60

hour, minute, second = map(int, input().split())
time = int(input())

temp = second + time
second = temp % SECOND
temp = temp // SECOND

temp += minute

minute = temp % MINUTE
temp = temp // MINUTE

temp += hour

hour = temp % HOUR

print(hour, minute, second)