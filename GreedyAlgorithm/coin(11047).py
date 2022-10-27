from audioop import reverse
# N: 동전의 종류, K: 동전의 합
N, K = map(int, input().split())
# 입력 값을 받는 곳
money = []
# 동전 개수 카운팅
sumMoney = 0

# 입력 값을 리스트에 넣음
for i in range(N):
    money.append(int(input()))

# 역순으로 치환
money.reverse()

# 높은 수 부터 나눈 몫을 카운트 함
for j in money:
    sumMoney += K//j
    # 나머지 반환
    K %= j

# 결과
print(sumMoney)
