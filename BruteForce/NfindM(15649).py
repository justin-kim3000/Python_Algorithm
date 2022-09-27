N, M = map(int, input().split())


for i in range(1, N+1):
    if M == 1:
        print(i)
        continue
    for j in range(1, N+1):
        if M == 2 and i != j:
            print(i, j)
            continue
        for k in range(1, N+1):
            if M == 3 and i != j and j != k and k != i:
                print(i, j, k)
                continue
            for l in range(1, N+1):
                if M == 4 and i != j and j != k and k != i and l != i:
                    print(i, j, k, l)
                    continue
