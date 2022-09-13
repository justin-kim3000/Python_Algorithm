countMember = int(input())
members = []
for _ in range(countMember):
    members.append(list(map(str,input().split())))
for i in range(len(members)):
    members[i][0].sort()

print(members[1], members[0])