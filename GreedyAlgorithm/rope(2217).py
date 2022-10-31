countRope = int(input())

liRope = []

for i in range(countRope):
    liRope.append(int(input()))

liRope = sorted(liRope, reverse=True)

temp = []
temp2 = 1
for i in liRope:
    temp.append(i * temp2)
    temp2 += 1

print(max(temp))

# Ropemean = sum(liRope)/countRope

# print(liRope)
