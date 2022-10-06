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
# 1부터 N까지 숫자를 리스트에 넣는다.
res = [i+1 for i in range(N)]
# 2이하의 숫자는 그대로 출력한다.(규칙 없음)
if N <= 2:
    print(N)
else:
    # 3부터 N까지 규칙에 맞춰 대입한다.
    for i in range(3, N):
        res[i] = res[i-1]+res[i-2]
    print(res[N-1] % 10007)
