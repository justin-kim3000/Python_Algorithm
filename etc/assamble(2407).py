def factorial(N):
    if N == 1:
        return 1
    else:
        return factorial(N-1)*N
    
def fact2(N,M):
    for _ in range(M):
        return fact2(N-1)*N

N,M = map(int,input().split())

print(fact2(N,M)/factorial(M))