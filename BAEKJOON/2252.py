import graphlib
import sys,collections
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def check(node:int):
    for p in graph[node]:
        if p not in order:
            check(p)
    if node not in order:
        order.update({node:True})
N,M = map(int,input().split())
graph = collections.defaultdict(set)
order = collections.OrderedDict()
for _ in range(M):
    a,b = map(int,input().split())
    graph[b].add(a) # b 앞에 a가 서야함
for i in range(1,N + 1):
    check(i)

print(*order.keys())


