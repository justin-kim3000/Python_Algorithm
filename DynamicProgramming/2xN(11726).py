# bad - 런타임 에러
# 문제의 중요 포인트는 d(n) = d(n-1)+d(n-2)
# N = int(input())


# def data(N):
#     if N == 1:
#         return 1
#     if N == 2:
#         return 2
#     return data(N-1)+data(N-2)


# print(data(N) % 10007)

N = int(input())
res = [i+1 for i in range(N)]

if N <= 3:
    print(N)
else:
    for i in range(3, N):
        res[i] = res[i-1]+res[i-2]
    print(res[N-1] % 10007)
