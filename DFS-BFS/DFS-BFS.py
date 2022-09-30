import sys
from collections import deque

# N -> 정점의 개수
# M -> 간선의 개수
# V -> 시작할 정점의 번호

N, M, V = map(int, input().split())

# ---------참고 자료 -----------#
# 행렬 만들기
# graph = [[0]*(N+1) for _ in range(N+1)]
# print(graph)
# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a][b] = graph[b][a] = 1
# print(graph)

# # 방문 리스트 행렬
# visited1 = [0]*(N+1)
# visited2 = visited1.copy()

# dfs 함수 만들기


# def dfs(V):
#     visited1[V] = 1  # 방문처리
#     print(V, end=' ')
#     for i in range(1, N+1):
#         if graph[V][i] == 1 and visited1[i] == 0:
#             dfs(i)

# #bfs 함수 만들기
# def bfs(V):
#     queue = [V]
#     visited2[V] = 1 #방문처리
#     while queue:
#         V = queue.pop(0) #방문 노드 제거
#         print(V, end = ' ')
#         for i in range(1, N+1):
#             if(visited2[i] == 0 and graph[V][i] == 1):
#                 queue.append(i)
#                 visited2[i] = 1 # 방문처리

# dfs(V)
# print()
# bfs(V)
# -----------------------------------

# ----------- 참고자료2 ---------------
def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
for i in range(1, N+1):
    graph[i].sort()

print(graph)

visited = [False]*(N+1)
dfs(V)
print()
visited = [False]*(N+1)
bfs(V)
