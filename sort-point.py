N = int(input())
numList = []
for i in range(N):
    numList.append(list(map(int, input().split())))

numList.sort()

for i in range(N):
    print(numList[i][0], numList[i][1])
