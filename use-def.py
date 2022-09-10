# def calculate(A, B):
#     print((A+B)*(A-B))


# A, B = map(int, input().split())

# calculate(A, B)

def verification(number):
    for i in number:
        temp += int(i)**2
    print(temp % 10)


temp = 0

for i in list(map(int, input().split())):
    temp += int(i)**2
print(temp % 10)
