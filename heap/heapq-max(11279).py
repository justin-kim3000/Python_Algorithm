import heapq
import sys

x = int(sys.stdin.readline())
heap = []

for i in range(x):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        if heap:
            print(-1*heapq.heappop(heap))
        else:
            print(0)
