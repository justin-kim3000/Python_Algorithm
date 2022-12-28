K = int(input())
li = []
for _ in range(K):
    li.append(int(input()))
    
for i in range(len(li)):
    if li[i] == 0:
        li[i-1] = 0
print(sum(li))