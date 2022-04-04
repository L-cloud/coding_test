import sys, collections

sys.setrecursionlimit(100,0000)


def make_tree(node:int)->None:
    for i in graph[node]:
        if not parent_list[i]:
            parent_list[i] = node
            make_tree(i)

N = int(sys.stdin.readline())

parent_list = [False for _ in range(N+1)]
parent_list[1] = True
graph = collections.defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


make_tree(1)
for i in range(2, N +1):
    print(parent_list[i])