# 이해 부족.
import sys
input = sys.stdin.readline

n = int(input())
mtx = [list(map(int, input().split())) for _ in range(n)]
minus, zero, one = 0, 0, 0
print(mtx)

def check(x, y, length):
    global minus, zero, one
    for i in range(x, x + length):
        for j in range(y, y + length):
            if mtx[x][y] != mtx[i][j]:
                for a in range(3):
                    for b in range(3):
                        check(x + length // 3 * a, y + length // 3 * b, length // 3)
                        print(x + length // 3 * a, y + length // 3 * b, length // 3)
                return

    if mtx[x][y] == -1:
        minus += 1
    elif mtx[x][y] == 0:
        zero += 1
    elif mtx[x][y] == 1:
        one += 1

check(0, 0, n)
print(minus)
print(zero)
print(one)