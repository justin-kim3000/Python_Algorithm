basicNum = [str(i) for i in range(10)]
givNum = input()
counting = 1

for i in givNum:
    if i in basicNum: 
        basicNum.remove(i)
    elif i == '6' and i not in basicNum:
        if '9' in basicNum:
            basicNum.remove('9')
        else:
            basicNum = [str(i) for i in range(10)]
            counting += 1
    elif i == '9' and i not in basicNum:
        if '6' in basicNum:
            basicNum.remove('6')
        else:
            basicNum = [str(i) for i in range(10)]
            counting += 1
    else:
        basicNum = [str(i) for i in range(10)]
        counting += 1


print(counting)