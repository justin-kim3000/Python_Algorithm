start, end = map(int, input().split())
counting = 1
# top to bottom
while(start != end):
    if end % 2 != 0 and str(end)[-1] == '1':
        end = int(str(end)-1)
        counting += 1
    elif end % 2 == 0:
        end /= 2
        counting += 1
    else:
        print(-1)
        break

print(counting)
