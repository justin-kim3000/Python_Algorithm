getCard, maxSum = map(int, input().split())
cardCollection = list(map(int, input().split()))
result = []
sum1 = 0

for i in range(getCard):
    if max(cardCollection) + sum1 < maxSum:
        maxList = max(cardCollection)
        popList = cardCollection.remove(maxList)
        sum1 += maxList
# result.append(popList)

print(sum1)
