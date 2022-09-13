count = int(input())
temp = 1
floor = room = 0

for _ in range(count):
    floors, rooms, guset = map(int, input().split())
    if temp != guset:
        for _ in range(1,rooms+1):
            for _ in range(1,floors+1):
                temp += 1
                floor += 1
            room += 1
                    
    else:
        if room >=10:
            print(str(floor)+str(room))
            break
        else:
            print(str(floor)+"0"+str(room))
            break
