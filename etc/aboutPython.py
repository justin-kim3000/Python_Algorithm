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


def calculate() -> int:
    num1 = int(input("1번 숫자 입력: "))
    num2 = int(input("1번 숫자 입력: "))
    op = input("연산자 입력(+,-,/,*)")
    
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    elif op == '/':
        res = num1 / num2
        
    return res

print(round(calculate(),2))