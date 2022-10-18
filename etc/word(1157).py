N = input().upper()
tempN = list(set(N))
countList = []
for i in range(len(tempN)):
    countList.append(N.count(tempN[i]))

if countList.count(max(countList)) > 1:
    print('?')
else:
    print(tempN[countList.index(max(countList))])
