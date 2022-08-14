import sys,collections
sys.setrecursionlimit(10**9)
def check(start:int, current:int,visited:set):
    while orders[current]:
        node = orders[current].pop()
        if node in visited:
            print(0)
            exit()
        if node not in v:
            visited.add(node)
            check(start,node,visited)
    if current not in v:
        v.update({current:1})
        visited.remove(current)
input = sys.stdin.readline
N, M = map(int,input().split())
orders =  collections.defaultdict(set)
for _ in range(M):
    order = list(map(int,input().split()))[1:]
    for index,value in enumerate(order):
        for v in order[:index]:
            orders[value].add(v)
v = collections.defaultdict()
for node in range(1,N + 1):
    check(node,node,set([node]))

print("\n".join([str(key) for key in v]))

