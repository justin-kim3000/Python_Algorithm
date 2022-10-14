A = [1, 2, 3, 4, 5, 6, 7, 8]
B = [8, 7, 6, 5, 4, 3, 2, 1]
N = list(map(int, input().split()))


if A == N:
    print("ascending")
elif B == N:
    print("descending")
else:
    print("mixed")


# 다른 풀이(sorted 활용)
a = list(map(int, input().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')
