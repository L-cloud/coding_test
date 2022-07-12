import sys,collections,heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
buses = collections.defaultdict(list) # 출발 -> 도착 동일한 버스가 있는가?
for _ in range(M):
    start, end, cost = map(int, input().split())
    buses[start].append([end,cost])
start, end = map(int,input().split())
cost_list = [float('inf') if i != start else 0 for i in range(N + 1)]
visited = collections.defaultdict(list)
h = []
for e, c in buses[start]: # heapq 초기화
    heapq.heappush(h,(c,e))
    cost_list[e] = min(c,cost_list[e]) # 1 -> 2 가 여러개 있을 수 있음
    visited[e] = [start]
while h:
    cost, d= heapq.heappop(h)
    if d == end:
        print(cost)
        break
    for destination, c in buses[d]:
        if c + cost < cost_list[destination]:
            visited[destination]  = visited[d][:]
            visited[destination].append(d)
            cost_list[destination] = c + cost
            heapq.heappush(h,(c+cost, destination))
print(len(visited[end]) + 1)
print(*visited[end], end)