# N은 홀수
N = int(input())
li = []

for _ in range(N):
    li.append(int(input()))

print("----------------")
print(round(sum(li)/N))
print(li[round(len(li)/2-1)])

print()
print(max(li)-min(li))