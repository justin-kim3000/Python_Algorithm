while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a <= c and b <= c and a**2 + b**2 == c**2:
            print("right")
        elif a <= b and c <= b and a**2 + c**2 == b**2:
            print("right")
        elif b <= a and c <= a and b**2 + c**2 == a**2:
            print("right")

        else:
            print("wrong")
