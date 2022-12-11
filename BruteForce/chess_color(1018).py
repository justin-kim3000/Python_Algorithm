from collections import deque


N, M = map(int, input().split())
chess = deque([])

for _ in range(N):
    chess.append(input())
print(chess[0][0])

