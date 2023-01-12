# name = [i for i in range(1,11)]
# delName = int(input())
# try:
#     name.remove(delName)
#     print(f'{delName} 이 삭제')
# except:
#     print(f'{delName} 데이터가 없습니다.')


# ev_name = [i for i in name if i %2==0]
# print(ev_name)

# rand = [[i,j]for i in range(3) for j in range(2)]
# print(rand)

# for i in range(3):
#     for j in range(2):
#         print(i,j)

# for i in rand:
#     for j in i:
#         print(j, end=' ')
#     print()

# # 비어있는 2차원 리스트 생성
# row, col = 3,4
# arrList = [[0 for _ in range(col)] for _ in range(row)]

# print(arrList)

# # 튜플
# # list= [], tupple=(), dict = {}
# my_num = (1,2,3,4,5)
# print(type(my_num))
# print(my_num[0])

# # 딕셔너리
# dic = {1:"www.google.com",2:"www.naver.com",3:"tistory.com"}

# key = 1

# if key in dic:
#     print(f'{key}가 dic안에 있습니다.')
#     print(f'{dic.get(key)}는 dic 값입니다.')
# else:
#     print(f'{key}가 dic안에 없습니다.')

# value = "kk"

# if value in dic.values():
#     print(f'{value}가 dic안에 있습니다.')

# else:
#     print(f'{value}가 dic안에 없습니다.')

# #del dic[1]
# print(dic)

# key = input("키를 입력하세요")
# if key in dic:
#     del dic[key]
# elif key == '삼성전자':
#     dic[key] = 'www.sec.com'

# print(dic)

# # 함수
# def main():
#     print(11)

# if __name__ == '__main__':
#     main()


# def calculate() -> int:
#     num1 = int(input("1번 숫자 입력: "))
#     num2 = int(input("1번 숫자 입력: "))
#     op = input("연산자 입력(+,-,/,*)")

#     if op == '+':
#         res = num1 + num2
#     elif op == '-':
#         res = num1 - num2
#     elif op == '*':
#         res = num1 * num2
#     elif op == '/':
#         res = num1 / num2

#     return res

# print(round(calculate(),2))
# # 빈 함수는 pass 사용
# def notin():
#     pass

# # 전역 변수, 지역 변수 -> 반드시 함수에서만 적용
# gNum = 200
# def funcLocal():
#     global gNum
#     print(gNum)


# def gugu():
#     for i in range(2,10):
#         for j in range(1,10):
#             print(f'{i}*{j} = {j*i}',end=' ')
#         print()

# def program_exit():
#     print("프로그램 종료")
#     exit()

# def show_menu():
#     print("=======================")
#     print("동작 테스트")
#     print("=======================")
#     print("2.구구단")
#     menu = int(input("메뉴 선택"))
#     return menu

# if __name__ == '__main__':
#     while True:
#         me = show_menu()
#         if me == 2: gugu()
#         elif me ==3: program_exit()
#         else: print("재 선택 요청")

# # 디폴트 값
# def info_print(name, pos = 'staff',nation='korea'):
#     print(name,pos,nation)

# info_print('king')

# # 가변인자 튜플
# # 튜플을 매개변수로 받을때는 *을 붙임
# def strAppend(*textList):
#     res = ''
#     for i in textList:
#         res += i
#     return res

# print(strAppend('안녕하세요요용'))
# tup = ('1','2','3','4','5','6','7')
# print(strAppend(*tup))

# # 가변인자 - 딕셔너리
# # 매개변수 사용시 ** 붙임
# def showDict(**player):
#     for i in player.keys():
#         print(f'{i}={player[i]}')
#     print()

# showDict(gool = 'GK', oo ='KA')
# showDict(gool = 'GK', oo ='KA',pp='ad')
# showDict(gool = 'GK', oo ='KA',pp='ad',olw='21')

# 함수를 변수에 담기
from functools import reduce
import math


# def myFunc(a):
#     print(a)


# p = myFunc
# p(111)

# # 함수 변수에 담기 2


# def plus(a, b):
#     return a+b


# def minus(a, b):
#     return a-b

# fList = [plus,minus]
# n1, n2 = 2,1
# print(fList[0](n1,n2))
# print(fList[1](n1,n2))

# # 중첩함수(Nested function)
# # 외부접근 불가
# def stddev(*args):
#     def mean():
#         return sum(args) / len(args)

#     def variance(m): # 분산
#         total = 0
#         for arg in args:
#             total += (arg-m) **2
#             return total / (len(args)-1)

#     v = variance(mean())
#     return math.sqrt(v)

# print(stddev(1,2,3,4,222))

# # 람다식 - 임시로 사용하는 간단한 기능의 익명 함수
# def calc():
#     a=3
#     b=5
#     return lambda x : a*x+b

# c = calc()
# print(c(1),c(2),c(3))

# # 람다 표현식
# func1 = lambda x,y : x+y
# func2 = lambda x: x*x

# print(func1(10,20))
# print(func2(10))

# # 람다 함수
# def func1_lamb(n):
#     return lambda x,y : x+y+n

# lam1 = func1_lamb(10)
# print(lam1(20,30))
# print(func1_lamb(1)(2,3))

# 람다식 + map()
num1 = [i for i in range(1, 6)]
num2 = [i for i in range(1, 11) if i % 2 == 0]

# print(num1,num2)
# print(list(map(lambda x,y : x*y, num1, num2)))

print(list(map(lambda x: x+10 if x % 2 == 0 else x, num1)))

# 람다식 + filter()
num3 = [i for i in range(1, 11)]
print(list(filter(lambda x: x % 3 == 0, num3)))

# 람다식 + reduce()
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
