M = int(input())
S = set()

for _ in range(M):
    com = input().split()

    if len(com) == 1:
        com0 = com[0]
    else:
        com0, com1 = com

    if com0 == "add":
        S.add(int(com1))

    elif com0 == "remove":
        if int(com1) in S:
            S.remove(int(com1))

    elif com0 == "check":
        if int(com1) in S:
            print(1)
        else:
            print(0)

    elif com0 == "toggle":
        if int(com1) in S:
            S.remove(int(com1))
        else:
            S.add(int(com1))

    elif com0 == "all":
        S = {i for i in range(1, 21)}

    else:
        S.clear()
