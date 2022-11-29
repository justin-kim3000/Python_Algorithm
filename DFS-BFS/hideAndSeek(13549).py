# N부터 K까지 가는데 걸리는 시간을 구하시오.*2는 시간 안걸림

from collections import deque
# N = 시작점 / K = 도착점(K 최대값 100,000)
N, K = map(int, input().split())

# 빈칸 만듬
visited = [-1 for _ in range(100001)]
# 방문하면 0
visited[N] = 0
# 큐만듬
deq = deque()
deq.append(N)

# 큐가 있으면 반복
while deq:
    pop = deq.popleft()
    # popleft가 도착점과 같으면 해당 좌표 인쇄 후 종료
    if pop == K:
        print(visited[pop])
        break
    # 1초 후 -1로 이동함
    if 0 <= pop-1 < 100001 and visited[pop-1] == -1:
        visited[pop-1] = visited[pop] + 1
        deq.append(pop - 1)
    # 순간이동 *2 (시간 카운팅 x)
    if 0 < pop*2 < 100001 and visited[pop*2] == -1:
        visited[pop*2] = visited[pop]
        deq.appendleft(pop*2)
    # 1초 후 +1로 이동함
    if 0 <= pop+1 < 100001 and visited[pop+1] == -1:
        visited[pop+1] = visited[pop] + 1
        deq.append(pop + 1)
