N, M = map(int, input().split())
li1 = set()
li2 = set()

for _ in range(N):
    li1.add(input())

for _ in range(M):
    li2.add(input())
res = sorted(list(li1 & li2))
print(len(res))
for i in res:
    print(i)
