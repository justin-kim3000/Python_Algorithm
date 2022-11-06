# 1~15:E, 1~28:S, 1~19:M
E, S, M = map(int, input().split())
tempE = 1
tempS = 1
tempM = 1
cou = 1

while(1):
    if tempE == E and tempS == S and tempM == M:
        print(cou)
        break
    elif tempE % 15 == 0:
        tempE = 0
    elif tempS % 28 == 0:
        tempS = 0
    elif tempM % 19 == 0:
        tempM = 0

    tempM += 1
    tempS += 1
    tempE += 1
    print(tempM, tempS, tempE)

    cou += 1
