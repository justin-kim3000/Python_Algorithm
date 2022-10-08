# if (n>3), f(n) = f(n-1)+f(n-2)+f(n-3)

testCase = int(input())

def loof(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    elif number == 3:
        return 4
    else:
        return loof(number-1)+loof(number-2)+loof(number-3)
    
for i in range(testCase):
    number = int(input())
    print(loof(number))

