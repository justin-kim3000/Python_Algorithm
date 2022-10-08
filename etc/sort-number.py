import sys
N =int(sys.stdin.readline())
NumList = []
for _ in range(N):
    NumList.append(int(sys.stdin.readline()))
    
NumList.sort()
for i in range(N):
    print(NumList[i])
