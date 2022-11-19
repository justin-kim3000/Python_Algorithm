L, C = map(int, input().split())

password = list(map(str, input().split()))

password = sorted(password)
print(password)

end = ""
for i in range(C-L, C):
    end += password[i]

while(1):
    temp = ""
    for i in range(L):
        temp += password[i]
    print(temp)
    if temp == end:
        break
