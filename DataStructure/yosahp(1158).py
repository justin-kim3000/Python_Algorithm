N, K = map(int, input().split())

for i in range(1, N):
    if K*i <= N:
        print(f'{K*i},', end=' ')
    elif N-K*i < 0:
        print(f'{-(N-K*i)},', end=' ')
    else:
        print(f'{N-K*i},', end=' ')
