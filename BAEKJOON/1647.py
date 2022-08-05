import sys
input = sys.stdin.readline
N,M = map(int,input().split()) # N개의 집, M개의 길
p = [i for i in range(N+1)]
edges = [list(map(int,input().split())) for _ in range(M)]
max_cost,cost = 0,0
edges.sort(key = lambda x: x[2],reverse= True)
branchs = 0
def find(node:int) -> int:
    if p[node] != node:
        node = find(p[node])
    return node
def union(a:int, b:int) -> bool:
    p_a, p_b = find(a),find(b)
    if p_a == p_b: # 이미 연결됨
        return False
    if p_a < p_b: 
        p[p_b] = p_a
    else:
        p[p_a] = p_b
    return True
while branchs < N - 1:
    a,b,c = edges.pop()
    if union(a,b):
        cost += c
        max_cost = max(c,max_cost)
        branchs += 1
print(cost - max_cost)
