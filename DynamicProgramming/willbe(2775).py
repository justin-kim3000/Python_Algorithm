# test = int(input())
# 0층에 i번째 -> i명
# 비율로 증가

def sol(n):
    if n == 1:
        return 1
    return n+sol(n-1)

print(sol(10))
temp = [a for a in range(1,10)]

print(temp)
# for _ in range(test):
#     k = int(input())
#     t = int(input())
    