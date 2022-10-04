# 1번 방법 - 시간초과
import sys
T = int(sys.stdin.readline())
# 변수 입력
count_zero = 0
count_one = 0

# 피보나치 수열 함수


def fibonacci(N):
    global count_zero, count_one
    # N == 0 일 경우 count_zero에 1을 더한다.
    if N == 0:
        count_zero += 1
        return 0
    # N == 1 일 경우 count_one에 1을 더한다.
    elif N == 1:
        count_one += 1
        return 1
    # 재귀 함수를 활용해 피보나치 수열을 반환한다.
    else:
        return fibonacci(N-1) + fibonacci(N-2)


# T번 반복
for _ in range(T):
    # 피보나치 숫자 입력
    num1 = int(sys.stdin.readline())
    fibonacci(num1)
    print(count_zero, count_one)
    # 재활용을 위해 0으로 초기화 한다.
    count_zero = 0
    count_one = 0

# 2번 방법 - 규칙 찾기
# 위 피보나치 식에 값을 1~9 까지 넣으보면 해당 값도 피보나치 수열을 따름을 알 수 있다.
# 반복 횟수 입력
T = int(input())
# T번 반복
for _ in range(T):
    # num 번째 피보나치 값
    num = int(input())
    # 시작값 선언
    count_zero = 1
    count_one = 0
    # 0일 경우
    if num == 0:
        print(count_zero, count_one)
    # 이외에
    else:
        # num번 반복
        for _ in range(num):
            # 현재 count_zero는 이전 counrt_one과 값이 같으며,
            # 현재 count_one의 값은 이전 'count_one and count_zero'의 합이다.
            count_zero, count_one = count_one, count_one + count_zero
        print(count_zero, count_one)
