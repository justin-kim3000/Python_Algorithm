
from collections import deque


N, K = map(int, input().split())

# 아이디어 : 리스트를 이용해 1부터 N까지 행렬을 만들고, K배수의 index를 추출 후 지운다. (조건 : index번호가 N을 넘어갈때 다시 돌아와서 카운트 한다.)
Number1 = list(map(int, range(1, N+1)))
temp = deque([])

while(1):
    if len(Number1) == 0:
        break
    else:
        temp.append(Number1[K-1])
        del Number1[K-1]


print(temp)
