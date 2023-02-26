# 블록 제거 작업 2초 걸림 / 블록 추가 작업 1초 걸림
import sys
N, M, B = map(int,input().split())
block = []
for _ in range(N):
    block.append([int(x) for x in sys.stdin.readline().rstrip().split()])

ans = 6.4*10**7
glevel = 0

for i in range(257): #땅 높이
    use_block = 0
    take_block = 0
    for x in range(N):
        for y in range(M):
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                use_block += i - block[x][y]

    if use_block > take_block + B:
        continue

    count = take_block * 2 + use_block

    if count <= ans:
        ans = count
        glevel = i

print(ans, glevel)

import sys
from collections import Counter

n, m, inven = map(int, sys.stdin.readline().split())
ground = []
for _ in range(n):
    ground += map(int, sys.stdin.readline().split())
height, time = 0, 1000000000000000

min_h = min(ground)
max_h = max(ground)
_sum = sum(ground)
ground = dict(Counter(ground))

for i in range(min_h, max_h + 1):
    if _sum + inven >= i * n * m:
        cur_time = 0
        for key in ground:
            if key > i:
                cur_time += (key - i) * ground[key] * 2
            elif key < i:
                cur_time += (i - key) * ground[key]
        if cur_time <= time:
            time = cur_time
            height = i

print(time, height)