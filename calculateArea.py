from math import sqrt


def calculateArea(x, y, w, h):
    return sqrt((x-w)**2+(y-h)**2)


print(calculateArea(6, 2, 10, 3))
