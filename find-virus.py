# countComputer = int(input())
# connectComputer = int(input())
# connectList = []
# countVirus = 0
# temp = []
# for i in range(connectComputer):
#     connectList.append(list(map(int,input().split())))

# for i in range(len(connectList)):
#     if 1 in connectList[i]:
#         temp.append(connectList[i][1])
#         countVirus+=1
#     for j in range(len(temp)):
#         if temp[j] in connectList[i]:
#             countVirus +=1
    
# print(countVirus)
# print(temp)

n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] 

print(graph)
visited=[0]*(n+1)
print(visited)
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    
    graph[b]+=[a] # b에 a 연결 -> 양방향