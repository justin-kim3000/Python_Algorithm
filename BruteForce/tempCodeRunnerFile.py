num = 9

height = []
for i in range(num):
    height.append(int(input()))

for i in range(num):
    for j in range(num):
        if i != j:
            if sum(height) - height[i] - height[j] == 100:
                temp1 = height[i]
                temp2 = height[j]

height.remove(temp1)
height.remove(temp2)


height.sort()

for i in height:
    print(i)
