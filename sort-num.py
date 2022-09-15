# time over..
import sys

N = int(input())
NumberList = []
for i in range(N):
    NumberList.append(sys.stdin.readline())

NumberList.sort()

for i in NumberList:
    print(i)
