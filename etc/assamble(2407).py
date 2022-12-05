def factorial(N):
    if N == 1:
        return 1
    else:
        return factorial(N-1)*N

N,M = map(int,input().split())
    
print(int(factorial(N)/(factorial(N-M)*factorial(M))))