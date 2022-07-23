import sys, collections, heapq
input = sys.stdin.readline
def find_load(start:int, end:int,reverse:bool) -> None:
    if start == end:
        cost_list[start] = 0
        return None
    costs,h = [100000 for _ in range(N + 1)], []
    costs[start] = 0
    for node, cost in edges[start]:
        costs[node] = cost
        heapq.heappush(h, (cost,node))
    while h:
        cost, node = heapq.heappop(h)
        if node == end:
            if reverse:
                cost_list[end] += cost
            else:
                cost_list[start] += cost
            return None
        for n,c in edges[node]:
            if cost + c < costs[n]:
                heapq.heappush(h,(cost+c, n))
                costs[n] = c+cost
N, M ,X = map(int, input().split())
cost_list = [0 for _ in range(N + 1)]
edges = collections.defaultdict(list)
for _ in range(M):
    a,b,c = map(int, input().split())
    edges[a].append([b,c])
for i in range(1,N+1):
    find_load(i,X,False)
for i in range(1,N+1):
    find_load(X,i,True)
print(max(cost_list))

