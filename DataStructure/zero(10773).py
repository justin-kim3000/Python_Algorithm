from collections import deque


K = int(input())
li = deque()

for _ in range(K):
    temp = int(input())
    if temp != 0:
        li.append(temp)
    else:
        li.pop()
    
print(sum(li))