
for i in range(int(input())):
    countNum = 0
    sumNum = 0
    OX = input()
    for i in range(len(OX)):
        if OX[i] == "O":
            countNum += 1
            sumNum += countNum
        else:
            countNum = 0
    print(sumNum)
