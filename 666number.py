# 666이 들어간 숫자를 순서에 맞게 출력하시오.
# ex) 1 -> 666 // 2 -> 1666 // 6 -> 5666

N = int(input())
num = 666
count = 0
while(1):
    if '666' in str(num):
        count +=1
    if count == N:
        print(num)
        break
    # print(num)
    num +=1