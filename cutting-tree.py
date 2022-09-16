
# treeLength를 집에 가져가기 위해 절단기 최대 설정 높이?
# 아이디어 : treeHeight의 높이를 각각 1씩 잘라서 잘라진 합이 takeLength와 같은지 비교를 한다. 만약 같다면 break 그뒤 주어진 나무에서 가장 높은 높이를 출력한다.

treeCount, takeLength = map(int, input().split())

treeHeight = list(map(int, input().split()))

start, end = 1, sum(treeHeight)

while start <= end:
    mid = (start+end) // 2
    log = 0
    for i in treeHeight:
        if i > mid:
            log += i - mid

    if log >= takeLength:
        start = mid + 1
    else:
        end = mid - 1
print(end)
# ---------------------------------------
# 시간 안에 푼 코드.
# import sys
# input= sys.stdin.readline

# def binary_search(arr, start, end):
#     res = 0
#     while start <= end:
#         mid = (start+end) // 2
#         total = 0

#         for x in arr:
#             if x > mid:
#                 total+= x- mid

#         if total < m:
#             end = mid-1
#         else:
#             res = mid
#             start = mid +1
#     return res

# n , m = map(int,input().split())
# li = list(map(int,input().split()))

# r = binary_search(li, 0, max(li))
# print(r)

# -----------------------------------------------------
# treeHeight.index(max(treeHeight))-1
# print(treeHeight[treeHeight.index(max(treeHeight))]-1)
# print(treeHeight)

# while(1):
#     for i in range(len(treeHeight)):
#         if max(treeHeight) == treeHeight[i]:
#             print(treeHeight)

#             treeHeight[i]-1
#             count += 1
#         elif count == takeLength:
#             break
# print(max(treeHeight))
