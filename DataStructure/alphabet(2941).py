alphabetList = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

probAlpha = input()

for i in alphabetList:
    # replace(비교값, 변환값)
    probAlpha = probAlpha.replace(i, "@")

print(len(probAlpha))
