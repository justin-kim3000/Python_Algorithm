
listNumber = []
for _ in range(9):
    listNumber.append(int(input()))

print(max(listNumber))
print(listNumber.index(max(listNumber))+1)
