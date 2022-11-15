N = list(map(str, input()))
M = list(map(str, input()))

print(N)
print(M)
counting = 0
for i in N:
    for j in range(len(M)):
        if i == M[j]:
            del M[:j]
            counting += 1

print(counting)
