import sys
import collections
from typing import List
def dfs(visited:List[bool], graph:dict, node_list :List[int], dfs_list : List[int]) -> List :
    if not node_list:
        return dfs_list
    for node in sorted(node_list):
        if not visited[node]:
            visited[node] = True
            dfs_list.append(node)
            dfs(visited, graph, graph[node], dfs_list) 

    return dfs_list
def bfs(visited:List[bool], graph:dict, node_list :List[int], bfs_list : List[int]) -> List :
    if not node_list: # 완전 동떨어진 node가 start로 올 수 있음
        return bfs_list
    node_list = collections.deque(node_list)
    while node_list:
        node = node_list.popleft()
        for n in sorted(graph[node]):
            if not visited[n]:
                visited[n] = True
                bfs_list.append(n)
                node_list.append(n)
    return bfs_list
    


node, edge, start_node = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited_dfs, visited_bfs = [False] * (node + 1), [False] * (node + 1)
visited_dfs[start_node], visited_bfs[start_node] = True, True
dfs_list = dfs(visited_dfs, graph, graph[start_node],[start_node])
bfs_list = bfs(visited_bfs, graph, [start_node],[start_node])

print(" ".join(map(str,dfs_list)))
print(" ".join(map(str,bfs_list)))