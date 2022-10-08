
from math import factorial


BCNumber1, BCNumber2 = map(int, input().split())
# 맨땅 헤딩
# temp1 = 1
# temp2 = 1
# temp3 = 1

# for i in range(1, BCNumber1+1):
#     temp1 *= i

# for i in range(1, BCNumber2+1):
#     temp2 *= i

# for i in range(1, BCNumber1-BCNumber2+1):
#     temp3 *= i

# print(int(temp1/(temp2*temp3)))

# use math
print(factorial(BCNumber1)/(factorial(BCNumber1-BCNumber2)*factorial(BCNumber2)))
