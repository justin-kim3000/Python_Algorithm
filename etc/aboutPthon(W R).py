# 파일 제어
# 1. 기본 파일 쓰기

# file = open("test.txt", "w")
# file.write("hi안녕")
# file.close()

# 2. 기본 파일 읽기
# try:     
#     file = open("test.txt","r")
#     data = file.read()
#     print(data)
#     file.close()
# except FileNotFoundError as e:
#     print("파일을 찾을 수 없습니다.",e)
#finally:    # 생략가능
#    file.close()

# with open("test.txt","r") as fi:
#     print(fi.read())
    
# 3. 라인단위로 파일 쓰기
# lines = ['안녕하세요.\n','반갑습니다.\n','홍길동입니다.\n']
# try:
#     with open('hello.txt','w') as f:
#         for line in lines:
#             f.write(line)
# except Exception as err:
#     print("파일쓰기 에러: ", err)
# else:
#     print("파일 쓰기 성공!")
    
# 4. 라인 단위로파일 읽기
# try:
        
#     with open('hello.txt', 'r') as f:
#         line = f.readline()
#         while line != '':
#             print(line)
#             line = f.readline()
# except :
#     print("파일 읽기 에러")

# # 5. 라인 전체를 파일에 쓰기
# lines = ['안녕하세요~.\n','반갑습니다~~.\n','홍길동입니다~~~.\n']
# try:    
#     with open('hellow2.txt','w') as f:
#         f.writelines(lines)
# # 예외 처리시 큰 범위는 나중에 쓴다(ex.Exception)
# # except는 사용 후 코드 탈출
# except FileNotFoundError as err:
#     print("파일 에러111", err)
# except Exception as err:
#     print("파일 엥러",err)
    
# # 라인 전체 파일 읽기
# try:    
#     with open('hellow2.txt','r') as f:
#         lines = f.readlines() # 오타주의
#         for line in lines:
#             print(line)
# # 예외 처리시 큰 범위는 나중에 쓴다(ex.Exception)
# # except는 사용 후 코드 탈출
# except FileNotFoundError as err:
#     print("파일 에러111", err)
# except Exception as err:
#     print("파일 엥러",err)
    
# uft8 타입으로 쓰기
# lines = ['こんにちは','你好','안녕?']
# with open('hello_utf8.txt','w',encoding='utf-8') as f:
#     for line in lines:
#         f.write(line+'\n')

# with open('hello_utf8.txt','r',encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# bin 파일 쓰기
import struct
strct_fmt = '=16s2fi' # char[16], float[2], int
city_info = [
    ('서울'.encode(encoding='utf-8'), 37.566, 127.472, 1),
    ('뉴욕'.encode(encoding='utf-8'), 49.526, 131.137, 2),
    ('파리'.encode(encoding='utf-8'), 21.556, 227.723, 3),
    ('런던'.encode(encoding='utf-8'), 90.766, 67.741, 4)    
]
with open('citi_info.dat', 'wb') as f:
    for city in city_info:
        f.write(struct.pack(strct_fmt, *city))
        
# bin 파일 읽기
strct_fmt = '=16s2fi' # char[16], float[2], int
struct_len = struct.calcsize(strct_fmt)
cities = []

with open('citi_info.dat', 'rb') as f:
    while True:
        buffer = f.read(struct_len)
        if not buffer: break
        city = struct.unpack(strct_fmt, buffer)
        cities.append(city)
        
for city in cities:
    name = city[0].decode(encoding='utf-8')
    print(f'도시: {name}, '
          f'경도 / 위도 : {city[1]}/{city[2]}, '
          f'인기점수: {city[3]}')