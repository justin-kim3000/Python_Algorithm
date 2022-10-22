M = int(input())
N = int(input())
arr = []
for i in range(M, N+1):
    countNum = 0
    if i > 1:
        # 2부터 i 번 반복
        for j in range(2, i):
            # j로 나누워 떨어지면 소수가 아님으로 브레이크
            if i % j == 0:
                countNum += 1
                break
        if countNum == 0:
            arr.append(i)

if len(arr) == 0:
    print('-1')
else:
    print(sum(arr))
    print(min(arr))
