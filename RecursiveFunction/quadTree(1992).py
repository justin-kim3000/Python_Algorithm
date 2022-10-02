# 자식이 4개인 트리

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]


def quad(x, y, n):
    check = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n //= 2
        quad(x, y, n)
        quad(x, y+n, n)
        quad(x+n, y, n)
        quad(x+n, y+n, n)
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


quad(0, 0, N)
