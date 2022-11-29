n = int(input())
num_li = []

for i in range(n):
    num_li.append(list(map(int,input().split())))
    
for i in range(1,n):
    for j in range(len(num_li[i])):
        if j == 0:
            num_li[i][j] = num_li[i][j]+num_li[i-1][j]
        elif j == len(num_li[i])-1:
            num_li[i][j]= num_li[i][j]+num_li[i-1][j-1]
        else:
            num_li[i][j]= max(num_li[i-1][j-1],num_li[i-1][j])+num_li[i][j]
print(max(num_li[n-1]))