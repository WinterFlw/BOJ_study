for i in range(int(input())):
    befad, aftad, adfee = map(int,input().split())
    if befad == aftad - adfee: print("does not matter")
    elif befad < aftad - adfee: print("advertise")
    else: print("do not advertise")