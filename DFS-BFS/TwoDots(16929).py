# N, M = map(int, input().split())

# room = []

# for i in range(N):
#     room.append(list(map(str, input())))

# for i in range(N-1):
#     for j in range(M-1):
#         room[i][j]
# print(room)
# print(room[1][2])

# 참고 자료
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cycle = False


N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(list(sys.stdin.readline().strip()))

print(board)


def dfs(x, y, curX, curY, cnt, color):
    global cycle
    if cycle:
        return

    visited[curX][curY] = True
    if x == curX and y == curY and cnt >= 4:
        cycle = True
        return

    for i in range(4):
        nx = curX + dx[i]
        ny = curY + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and color == board[nx][ny]:
                dfs(x, y, nx, ny, cnt+1, color)
            elif nx == x and ny == y and cnt >= 4:
                dfs(x, y, nx, ny, cnt, color)
    return


for i in range(N):
    for j in range(M):
        visited = [[False] * M for _ in range(N)]
        visited[i][j] = True
        dfs(i, j, i, j, 1, board[i][j])

if cycle:
    print("Yes")
else:
    print("No")
