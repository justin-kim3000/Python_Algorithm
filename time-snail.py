# Time out..
# upSnail, downSnail, total = map(int, input().split())
# now = downSnail
# day = 0
# while 1:
#     if now < total:
#         now -= downSnail
#     else:
#         print(day)
#         break
#     day += 1
#     now += upSnail

# 공식 이해 어려움
upSnail, downSnail, total = map(int, input().split())

day = (total - downSnail)/(upSnail-downSnail)
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)
