def pibo(N):
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        return pibo(N-1)+pibo(N-2)


N = int(input())

print(pibo(N))

# 다른 풀이
n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a+b
print(a)
