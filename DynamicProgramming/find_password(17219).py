from collections import deque

N, M = map(int, input().split())
sitePassword = {}

for _ in range(N):
    key, value = map(str, input().split())
    sitePassword[key] = value

for _ in range(M):
    findPassWord = input()
    print(sitePassword[findPassWord])
