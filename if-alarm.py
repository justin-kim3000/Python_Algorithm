H, M = input().split()

H = int(H)
M = int(M)

Setting = 45
if H!=0 and M-Setting <0:
    print(H-1,M+60-Setting)
elif H==0 and M-Setting <0:
    H = 23
    print(H,M+60-Setting)
else:
    print(H,M-Setting)