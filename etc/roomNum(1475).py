basicNum = [0,1,2,3,4,5,6,7,8,9]
givNum = list(input())
counting = 1

for i in givNum:
    if i in basicNum: 
        basicNum.remove(i)
        pass
    elif i == '6' and i not in basicNum:
        if '9' in basicNum:
            basicNum.remove('9')
        else:
            basicNum = [0,1,2,3,4,5,6,7,8,9]
            counting += 1
    elif i == '9' and i not in basicNum:
        if '6' in basicNum:
            basicNum.remove('6')
        else:
            basicNum = [0,1,2,3,4,5,6,7,8,9]
            counting += 1
    else:
        basicNum = [0,1,2,3,4,5,6,7,8,9]
        counting += 1


print(counting)