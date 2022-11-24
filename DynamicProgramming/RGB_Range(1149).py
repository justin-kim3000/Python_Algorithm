# RGB
# 조건 1 : 1번 집의 색은 2번 집 색과 다름
# 조건 2 : N번 집의 색은 N-1 집과 색이 다름
# 조건 3 : i번 집의 색은 i-1번, i+1 번 집과 색이 다름
# N -> 집의 수 // 집 칠하는 비용 주워짐
# 비용의 최솟값은?
# 각각 칠하는 빨 / 초 / 파 가격임

N = int(input())
N_list = []

for i in range(N):
    N_list.append(list(map(int, input().split())))

print(min(N_list[0]))
