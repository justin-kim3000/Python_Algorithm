# N x N에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# 1<= N <15
# d

n = int(input())
result = 0


# 퀸을 놓은 후 그 이후의 줄에 대해서만 불가능한 칸 체크
def visit(x, y, in_visited):
    tmp_visited = [visi[:] for visi in in_visited]
    for i in range(1, n-x):
        tmp_visited[x+i][y] = True  # 아래 방향 체크
        if 0 <= y-i < n:
            tmp_visited[x+i][y-i] = True    # 왼쪽 아래 대각선 체크
        if 0 <= y+i < n:
            tmp_visited[x+i][y+i] = True    # 오른쪽 아래ㄹㅇ 대각선 체크
    return tmp_visited