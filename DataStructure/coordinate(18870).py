N = int(input())

xy = list(map(int, input().split()))
res = sorted(list(set(xy)))

resDict = {}

for i in range(len(res)):
    resDict[res[i]] = i

for i in range(len(xy)):
    xy[i] = resDict[xy[i]]

# 주소값? 이용 출력
# print(*xy, sep=' ')

# 반복문으로 출력
for i in xy:
    print(i, end=' ')
