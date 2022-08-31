inputNumber = int(input())

temp = []
for i in range(inputNumber):
    temp.append(int(input()))
    i += 1


list_set = list(set(temp))
list_set.sort()

for i in list_set:
    print(i)

# def arrayAppend(num):
#     temp = []
#     for i in range(num):
#         temp.append(int(input()))
#         i += 1
#     return temp
