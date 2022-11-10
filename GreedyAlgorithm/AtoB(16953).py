start, end = map(int, input().split())
counting = 1
# top to bottom
while(start != end):
    temp = end

    if end % 10 == 1:
        end //= 10
        counting += 1
    elif end % 2 == 0:
        end /= 2
        counting += 1
    # 위 if 문에 해당되지 않음
    if temp == end:
        print(-1)
        break
else:
    print(counting)
