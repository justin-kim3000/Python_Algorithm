# 대소문자 변환, (잠시 넣어둘곳 만들것)
# from curses.ascii import islower, isupper

# word = input()
# result = ""
# for i in word:
#     if i.isupper():
#         result += i.lower()
#     elif i.islower():
#         result += i.upper()

# print(result)

# -------------------------------------------

# use - Dictionary
# score = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,

#          'B+': 3.3, 'B0': 3.0, 'B-': 2.7,

#          'C+': 2.3, 'C0': 2.0, 'C-': 1.7,

#          'D+': 1.3, 'D0': 1.0, 'D-': 0.7,

#          'F': 0.0}

# getScore = str(input())
# print(score[getScore])

# -------------------------------------------

# try / except 사용 (end of file)
# while(1):
#     try:
#         print(input())
#     except EOFError:
#         break

# -------------------------------------------

inputNumber = int(input())
temp = []
for i in range(inputNumber):
    word = list(map(str, input()))
    temp.append(word)
print(temp)
