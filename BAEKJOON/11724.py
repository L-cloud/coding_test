import sys
import collections

def bfs(n):
    node_list = collections.deque([n])
    while node_list:
        node = node_list.popleft()
        visited[node] = True
        for c in dic[node]:
            if not visited[c]:
                node_list.append(c)
                visited[c] = True
node, edge = map(int, sys.stdin.readline().split())
dic = collections.defaultdict(list)

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [False] * (node + 1)
island = -1 # 0번 인덱스 때문에
for key in range(node + 1):
    if not visited[key]:
        bfs(key)
        island += 1
    if sum(visited) == node + 1:
        break
print(island)