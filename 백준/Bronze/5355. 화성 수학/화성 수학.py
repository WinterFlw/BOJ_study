for i in range(int(input())):
    str = input().split()
    rst = 0
    for j in range(len(str)):
        if j == 0:
            rst = float(str[j])
        if str[j] == "@":
            rst *= 3.00
        elif str[j] == "%":
            rst += 5.00
        elif str[j] == "#":
            rst -= 7.00
    print(f"{rst:.2f}")