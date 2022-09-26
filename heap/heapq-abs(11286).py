import heapq
import sys


X = int(input())
heap = []

for i in range(X):
    x = int(sys.stdin.readline())
    if x != 0:
        # heappush - 리스트에 값을 추가함
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
