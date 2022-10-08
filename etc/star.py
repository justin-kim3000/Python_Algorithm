Num = int(input())
up = 1

while (Num > 1):
    Num -= 1
    print(" "*Num, end="")
    print("*"*up)
    up += 1
print("*"*up)

# other solution
a = int(input())
for i in range(1, a+1):
    print(" "*(a-i) + "*"*i)
