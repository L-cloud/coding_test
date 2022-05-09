import sys,collections

# 어디서 런타임 에러가 나는거지..?

class Node:
    def __init__(self,left,right) -> None:
        self.left = left
        self.right = right
        self.left_num = 0
        self.right_num = 0
        self.location = 0

def dfs_num(left_,right_,node):
    if node.left != -1:
        node.left_num = dfs_num(left_+1,right_,dic[node.left]) + 1
    if node.right != -1:
        node.right_num = dfs_num(left_,right_+1,dic[node.right]) + 1
    return node.left_num + node.right_num

def dfs_location(left, location, node): # 위치 정하는 거
    if left: # 왼쪽으로 옴
        node.location = location - node.right_num - 1
    else: # 오른쪽으로 옴
        node.location = location + 1 + node.left_num
    if node.left != -1:
        dfs_location(True,node.location, dic[node.left])
    if node.right != -1:
        dfs_location(False,node.location, dic[node.right])

N = int(sys.stdin.readline().rstrip())
if N == 1:
    print(1, 1)
    exit()
dic = {}
is_parent = [False for _ in range(N+1)]
for _ in range(N):
    a,b,c = map(int, sys.stdin.readline().split())
    if a not in dic: # 부모 노드가 더 늦게 나올 수 있음
        node1 = Node(b,c)
        dic[a] = node1
    if b not in dic:
        node2 = Node(-1,-1)
    else: 
        node2 = dic[b]
    if c not in dic:
        node3 = Node(-1,-1)
    else:
        node3 = dic[c]
    dic[a].left = b
    dic[a].right = c
    if b != -1:
        dic[b] = node2
        is_parent[b] = True
    if c != -1:
        dic[c] = node3
        is_parent[c] = True
root = dic[is_parent[1:].index(False) + 1]
dfs_num(0,0,root)
root.location = root.left_num
if root.left != -1:
    dfs_location(True,root.location,dic[root.left])
if root.right != -1:
    dfs_location(False,root.location,dic[root.right])
answer, level = [1,1], 0

q = collections.deque([root])

while q:
    lq = sorted(q ,key = lambda x : x.location)
    level += 1
    if answer[1] < lq[-1].location - lq[0].location + 1:
        answer[1] = lq[-1].location - lq[0].location + 1
        answer[0] = level
    for _ in range(len(q)):
        node = q.pop()
        if node.left != -1:
            q.appendleft(dic[node.left])
        if node.right != -1:
            q.appendleft(dic[node.right])

print(answer[0], answer[1])