A, B = input().split()

changeA = A[-1]+A[1]+A[0]
changeB = B[-1]+B[1]+B[0]

if changeA > changeB:
    print(changeA)
else:
    print(changeB)

# tip - 뒤집기 가능
changeA = A[::-1]
