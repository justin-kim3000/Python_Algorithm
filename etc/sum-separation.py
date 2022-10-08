# 분해합 구하는 코드
# inputNumber = str(input())

# def sumSeparation(number):
#     temp = 0
#     for i in number:
#         temp += int(i)
#     print(temp+int(number))


# sumSeparation(inputNumber)

# 생성자 구하는 코드
inputNumber = int(input())
result = 0

for i in range(1, inputNumber+1):
    nums = list(map(int, str(i)))
    print(nums)
    result = sum(nums) + i
    print(result)
    if result == inputNumber:
        print(i)
        break
    if i == inputNumber:
        print(0)
