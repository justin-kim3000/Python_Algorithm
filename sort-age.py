countMember = int(input())
members = []
for i in range(countMember):
    age, name = map(str,input().split())
    members.append([int(age),i,name])

members.sort()
for i in range(len(members)):
    print("{} {}".format(members[i][0], members[i][2]))