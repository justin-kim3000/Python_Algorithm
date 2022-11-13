import sys
N = int(sys.stdin.readline())
NList = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
MList = list(map(int, sys.stdin.readline().split()))

for i in MList:
    if i in NList:
        print(1)
    else:
        print(0)
