
# treeLength를 집에 가져가기 위해 절단기 최대 설정 높이?
# 아이디어 : treeHeight의 높이를 각각 1씩 잘라서 잘라진 합이 takeLength와 같은지 비교를 한다. 만약 같다면 break 그뒤 주어진 나무에서 가장 높은 높이를 출력한다.

# treeCount, takeLength = map(int, input().split())
treeCount, takeLength = 4, 7

# treeHeight = list(map(int, input().split()))
treeHeight = [20, 15, 10, 17]
count = 0
print(treeHeight)


start, end = 1, max(treeHeight)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2

    log = 0  # 벌목된 나무 총합
    for i in treeHeight:
        if i >= mid:
            log += i - mid

    # 벌목 높이를 이분탐색
    if log >= takeLength:
        start = mid + 1
    else:
        end = mid - 1
print(end)


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
