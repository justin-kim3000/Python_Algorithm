inputNumber = int(input())
count = 1
beeHouse = 1

while inputNumber > beeHouse:
    beeHouse += 6*count
    count += 1

print(count)
