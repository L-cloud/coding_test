import sys
input = sys.stdin.readline
class Node():
    def __init__(self,node:int) -> None:
        self.num = node
        self.childs = []
        self.erase = False
N = int(input())
nodes = list(map(int, input().split()))
tree = {}
for index,p in enumerate(nodes):
    if tree.get(index):
        node = tree.get(index)
    else:
        node = Node(index)
        tree.update({index:node})
    if parent := tree.get(p):
        parent.childs.append(node)
    else:
        parent = Node(p)
        tree.update({p:parent})
        parent.childs.append(node)
erase = int(input())
tree[erase].erase = True
cnt = [0]
def dfs(N:Node) -> bool:
    if not N or N.erase:
        return True
    flag = True
    for child in N.childs:
        if not dfs(child):
            flag = False
    if flag:
        cnt[0] += 1
    return False
dfs(tree[-1].childs[0])
print(*cnt)
