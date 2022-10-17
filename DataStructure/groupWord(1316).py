N = int(input())
# 모두가 해당될 경우
countNum = N

for _ in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            countNum -= 1
            break

print(countNum)
