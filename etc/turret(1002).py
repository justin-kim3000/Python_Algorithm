import math

testT = int(input())

# x1,y1(x,y좌표),r1(목표물과 거리),x2,y2,r2

for _ in range(testT):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 원점 사이 거리
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)

    # 2개 교점일 경우
    if r1 == r2 and distance == 0:
        print(-1)
    elif r1 + r2 == distance or abs(r1-r2) == distance:
        print(1)
    elif abs(r1 - r2) < distance < (r1+r2):
        print(2)
    else:
        print(0)
