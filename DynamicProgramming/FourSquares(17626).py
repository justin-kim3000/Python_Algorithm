from math import sqrt

n = int(input())
countNum = 0

if type(sqrt(n)) is float:
    countNum += 1


print(countNum)
print(sqrt(n))
