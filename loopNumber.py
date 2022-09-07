N = int(input())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)


while (True):
    A, B = map(int, input().split())

    if (A and B) == 0:
        break
    else:
        print(A+B)
