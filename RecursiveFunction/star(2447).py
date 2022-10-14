# 아이디어 : 1이면 별이 찍히고, 0일 경우 빈칸으로 처리한다.
# 0인 행렬을 만듬
# 별은 *** * * ***로 찍힘.
# 최소 단위는 '***' '* *' '***'
#

N = int(input())
room = [[0 for _ in range(N)] for _ in range(N)]


def star(n):
    global room

    if n == 3:
        room[0][:3] = room[2][:3] = [1]*3
        room[1][:3] = [1, 0, 1]
        return

    # 3 간격으로 패턴이 반복
    split_ = n//3
    star(split_)
    # x,y의 3x3 행렬을 만듬.
    for i in range(3):
        for j in range(3):
            # 위에 있는 [1,0,1]의 0 부분이므로 그냥 넘긴다.
            if i == 1 and j == 1:
                continue
            # think more! splic_ = 3,9값을 stack 형식으로 대입
            for k in range(split_):
                room[split_*i+k][split_*j:split_*(j+1)] = room[k][:split_]


star(N)
# 행렬에 행을 출력
for i in room:
    # 행의 열을 출력
    for j in i:
        # 만약 j가 참(1)이라면 별
        if j:
            print('*', end='')
        # 아니면 빈칸
        else:
            print(' ', end='')
    print()
