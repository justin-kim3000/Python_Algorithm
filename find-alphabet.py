from operator import index


inputWords = str(input())
alphabet = str("abcdefghijklmnopqrstuvwxyz")
for i in alphabet:
    print(inputWords.find(i), end=' ')
