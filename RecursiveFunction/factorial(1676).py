
N = int(input())
count1 = 0


def factorial(N):
    if N == 0:
        return 1
    else:
        return N*factorial(N-1)


res = factorial(N)
for _ in range(len(str(res))):
    if res % 10 == 0:
        count1 += 1
        res //= 10
print(count1)
