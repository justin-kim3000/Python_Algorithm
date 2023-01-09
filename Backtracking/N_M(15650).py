N, M = map(int,input().split())


for i in range(1,N): 
    for j in range(1,i+1):
        print(f"{j}",end= ' ')
    print()