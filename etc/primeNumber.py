inputNumber = int(input())
inputNumbers = list(map(int, input().split()))
count = 0

for i in inputNumbers:
    temp = 0
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0:
                temp += 1

        if temp == 1:
            count += 1


print(count)
