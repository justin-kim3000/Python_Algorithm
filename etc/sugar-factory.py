# 3키로 5키로 봉지가 있음.
# 최대한 적은 봉지를 이용해서 설탕을 옮기자!

sugar = int(input())

if sugar %5==0:
    print(sugar//5)
else:
    count = 0
    while(sugar>0):
        sugar -= 3
        count+=1
        if sugar %5==0:
            count += sugar//5
            print(count)
            break
        elif sugar == 1 or sugar ==2:
            print(-1)
            break
        elif sugar ==0:
            print(count)
            break

# count3 = 0
# count5 = sugar//5
# sugar=sugar%5
    
# if sugar <=4:
#     count3+=1
    
# if count5 == 0:
#     print("-1")
# else:
#     print(count3+count5)