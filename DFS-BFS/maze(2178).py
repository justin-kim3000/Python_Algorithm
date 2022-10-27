from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(1, N+1):
    graph.append(list(map(int, input())))

# x,y 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # 방문할 곳의 큐를 만듬
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[N-1][M-1]


print(bfs(0, 0))
print(graph)
