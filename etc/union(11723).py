S = []
M = int(input())
temp = []
for i in range(M):

    word, num = input().split()
        
    
    if word == 'add':
        if num not in S:
            S.append(num)
    if word == 'remove':
        if num in S:
            S.remove(num)
    if word == 'check':
        if num in S:
            temp.append(1)
        
            # print(1)
        else:
            temp.append(0)
            
            # print(0)
    if word == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.append(num)
    if word == 'all':
        S = []
        S = [i for i in range(1,21)]
    if word == 'empty':
        S = []
        
print(temp)