from math import sqrt

n = int(input())
# countNum = 0
# check = 0
# room = [i**2 for i in range(1, int(sqrt(n)+1))]
# print(room)

# 무식한 방법.. 오류 있음.
# for i in range(int(sqrt(n))-1, 0, -1):
#     check += room[i]
#     if n > check:
#         print(check, "n이 책이보다 크다")
#         countNum += 1
#     elif n == check:
#         print(check, "n이 책이랑 같다")
#         countNum += 1
#         break
#     elif n < check:
#         print(check, "n이 책보다 작다.")
#         check -= room[i]

# print(countNum)

# 브루트포스 - 모든 경우의수 다 때림


def fourSqu(n):
    if int(sqrt(n)) == sqrt(n):
        return 1
    for i in range(1, int(sqrt(n))+1):
        if int(sqrt(n-i**2)) == sqrt(n-i**2):
            return 2
    for i in range(1, int(sqrt(n))+1):
        # 뺀 이후의 범위에서 다시 검색
        for j in range(1, int(sqrt(n - i**2))+1):
            if int(sqrt(n-i**2-j**2)) == sqrt(n-i**2-j**2):
                return 3
    return 4


print(fourSqu(n))
