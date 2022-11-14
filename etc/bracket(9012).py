N = int(input())

for _ in range(N):
    temp = list(map(str, input()))
    if temp.count('(') == temp.count(')'):
        print("YES")
    else:
        print("NO")
