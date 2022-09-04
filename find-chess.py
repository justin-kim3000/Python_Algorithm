# 킹 1 / 퀸 1 / 룩 2 / 비숍 2 / 나이트 2 / 폰 8

# def find_chess(king=1, queen=1, ruck=2, bishop=2, knight=2, pawn=8):
#     if (king and queen == 1):
#         return king, queen
#     elif (king and queen != 1):
#         return -(king - 1), -(queen - 1)
#     elif (ruck and bishop and knight == 2):
#         return ruck, bishop, knight
#     elif (ruck and bishop and knight != 2):
#         return -(ruck - 2), -(bishop - 2), -(knight - 2)
#     elif (pawn == 8):
#         return pawn
#     elif (pawn != 8):
#         return -(pawn - 8)
#     else:
#         print("error")


# print(find_chess(5, 2, 2, 2, 7))


answer = [1, 1, 2, 2, 2, 8]
inputNumber = list(map(int, input().split()))
for i in range(6):
    print(answer[i]-inputNumber[i], end=' ')
