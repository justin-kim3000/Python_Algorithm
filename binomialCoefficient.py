BCNumber1, BCNumber2 = map(int, input().split())
temp1 = 1
temp2 = 1
temp3 = 1

for i in range(1, BCNumber1+1):
    temp1 *= i

for i in range(1, BCNumber2+1):
    temp2 *= i

for i in range(1, BCNumber1-BCNumber2+1):
    temp3 *= i

print(int(temp1/(temp2*temp3)))
