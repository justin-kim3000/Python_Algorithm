# 1번 방법 - 시간초과
# import sys
# T = int(sys.stdin.readline())
# count_zero = 0
# count_one = 0


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


# for _ in range(T):
#     num1 = int(sys.stdin.readline())
#     fibonacci(num1)
#     print(count_zero, count_one)
#     count_zero = 0
#     count_one = 0

# 2번 방법 - 규칙 찾기
# 위 피보나치 식에 값을 1~9 까지 넣으보면 해당 값도 피보나치 수열을 따름을 알 수 있다.

T = int(input())
for _ in range(T):
    num = int(input())
    count_zero = 1
    count_one = 0
    if num == 0:
        print(count_zero, count_one)
    else:
        for _ in range(num):
            count_zero, count_one = count_one, count_one + count_zero
        print(count_zero, count_one)
