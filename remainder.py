# 공백으로 나누기
number1, number2, number3 = input().split()

# 정수 지정
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)

# 나머지 출력
print((number1+number2) % number3)
print(((number1 % number3)+(number2 % number3)) % number3)
print((number1*number2) % number3)
print(((number1 % number3)*(number2 % number3)) % number3)
