n = int(input())

data = []
result = []

for i in range(n):
    wight, hieght = map(int, input().split())
    data.append((wight, hieght))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    result.append(count + 1)

for i in result:
    print(i, end=" ")
