from math import sqrt

n = int(input())
countNum = 0
check = 0
room = [i**2 for i in range(1, n+1)]
print(room)

if sqrt(n)**2 == n:
    print(1)
else:
    for i in range(n-1, 0, -1):
        check += room[i]
        if n < check:
            countNum += 1
        elif n == check:
            countNum += 1
            break
        elif n > check:
            check -= room[i]
        else:
            countNum = 0
    print(countNum)
