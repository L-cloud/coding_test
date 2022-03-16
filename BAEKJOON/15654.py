import sys
from typing import List
def dfs(index_list : List[int],tempt:int)-> None:
    if len(tempt) == b:
        print(*tempt)
        return
    for i,v in enumerate(num_list):
        if i not in index_list:
            index_list.append(i)
            tempt.append(v)
            dfs(index_list, tempt)
            tempt.pop()
            index_list.pop()

a, b = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
dfs([],[])

