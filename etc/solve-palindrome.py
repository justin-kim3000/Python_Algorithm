
while (1):
    inputNumber = input()
    if inputNumber == '0':
        break
    else:
        if inputNumber == inputNumber[::-1]:
            print("yes")
        else:
            print("no")
