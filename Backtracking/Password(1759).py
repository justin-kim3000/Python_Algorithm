# L, C = map(int, input().split())

# password = list(map(str, input().split()))

# password = sorted(password)
# print(password)

# end = ""
# for i in range(C-L, C):
#     end += password[i]

# while(1):
#     temp = ""
#     for i in range(L):
#         temp += password[i]
#     print(temp)
#     if temp == end:
#         break

# othrer

L, C = map(int, input().split())

password = list(map(str, input().split()))
password = sorted(password)

vowels = ['a', 'e', 'i', 'o', 'u']
sol = []


def back_tracking(count, idx):
    if count == L:
        vo = 0
        co = 0
        for i in range(L):
            if sol[i] in vowels:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(sol))
        return
    for i in range(idx, C):
        sol.append(password[i])
        back_tracking(count+1, i+1)
        sol.pop()


back_tracking(0, 0)
