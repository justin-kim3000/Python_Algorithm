# name = [i for i in range(1,11)]
# delName = int(input())
# try:
#     name.remove(delName)
#     print(f'{delName} 이 삭제')
# except:
#     print(f'{delName} 데이터가 없습니다.')
    
    
# ev_name = [i for i in name if i %2==0]
# print(ev_name)

rand = [[i,j]for i in range(3) for j in range(2)]
print(rand)

for i in range(3):
    for j in range(2):
        print(i,j)
        
for i in rand:
    for j in i:
        print(j, end=' ')
    print()
    
# 비어있는 2차원 리스트 생성
row, col = 3,4
arrList = [[0 for _ in range(col)] for _ in range(row)]

print(arrList)

# 튜플
# list= [], tupple=(), dict = {}
my_num = (1,2,3,4,5)
print(type(my_num))
print(my_num[0])