# 변수 받음
N = int(input())
# 횟수 카운트 선언
count_blue = 0
count_white = 0
# 조건을 그래프로 받음
graph = [list(map(int, input().split())) for _ in range(N)]

# 쿼드 선언


def quad(x, y, n):
    # 그래프의 [x][y]값을 확인하겠다.
    check = graph[x][y]
    # 전역변수 사용하겠다 선언
    global count_white, count_blue
    # 범위 x부터 x+n까지 루프를 돈다
    for i in range(x, x+n):
        # 범위 y부터 y+n까지 루프를 돈다
        for j in range(y, y+n):
            # 만약 check값이 graph의 {ex)graph[0][2] = 0}과 같지 않다면
            # check값을 -1로 바꾸고 반복문을 정지(break)한다.
            if check != graph[i][j]:
                check = -1
                break
    # 만약 check값이 -1이라면 n을 2로 나눈다.
    if check == -1:
        n //= 2
        # 좌측 상단
        quad(x, y, n)
        # 우측 상단
        quad(x, y+n, n)
        # 좌측 하단
        quad(x+n, y, n)
        # 우측 하단
        quad(x+n, y+n, n)

    # 만약 check값이 1이면 count_blue를 1더함
    elif check == 1:
        count_blue += 1
    # 만약 check값이 0이면 count_blue를 1더함
    elif check == 0:
        count_white += 1

    # count한 값을 리턴
    return count_white, count_blue


# 각각 나눠주고
count_white, count_blue = quad(0, 0, N)

# 출력함
print(count_white)
print(count_blue)
