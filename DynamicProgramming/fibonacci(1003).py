# 1번 방법 - 시간초과
import sys
T = int(sys.stdin.readline())
count_zero = 0
count_one = 0


def fibonacci(N):
    global count_zero, count_one
    if N == 0:
        count_zero += 1
        return 0
    elif N == 1:
        count_one += 1
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)


for _ in range(T):
    num1 = int(sys.stdin.readline())
    fibonacci(num1)
    print(count_zero, count_one)
    count_zero = 0
    count_one = 0
