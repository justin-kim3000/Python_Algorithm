test = str(input())
alpabat = [0 for _ in range(97,123)]
for j in test:
    for i in range(97,123):
        if j == chr(i):
            alpabat[i-97] += 1
            
print(alpabat)