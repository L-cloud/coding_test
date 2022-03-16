import sys
from typing import List
a, b = map(int, sys.stdin.readline().split())
total = []
def dfs(start : int, tempt: List[int]):
    if len(tempt) == b:
        total.append(tempt[:])
        return
    for i in range(start, a+1):
        tempt.append(i)
        dfs(i, tempt)
        tempt.pop()


dfs(1,[])

for i in total:
    print(*i)