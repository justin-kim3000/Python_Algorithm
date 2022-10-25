
M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue
    # 2부터 i 번 반복
    # 약수는 대칭임
    # ex)18
    # 1,2,3,6,9,18
    # 1*18 = 2*9 = 3*6
    for j in range(2, int(i**0.5)+1):
        # j로 나누워 떨어지면 소수가 아님으로 브레이크
        if i % j == 0:
            break
    else:
        print(i)
