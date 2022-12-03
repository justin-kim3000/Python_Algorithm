A,B,C = map(int,input().split())

# time out!
# print(A**B%C)

# a**10 = (a**5)**2
def multi(a,b,c):
    if b == 1:
        return a%c
    elif b%2 ==0:
        return multi(a,b//2,c)**2%c
    else:
        return multi(a,b//2,c)**2*a%c
    
print(multi(A,B,C))