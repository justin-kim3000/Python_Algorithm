#공백으로 나누기
a,b,c = input().split()

#정수 지정
a = int(a)
b = int(b)
c = int(c)

#나머지 출력
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)