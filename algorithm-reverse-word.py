inputWords = int(input())

for i in range(inputWords):
    words = list(input().split())
    temp = []
    for word in words:
        # [::-1]역순으로 나열
        temp.append(word[::-1])
        answer = " ".join(temp)
    print(answer)

# # revers all words
# for i in range(N):
#     words = str(input())
#     reverse_words = ""
#     for j in words:
#         reverse_words = j + reverse_words
#     print(reverse_words)
