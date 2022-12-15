import sys
input = sys.stdin.readline
num = int(input())
arr = [0]*10000

# 해당 열의 숫자가 나오면 1을 더함
# 나온 횟수 만큼 더하기됨
for i in range(num):
    a = int(input())
    arr[a-1] += 1
    
# 행렬에 값이 0이 아니면 해당 값의 횟수 만큼 출력함
for i in range(10000):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i+1)
