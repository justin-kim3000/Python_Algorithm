inputNumber = int(input())
answer = 1

for i in range(inputNumber):
    if inputNumber != 0:
        i += 1
        answer *= i
    elif inputNumber == 0:
        break

print(answer)

# def calculateFactorial(i):
#     result = 1

#     if i > 0:
#         result = i * calculateFactorial(i-1)
#     return result


# print(calculateFactorial(5))
