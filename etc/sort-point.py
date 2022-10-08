N = int(input())
numList = []
# X축 정렬
# for i in range(N):
#     x, y = list(map(int, input().split()))
#     numList.append([x][y])

# numList.sort()

# for i in range(N):
#     print(numList[i][0], numList[i][1])

# Y축 정렬
for i in range(N):
    x, y = list(map(int, input().split()))
    numList.append([y, x])

numList.sort()
for i in range(N):
    print(numList[i][1], numList[i][0])
