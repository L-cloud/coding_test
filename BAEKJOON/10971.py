import sys,collections
N = int(sys.stdin.readline())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
visited = collections.defaultdict(set)
min_cost = float('inf')
def travel(start:int,L : set[int], cost:int):
    if len(visited[start]) == N and L[start]:
        return True, cost + L[start]
    tempt_list = [[i,v] for i,v in enumerate(L)]
    for i,v in sorted(tempt_list, key = lambda x: x[1], reverse=True): # 인덱스 유지 + 가격 낮은 순으로 정렬
        if i not in visited[start] and v: #방문 안 했고, 갈 수 있으면
            visited[start].add(i)
            b, c = travel(start,graph[i],cost + v) # boolean, cost
            if b:
                return b, c # 최소값들로 순회를 끝냄 그럼 return
            visited[start].remove(i)
    return False, 0

for i in range(N):
    visited[i].add(i)
    b,cost=travel(i,graph[i],0)
    if b:
        min_cost = min(cost, min_cost)

print(min_cost) 

