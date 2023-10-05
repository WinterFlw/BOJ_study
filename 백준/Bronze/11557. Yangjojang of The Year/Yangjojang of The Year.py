for i in range(int(input())):
    max_alcohol = [None, 0]
    for j in range(int(input())):
        univ, alchole = map(str, input().split())
        if int(max_alcohol[1]) < int(alchole):
            max_alcohol[0] = univ
            max_alcohol[1] = alchole
    print(max_alcohol[0])