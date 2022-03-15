import sys
import collections
from typing import List
def dfs(f_dic:dict,friend_list : List[int],visited:set ,f_num:int) -> None:
    if f_num == 5:
        print(1)
        exit()
    for f in friend_list:
        if f not in visited:
            visited.add(f)
            dfs(f_dic,f_dic[f],visited, f_num + 1)
            visited.remove(f)
num, relation = map(int, sys.stdin.readline().split())
r_dic = collections.defaultdict(list)
for _ in range(relation):
    a, b = map(int, sys.stdin.readline().split())
    r_dic[a].append(b)
    r_dic[b].append(a)

for key in r_dic.keys():
    visited = set([key])
    dfs(r_dic, r_dic[key],visited, 1)
print(0)