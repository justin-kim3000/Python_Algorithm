# '['이면 ']'로 끝나야 하며, '('이면 ')'로 끝이 나야한다.
# 아이디어 [로 시작하고 ]로 끝나는 경우 참.
# li = []
# li.append(input())

# print(li)

import sys
while True:
    sen = sys.stdin.readline().rstrip()
    flag = 0
    stack = []
    if sen == '.':
        break
    for i in sen:
        if i == "(" or i == "[": 
            stack.append(i)
        elif i == ")": 
            if not stack or stack[-1] == "[": 
                print("no")
                flag = 1
                break
            else:
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(": 
                print("no")
                flag = 1
                break
            else:
                stack.pop()
    if flag == 0:
        if not stack :
            print("yes")
        else:
            print("no")
