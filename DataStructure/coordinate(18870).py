
from unittest import result


N = int(input())

xy = list(map(int, input().split()))
print(xy)
res = []
print(res)
print(xy.index(min(xy)))

for i in range(N):
    liMin = xy.index(min(xy))
    res.insert(liMin, 0)


print(res)
