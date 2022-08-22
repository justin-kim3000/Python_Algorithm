compareNumber1, compareNumber2 = input().split()

compareNumber1 = int(compareNumber1)
compareNumber2 = int(compareNumber2)

if compareNumber1 > compareNumber2:
    print(">")
elif compareNumber1 < compareNumber2:
    print("<")
else:
    print("==")
