testCase = int(input())

for _ in range(testCase):
    N = int(input())
    testlist = []
    countli = 1
    for _ in range(N):
        testlist.append(list(map(int, input().split())))
    testlist.sort()

    minli = testlist[0][1]

    for i in range(len(testlist)):
        if testlist[i][1] < minli:
            countli += 1
            minli = testlist[i][1]

    print(countli)
