Ncity = int(input())

langhByCity = []
oilPrice = []

langhByCity = list(map(int, input().split()))
oilPrice = list(map(int, input().split()))

res = 0
mini = oilPrice[0]
for i in range(Ncity-1):
    if oilPrice[i] < mini:
        mini = oilPrice[i]
    res += mini * langhByCity[i]

print(res)
