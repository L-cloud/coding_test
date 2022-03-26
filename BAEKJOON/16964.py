import sys
import collections

def dfs(i : int) -> None:
    if visited[i]:
        return
    stack.append(i)
    visited[i] = True
    for node in graph[i]:
        if not visited[node]:
            dfs(node)


num = int(sys.stdin.readline())
graph = collections.defaultdict(list)
visited = [False for _ in range(num + 1)]
order = [0 for _ in range(num + 1)]
for _ in range(num - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

user_input = list(map(int, sys.stdin.readline().split()))

for i in range(len(user_input)):
    order[user_input[i]] = i

for i in range(1,num + 1):
    graph[i].sort(key = lambda  x : order[x])

stack = []
dfs(1)

if stack == user_input:
    print(1)
else:
    print(0)