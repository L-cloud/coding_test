import sys
from typing import List
def dfs(num:List[int]):
    if len(tempt) == b:
        if tuple(tempt) in visited:
            return
        else:
            print(*tempt)
            visited.add(tuple(tempt[:]))
        return
    for i,v in enumerate(num):
        tempt.append(v)
        dfs(num[:i] + num[i + 1 :])
        tempt.pop()

a, b = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
tempt = []
visited = set()

dfs(num_list)