sizeBorad = int(input())

matrix = [[i for i in range(sizeBorad)] for _ in range(sizeBorad)]

for i in matrix:
    i.append(map((str, input())))
    print(matrix)

print(matrix)
