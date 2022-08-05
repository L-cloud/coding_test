import sys,collections,heapq

input = sys.stdin.readline


V,E = map(int, input().split())
v = [False for _ in range(V + 1)]
cnt,s = 0,0
edges = collections.defaultdict(list)

for _ in range(E):
    a,b,c = map(int, input().split())
    edges[a].append([b,c])
    edges[b].append([a,c])
h = [(0,1)]
while cnt < V:
    cost, node = heapq.heappop(h)
    if not v[node]:
        v[node] = True
        cnt += 1
        s += cost
        for n,c in edges[node]:
            heapq.heappush(h,(c,n))
print(s)