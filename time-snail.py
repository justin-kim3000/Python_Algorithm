# Time out..
upSnail, downSnail, total = map(int, input().split())
now = downSnail
day = 0
while 1:
    if now < total:
        now -= downSnail
    else:
        print(day)
        break
    day += 1
    now += upSnail
