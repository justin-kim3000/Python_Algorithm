from collections import deque

N, K = map(int, input().split())
# 빈칸 만듬
visited = [-1 for _ in range(100001)]
# 방문하면 0
visited[N] = 0

deq = deque()
deq.append(N)

while deq:
    pop = deq.popleft()
    if pop == K:
        print(visited[pop])
        break
    if 0 <= pop-1 < 100001 and visited[pop-1] == -1:
        visited[pop-1] = visited[pop] + 1
        deq.append(pop - 1)
    if 0 < pop*2 < 100001 and visited[pop*2] == -1:
        visited[pop*2] = visited[pop]
        deq.appendleft(pop*2)
    if 0 <= pop+1 < 100001 and visited[pop+1] == -1:
        visited[pop+1] = visited[pop] + 1
        deq.append(pop + 1)
