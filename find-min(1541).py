array_number = input().split('-')
print(array_number)
sum = 0
for i in array_number[0].split('+'):
    sum += int(i)
for i in array_number[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)