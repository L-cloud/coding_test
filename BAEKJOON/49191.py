from typing import List,Dict, Set
from collections import defaultdict
def solution(n:int, results:List[List[int]]) -> int:
    v, l = defaultdict(set), defaultdict(set)
    visit_v = [False for _ in range(n+1)]
    visit_l = [False for _ in range(n+1)]
    for win, lose in results:
        v[win].add(lose)
        l[lose].add(win)
    for i in range(1,n+1):
        dfs(v,i,visit_v)
        dfs(l, i, visit_l)
    return sum([1 if (len(v[i]) + len(l[i])) == n-1 else 0 for i in range(1,n+1)])
def dfs(d:Dict[Set,int], index:int,visit:List[bool]) -> Set:
    if not d[index]:
        visit[index] = True
        return set()
    for i in list(d[index]):
        d[index] |= dfs(d,i,visit) if not visit[i] else d[i]
    visit[index] = True
    return d[index]

        
