A = int(input())
B = int(input())
C = int(input())

multi = str(A*B*C)
multiList = list(multi)

for i in range(10):
    count = 0
    for j in multiList:
        if int(j) == i:
            count += 1
    print(count)   

# 심플하게
for i in range(10):
    print(multiList.count(str(i)))
   
# for i in range(len(str(multi)),0,-1):
#     print(multi//(10**(len(str(multi))-1)))
#     temp.append(multi//(10**(len(str(multi))-1)))
    
    
    