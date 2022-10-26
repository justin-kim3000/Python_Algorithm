N = input()
M = input()

temp = str()
countN = 0
# for i in range(1, len(N)+1):
#     if N[:i] in M:
#         countN += 1
#         print(countN)

for i in range(1, len(N)+1):
    print(N[:i])

for i in range(1, len(N)+1):
    print(N[:-i])
