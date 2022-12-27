T = int(input())

for _ in range(T):
    n = int(input())
    room = [list(map(int,input().split())) for _ in range(2)]
    for j in range(1, n):
        if j == 1:
            room[0][j] += room[1][j - 1]
            room[1][j] += room[0][j - 1]
        else:
            room[0][j] += max(room[1][j - 1], room[1][j - 2])
            room[1][j] += max(room[0][j - 1], room[0][j - 2])
    print(max(room[0][n - 1], room[1][n - 1]))
