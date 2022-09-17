# time out.....
countCard = int(input())
cardList = list(map(int, range(1, countCard+1)))
while 1:
    if len(cardList) == 1:
        print(cardList)
        break
    else:
        cardList.pop(0)
        cardList.append(cardList[0])
        cardList.pop(0)
