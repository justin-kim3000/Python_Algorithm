from collections import deque
import sys

countCard = int(sys.stdin.readline())
useDeque = deque()
# time out.....
# cardList = list(map(int, range(1, countCard+1)))
# while 1:
#     if len(cardList) == 1:
#         print(cardList)
#         break
#     else:
#         cardList.pop(0)
#         cardList.append(cardList[0])
#         cardList.pop(0)
for i in range(countCard):
    useDeque.append(i+1)
while len(useDeque) > 1:
    useDeque.popleft()
    useDeque.append(useDeque.popleft())
print(useDeque.pop())
