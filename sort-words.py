
import sys

N = int(sys.stdin.readline())
NList = []
for _ in range(N):
    NList.append(sys.stdin.readline().strip())
setNList = set(NList)
NList = list(setNList)
NList.sort()
NList.sort(key=len)
for i in NList:
    print(i)