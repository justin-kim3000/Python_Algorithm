inputNumber = str(input())


def sumSeparation(number):
    temp = 0
    for i in number:
        temp += int(i)
    print(temp+int(number))


sumSeparation(inputNumber)
