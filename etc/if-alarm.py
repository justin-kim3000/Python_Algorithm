number1, number2 = input().split()

number1 = int(number1)
M = int(number2)

Setting = 45
if number1 != 0 and number2-Setting < 0:
    print(number1-1, number2+60-Setting)
elif number1 == 0 and number2-Setting < 0:
    number1 = 23
    print(number1, number2+60-Setting)
else:
    print(number1, number2-Setting)
