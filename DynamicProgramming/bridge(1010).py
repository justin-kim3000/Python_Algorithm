def factorial(N):
    if N <= 1:
        return 1
    return N*factorial(N-1)


caseN = int(input())

for i in range(caseN):
    west, east = map(int, input().split())

    print(factorial(east)//(factorial(west)*factorial(east-west)))
