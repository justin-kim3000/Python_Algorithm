from collections import deque


N, K = map(int, input().split())

Number1 = deque([i for i in range(1,N+1)])
print('<',end='')
while(Number1):
    for _ in range(K-1):
        Number1.append(Number1[0])
        Number1.popleft()
    print(Number1.popleft(),end='')
    if Number1:
        print(', ',end='')

print('>',end='')
