# bad - 런타임 에러
N = int(input())


def data(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return data(N-1)+data(N-2)


print(data(N) % 10007)
