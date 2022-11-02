Ncity = int(input())

langhByCity = []
oilPrice = []

langhByCity = list(map(int, input().split()))
oilPrice = list(map(int, input().split()))

del oilPrice[-1]
minoilprice = min(oilPrice)
print(oilPrice.index(minoilprice))


print(oilPrice)
print(langhByCity)
