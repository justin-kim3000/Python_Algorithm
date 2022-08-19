from posixpath import split


N = int(input())
Numbers = list(map(int,input().split()))

print(min(Numbers), max(Numbers))


# for _ in range(N):
#     Numbers.append(number)