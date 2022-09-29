# 토마토 익히기 위해한 최소일수
# 익은 토마토 위, 아래, 좌, 우 가 익음
# 대각선 토마토는 영향이 없다.

from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

# 방향 리스트(좌, 우)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

result = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

# 토마토 위치 확인
print(queue)


def bfs():
    while queue:
        # 첫 토마토 좌표
        x, y = queue.popleft()

        # 토마토의 사분면을 익힘.
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            # 좌표가 좌표 크기를 넘으면 안되며, 해당 좌표의 토마토는 익지 않아(0)야 함
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])


bfs()

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))

print(result - 1)
