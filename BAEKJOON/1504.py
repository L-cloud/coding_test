[200~import sys,collections,heapq
        from typing import List
input = sys.stdin.readline
def find_load(start:int) -> List[int]:
    visited = [float('inf') for _ in range(N + 1)]
    visited[start] = 0
    h= [(0,start)]
    while h:
        cost, node = heapq.heappop(h)
        for destination, c in edges[node]:
            if cost + c < visited[destination]:
                visited[destination] = cost + c
                heapq.heappush(h,(cost+c,destination))
    return visited
N,E = map(int, input().split())
edges = collections.defaultdict(list)
for _ in range(E):
    a,b,c = map(int, input().split())
    edges[a].append([b,c])
    edges[b].append([a,c])
v1,v2 = map(int,input().split())
dist,v1_dist,v2_dist = find_load(1), find_load(v1), find_load(v2)
cost = min(dist[v1] + v1_dist[v2] + v2_dist[N], dist[v2] + v2_dist[v1] + v1_dist[N])
print(cost if cost != float('inf') else -1)

