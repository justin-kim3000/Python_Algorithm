# 셀프 넘버인 것을 전체에서 뺀다.
Numlist = set(range(1, 10001))
No_selfNum = set()

for i in Numlist:
    for j in str(i):
        i += int(j)
    No_selfNum.add(i)

Numlist = sorted(Numlist - No_selfNum)
for i in Numlist:
    print(i)
