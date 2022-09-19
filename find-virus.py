countComputer = int(input())
connectComputer = int(input())
connectList = []
countVirus = 0
temp = []
for i in range(connectComputer):
    connectList.append(list(map(int,input().split())))

for i in range(len(connectList)):
    if 1 in connectList[i]:
        temp.append(connectList[i][1])
        countVirus+=1
    for j in range(len(temp)):
        if temp[j] in connectList[i]:
            countVirus +=1
    
print(countVirus)
print(temp)