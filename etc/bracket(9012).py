# N = int(input())

# for _ in range(N):
#     temp = list(map(str, input()))
#     if temp.count('(') == temp.count(')'):
#         print("YES")
#     else:
#         print("NO")
N = int(input())

for _ in range(N):
    temp = list(map(str, input()))
    sumN = 0

    for i in temp:
        if i == '(':
            sumN += 1
        elif i == ')':
            sumN -= 1
        if sumN < 0:
            print("NO")
            break
    if sumN > 0:
        print("NO")
    elif sumN == 0:
        print("YES")
