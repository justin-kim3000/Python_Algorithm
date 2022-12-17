N, K = map(int,input().split())
li = []
for _ in range(N):
    li.append(int(input()))
    
print(sum(li)/K)