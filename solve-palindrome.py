inputNumber = input()

while (inputNumber != '0'):
    if inputNumber == inputNumber[::-1]:
        print("yes")
    else:
        print("no")
