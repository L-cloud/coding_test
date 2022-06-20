import sys, heapq
from collections import defaultdict
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph,h = defaultdict(dict),[]
for _ in range(E):
    a, b, c = map(int,sys.stdin.readline().split())
    if graph[a] and graph[a][b]:
        graph[a][b] = min(graph[a][b],c)
        continue
    graph[a][b] = c
cost = [float('inf') if i != start else 0 for i in range(V+1)]
for index, value in graph[start]:
    cost[index] = value
    heapq.heappush(h, (value,index))
while h:
    w, e = heapq.heappop(h)
    for index, value in graph[e]:
        if  w + value < cost[index]:
            cost[index] =  w + value
            heapq.heappush(h, (w + value, index))
for i in cost[1:]:
    if i == float('inf'):
        print('INF')
        continue
    print(i)
