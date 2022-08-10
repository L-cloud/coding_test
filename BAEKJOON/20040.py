import sys
input = sys.stdin.readline  
N, M = map(int,input().split())
parent = [i for i in range(N)]
def find(node :int) -> int:
    while node != parent[node]:
        node = parent[node]
    return node
def union(a:int,b:int) -> bool:
    p_a,p_b = find(a), find(b)
    if p_a == p_b:
        return True
    parent[max(p_a,p_b)] = parent[min(p_a,p_b)] 
    return False
answer = 0
for i in range(M):
    a,b = map(int, input().split())
    if not answer:
        if union(a,b):
            answer = i + 1
print(answer)
