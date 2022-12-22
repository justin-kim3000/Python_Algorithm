test = int(input())
# 0층에 i번째 -> i명
# 비율로 증가

for _ in range(test):
    k = int(input())
    t = int(input())
    temp = [i for i in range(1,t+1)]
    for i in range(k):
        for j in range(1,t):
            temp[j] += temp[j-1]
    print(temp[-1])