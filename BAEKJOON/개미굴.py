import collections
import sys

input_num = int(sys.stdin.readline())
ant = []
root = collections.defaultdict(dict)
for _ in range(input_num):
    tempt = root
    for room in sys.stdin.readline().split()[1:]:
        if room not in tempt:
            dic = {room : {}}
            tempt.update(dic)
        tempt = tempt[room]
def dfs(index : int,root:dict) -> None:
    if not root:
        return
    for key in sorted(root.keys()):
        print("-" * index * 2 + key)
        dfs(index + 1, root[key])

dfs(0, root)