N = int(input())
firstNum = str(N)
countNum = 0

while 1:
    if len(firstNum) == 1:
        firstNum = "0"+firstNum
    sum1 = firstNum[0]
    sum2 = firstNum[1]
    plusNum = str(int(sum1)+int(sum2))
    firstNum = firstNum[-1]+plusNum[-1]

    countNum += 1
    if int(firstNum) == N:
        print(countNum)
        break
