cont = 0


def DFS(target):
    global cont
    visited[target] = 1

    for i in net[target]:
        if visited[i] == 0:
            DFS(i)
            cont += 1


def BFS(target):
    global cont
    visited[target] = 1
    que = [target]
    while que:
        for i in net[que.pop()]:
            if visited[i] == 0:
                visited[i] = 1
                que.insert(0, i)
                cont += 1


N = int(input())
edge = int(input())
visited = [0]*(N+1)

net = [[]*(N+1) for _ in range(N+1)]

for i in range(edge):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

BFS(1)
print(cont)
