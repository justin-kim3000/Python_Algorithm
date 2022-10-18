N = int(input())
score = list(map(int, input().split()))
temp = 0
max(score)

for i in score:
    temp += i/max(score)*100
print(temp/N)
