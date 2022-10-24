# import sys
# N, M = map(int, sys.stdin.readline().split())
# weight = {}
# for i in range(N):
#     W, V = map(int, sys.stdin.readline().split())
#     weight[W] = V

# print(weight)

# for key in weight:
#     print(key)


# n: 물품의 수, k: 가방에 넣을 수 있는 최대 무게
n, k = map(int, input().split())
# 비교 배낭
pock = [[0] * (k+1) for _ in range(n+1)]
m = [[0, 0]]

for i in range(n):
    # w: 물건 무게, v: 물건 가치
    w, v = map(int, input().split())
    m.append([w, v])

# [0,0]뒤에 붙으므로 범위를 1부터 n+1로 정함
for i in range(1, n+1):
    # 무게
    w = m[i][0]
    # 가치
    v = m[i][1]
    # k : 최대무게
    for j in range(1, k+1):
        # 최대무게 보다 무거우면 물품수를 뺌
        if j < w:
            pock[i][j] = pock[i-1][j]
        # 최대무게보다 적을 경우, 가치와 무게중 최대값
        else:
            pock[i][j] = max(pock[i-1][j-w] + v, pock[i-1][j])
print(pock[n][k])
