from operator import index


S = str(input())
alphabet = str("abcdefghijklmnopqrstuvwxyz")
for i in alphabet:
    print(S.find(i), end=' ')
