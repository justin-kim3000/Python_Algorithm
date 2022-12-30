# N은 홀수
from collections import Counter
import sys
N = int(sys.stdin.readline())
li = []

for _ in range(N):
    li.append(int(sys.stdin.readline()))

print("----------------")
print(round(sum(li)/N))
print(li[round(len(li)/2-1)])

cnt = Counter(li).most_common(2)

if len(li) >1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[0][1])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])


print()
print(max(li)-min(li))