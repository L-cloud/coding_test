import sys
import collections

def bfs(node:int, time : int) -> None:
    if node == brother:
        print(time)
        stack = []
        while path[node] != -1: # 미친 이색기 0...
            stack.append(node)
            node = path[node]
        stack.reverse()
        print(me, *stack)
        exit()
    if 0 <= node - 1 and not node - 1 in visited:
        candi.appendleft(node -1)
        visited.add(node -1)
        path[node -1] = node
    if node + 1 <= brother and node + 1 not in visited:
        candi.appendleft(node + 1)
        visited.add(node + 1)
        path[node + 1] = node
    if node * 2 <= brother + 1 and node * 2 not in visited:  
        candi.appendleft(node * 2)
        visited.add(node * 2)
        path[node * 2] = node
me, brother = map(int, sys.stdin.readline().split())
time = -1
candi = collections.deque([me])
visited = set([me])
path = {me : -1}
while True:
    time += 1
    for i in range(len(candi)):
        stack = candi.pop()
        bfs(stack, time)

