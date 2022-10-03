N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
count_zero = 0
count_one = 0
count_min = 0


def quad(x, y, n):
    check = graph[x][y]
    global count_zero, count_min, count_one
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != graph[i][j]:
                # 3등분
                for k in range(3):
                    for l in range(3):
                        quad(x+k*n//3, y+l*n//3, n//3)
                return

    if check == -2:
        n //= 3
        quad(x, y, n)
        quad(x, y+n, n)
        quad(x+n, y, n)
        quad(x+n, y+n, n)

    elif check == 1:
        count_one += 1
    elif check == 0:
        count_zero += 1
    elif check == -1:
        count_min += 1


quad(0, 0, N)

print(count_min)
print(count_zero)
print(count_one)
