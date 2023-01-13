# N, M = map(int,input().split())


# for i in range(1,N): 
#     for j in range(1,i+1):
#         print(f"{j}",end= ' ')
#     print()
    
    
def dfs(start):
    global arr, N, M
    if len(arr)==M:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(start,N+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()


N,M=map(int,input().split())
arr = []

dfs(1)