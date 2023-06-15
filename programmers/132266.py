from typing import List
from collections import defaultdict
from heapq import heappush,heappop
def solution(n:int, roads:List[List[int]], sources:List[int], destination:int) -> List[int]:
    v = [float('inf') for _ in range(n+1)]
    v[destination] = 0
    r = defaultdict(list)
    for a,b in roads:
        r[a].append(b)
        r[b].append(a)
    q = [(0,destination)]
    answer = []
    while q:
        d, node = heappop(q)
        for n in r[node]:
            if d + 1 < v[n]:
                v[n] = d + 1
                heappush(q,(v[n],n))
    return [v[s] if v[s] != float('inf') else -1 for s in sources]
