N = int(input())

Nmatrix = []
# print(Nmatrix)
for _ in range(N):
    Nmatrix.append(list(map(int, input().split())))

# 람다 -> lambda Nmatrix: Nmatrix[0]


def sortlambda0(*a):
    a = Nmatrix
    return a[0]


# key = 어떤 기준으로 정렬할지 정함, reverse = True 내림차순으로 정렬
# sorted(정렬할 데이터, key=, reverse =)
Nmatrix = sorted(Nmatrix, key=lambda a: a[0])
Nmatrix = sorted(Nmatrix, key=lambda a: a[1])


last = 0
cnt = 0
for i, j in Nmatrix:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
