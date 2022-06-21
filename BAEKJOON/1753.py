import sys, heapq
from collections import defaultdict
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph,h = defaultdict(list),[]
for _ in range(E):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
cost = [float('inf') if i != start else 0 for i in range(V+1)]
for index, value in graph[start]:
    cost[index] = min(value,cost[index])
    heapq.heappush(h, (value,index))
visited = [False for _ in range(V+1)]
while h:
    w, e = heapq.heappop(h)
    if visited[e]: # 이미 방문
        continue
    for index, value in sorted(graph[e], key = lambda x:x[1]):
        if  w + value < cost[index]:
            cost[index] =  w + value
            heapq.heappush(h, (w + value, index))
    visited[e] = True
for i in cost[1:]:
    if i == float('inf'):
        print('INF')
        continue
    print(i)
