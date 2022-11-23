# n가지 종류 동전 / k원 : 동전의 합
# 해당 경우의 수 찾아라

from collections import deque


n, k = map(int, input().split())
deq = deque()
room = [0 for _ in range(k+1)]
room[0] = 1

for _ in range(n):
    deq.append(int(input()))

for i in deq:
    for j in range(1, k+1):
        if j - i >= 0:
            room[j] = room[j] + room[j-i]

print(room[k])
