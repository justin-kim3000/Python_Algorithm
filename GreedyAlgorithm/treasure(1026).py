N = int(input())

Alist = list(map(int, input().split()))
Blist = list(map(int, input().split()))

temp = 0

for _ in range(len(Alist)):
    temp += min(Alist)*max(Blist)
    Alist.remove(min(Alist))
    Blist.remove(max(Blist))

print(temp)
