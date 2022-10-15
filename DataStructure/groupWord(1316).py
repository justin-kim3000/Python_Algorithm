# N <=100
N = int(input())
groupWord = []
countNum = 0

for i in range(N):
    word = input()
    groupWord.append(word)
    if len(word) == 1:
        countNum += 1
    for i in range(1, len(word)):
        if word[0] != word[i]:
            countNum += 1

print(groupWord[0][:3])
