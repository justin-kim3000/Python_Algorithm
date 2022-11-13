N = int(input())
NList = list(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))

for i in MList:
    if i in NList:
        print(1)
    else:
        print(0)
