# 블록 제거 작업 2초 걸림 / 블록 추가 작업 1초 걸림
N,M,B = map(int,input().split())

li = []

for i in range(N):
    li.append(list(map(int,input().split())))


print(li)
import sys
N, M, B = map(int,input().split())
block = []
for _ in range(N):
    block.append([int(x) for x in sys.stdin.readline().rstrip().split()])

ans = int(1e9)
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