import sys

N = int(sys.stdin.readline())
countNum = 0

# 재귀로 안풀림..
# def calculate(N):
#     global countNum
#     if N == 1:
#         print(countNum, "1일때 마지막")
#         return
#     else:
#         if N % 3 == 0:
#             calculate(N//3)
#             countNum += 1
#             print(N, "3333333333 나누기 N은?")
#             print(countNum, "3333333333 나누기")
#         elif N % 2 == 0:
#             calculate(N//2)
#             countNum += 1
#             print(N, "/////////////2 나누기 N은?")
#             print(countNum, "///////////2 나누기")
#         else:
#             calculate(N-1)
#             countNum += 1
#             print(N, "--------------1 빼기 N은?")
#             print(countNum, "----------1 빼기")
#         print(countNum, "마지막!!!!!!!")
