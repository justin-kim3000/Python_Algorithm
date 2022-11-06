# 1~15:E, 1~28:S, 1~19:M
E, S, M = map(int, input().split())
tempE = 1
tempS = 1
tempM = 1
cou = 1

while(1):
    if tempE == E and tempS == S and tempM == M:
        break
    tempM += 1
    tempS += 1
    tempE += 1
    cou += 1

    if tempE > 15:
        tempE -= 15
    if tempS > 28:
        tempS -= 28
    if tempM > 19:
        tempM -= 19
print(cou)
# while(1):
#     if tempE == E and tempS == S and tempM == M:
#         break
#     if tempE % 15 == 0:
#         tempE = 0
#     elif tempS % 28 == 0:
#         tempS = 0
#     elif tempM % 19 == 0:
#         tempM = 0

#     tempM += 1
#     tempS += 1
#     tempE += 1

#     cou += 1
# print(cou)
