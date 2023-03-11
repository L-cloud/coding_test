import sys, copy
from collections import defaultdict,deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N,M = map(int, input().split())
graph = defaultdict(dict)
for _ in range(N-1):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].update({b:c})
    graph[b].update({a:c})
def cnt(value:int,node:int) -> int:
    visited,q,answer = {node}, deque([node]),0
    while q:
        for _ in range(len(q)):
            n = q.pop()
            for k,v in graph[n].items():
                if value <= v and k not in visited:
                    answer += 1
                    q.appendleft(k)
                    visited.add(k)
    return answer
for _ in range(M):
    k,v = map(int, input().split())
    print(cnt(k,v))
