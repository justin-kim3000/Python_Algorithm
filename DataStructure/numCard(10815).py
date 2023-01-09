N = int(input())
N_li = list(map(int,input().split()))
M = int(input())
M_li = list(map(int,input().split()))

for i in range(M):
    for j in range(N):
        if N_li[j] == M_li[i]:
            print(1,end=' ')
        else:
            continue
        print(0,end=' ')
        