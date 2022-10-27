from re import M


N, K = map(int, input().split())
money = []
sumMoneyLi = []
sumMoney = 0
countNum = 0

for i in range(N):
    money.append(int(input()))

print(money)
# while 1:
#     if sumMoney == K:
#         print(countNum)
#         break

for i in range(len(money)):
    if money[i] > K:
        sumMoneyLi.append(money[i-1])
        for k in range(1, 11):
            if sumMoneyLi[0]*k > K:
                sumMoneyLi[0] = sumMoneyLi[0]*(k-1)
                break

        for j in range(i):
            if sumMoneyLi[0] + money[j] > K:
                sumMoneyLi.append(money[j-1])
                for l in range(1, 11):
                    if sumMoneyLi[0]+sumMoneyLi[1]*l > K:
                        sumMoneyLi[1] = sumMoneyLi[1]*(l-1)
                        break

        break

print(sumMoneyLi)
