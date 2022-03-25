import sys
import collections


node_num = int(sys.stdin.readline())

graph = collections.defaultdict(list)

for _ in range(node_num - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
graph[0].extend([1,1]) # len(graph[node] -1 때문에 두번
graph[1].append(0) # len(graph[node] -1) 때문에 하나 추가
que = collections.deque([0])
user_bfs = list(map(int, sys.stdin.readline().split()))
index = 0
while que:
    node = que.pop()
    for _ in range(len(graph[node]) - 1): # 부모노드까지 graph에 append되어 있어서
        if user_bfs[index] in graph[node]: #여기가 문제겠지
            que.appendleft(user_bfs[index])
            index += 1
            continue
        else:
            print(0)
            exit()

print(1)