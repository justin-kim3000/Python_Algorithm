def pibona(N):
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        return pibona(N-1)+pibona(N-2)


for i in range(10):
    print(pibona(i))
