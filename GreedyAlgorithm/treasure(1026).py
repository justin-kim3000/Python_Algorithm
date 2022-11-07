N = int(input())

Alist = list(map(int, input().split()))
Blist = list(map(int, input().split()))

temp = 0

while(1):
    temp += min(Alist)*max(Blist)
    Alist.remove(min(Alist))
    Blist.remove(max(Blist))
    if len(Alist) == 0:
        break

print(temp)
