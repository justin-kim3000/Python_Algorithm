num = int(input())
hansu = 0

for n in range(1, num+1):
    # 두자리는 모두 한수
    if n <= 99:
        hansu += 1

    else:
        nums = list(map(int, str(n)))
        # 등비 수열
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1
print(hansu)
