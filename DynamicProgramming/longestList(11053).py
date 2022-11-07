# 가장 증가하는 부분 수열 구하시오.

N = int(input())
cou = 0
numlist = list(map(int, input().split()))
temp = 0
for i in range(N):
    if numlist[i] >= max(numlist[:i+1]):
        cou += 1
print(cou)
