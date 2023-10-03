for i in range(int(input())):
    str = input()
    score = 0
    combo = 0
    for j in str:
        if j == "O":
            combo += 1
            score += combo
        elif j == "X":
            combo = 0
    print(score)