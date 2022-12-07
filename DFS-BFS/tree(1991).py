N= int(input())
tree = {}

for _ in range(N):
    root, left, right = map(str,input().split())
    tree[root] =[left,right]
    
def adv(root):
    if root != '.':
        print(root, end='')
        adv(tree[root][0])
        adv(tree[root][1])
        
def mid(root):
    if root != '.':
        mid(tree[root][0])
        print(root, end='')
        mid(tree[root][1])
        
def end(root):
    if root != '.':
        end(tree[root][0])
        end(tree[root][1])
        print(root, end='')

adv('A')
print()
mid('A')
print()
end('A')