# 가장 증가하는 부분 수열 구하시오.

N = int(input())
cou = 1
numlist = list(map(int, input().split()))
temp = 0

print(max(numlist[:3]))


# for i in range(1, N):
#     if numlist[i] > max(numlist[:i-1]):
#         cou += 1
print(cou)
