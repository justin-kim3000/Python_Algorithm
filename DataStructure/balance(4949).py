# '['이면 ']'로 끝나야 하며, '('이면 ')'로 끝이 나야한다.
# 아이디어 [로 시작하고 ]로 끝나는 경우 참.
# li = []
# li.append(input())

# print(li)

while True :
    a = input()
    stack = []

    if a == "." :
        break
    for i in a :
        print(i,end='\n\n')