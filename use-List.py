# M 보다 작은 수 출력
# N, M = map(int, input().split())
# list_N = list(map(int, input().split()))


# for i in range(0, N):
#     if(list_N[i] < M):
#         print(list_N[i], end=" ")

# ----------------------------------------

# 리스트 안의 같은 숫자 카운트 하기
# numberCount = int(input())
# numberList = list(map(int, input().split()))
# numberFind = int(input())
# count = 0

# for i in range(numberCount):
#     if(numberList[i] == numberFind):
#         count +=1

# print(count)

# ---------------------------------------

# 소거법 사용
# student = list(map(int, range(1, 31)))

# for _ in range(28):
#     inputStudent = int(input())
#     student.remove(inputStudent)

# print(student[0])
# print(student[1])

# ---------------------------------------

# 행렬 문제 보충 할것
N, M = map(int, input().split())
A, B, result = [], [], []

for i in range(N):
    i = list(map(int, input().split()))
    A.append(i)
for i in range(N):
    i = list(map(int, input().split()))
    B.append(i)

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end=' ')
    print()
