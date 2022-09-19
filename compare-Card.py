# time over..
# N = int(input())
# N_List = list(map(int,input().split()))

# M = int(input())
# M_List = list(map(int,input().split()))

# def countUp(ListA,ListB):
#     for i in range(len(ListB)):
#         count = 0
#         for j in range(len(ListA)):
#             if ListB[i] == ListA[j]:
#                 count += 1
#         ListB[i] = count
#     # 리스트 값을 한번에 출력하기!(*)
#     print(*ListB)

# countUp(N_List, M_List)


from sys import stdin

n = stdin.readline()
card = list(map(int,stdin.readline().split()))
m = stdin.readline()
test = list(map(int,stdin.readline().split()))

dic = {}

for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in test:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')