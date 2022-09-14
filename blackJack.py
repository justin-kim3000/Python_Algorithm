getCard, maxSum = map(int, input().split())
cardCollection = list(map(int, input().split()))
sum1 = 0

# 어짜피 3번 안에 완료하면 됨
for i in range(getCard):
    for j in range(i+1, getCard):
        for k in range(j+1, getCard):
            if(cardCollection[i]+cardCollection[j]+cardCollection[k] > maxSum):
                continue
            else:
                sum1 = max(
                    sum1, cardCollection[i]+cardCollection[j]+cardCollection[k])
print(sum1)
