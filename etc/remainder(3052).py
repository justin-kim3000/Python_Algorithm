countlist = []
countNum = 0

for i in range(10):
    countlist.append(int(input()) % 42)

print(len(set(countlist)))
