N = int(input())

Nmatrix = [[] for _ in range(N)]

# print(Nmatrix)
for i in range(N):
    Nmatrix[i].append(list(map(int, input().split())))

print(Nmatrix)
