# 다시 처음부터 생각해보자
import sys,heapq, collections
TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    n,d,c = map(int, sys.stdin.readline().split())
    visited = [float('inf') for _ in range(n + 1)]
    visited[c] = 0
    h = [(0,c)]
    graph = collections.defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((s,a))
    while h:
        time, node = heapq.heappop(h)
        for t,v in graph[node]:
            if time + t < visited[v]:
                visited[v] = time + t
                heapq.heappush(h,(time+t,v))
    result = [i for i in visited if i != float('inf')]
    print(len(result), max(result))
    

    

                    

        

