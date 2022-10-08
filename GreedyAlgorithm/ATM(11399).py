N = int(input())
timeP = list(map(int, input().split()))
sumTime = 0

timeP.sort()
for i in timeP:
    sumTime += i*N
    N -= 1

print(sumTime)
