from posixpath import split


fixedCosts, variableCosts, priceGoods = map(int, input().split())

i = 1

while priceGoods*i <= fixedCosts + variableCosts*i:
    i += 1
    if priceGoods < variableCosts:
        i = -1
        break
print(i)
