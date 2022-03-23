import sys, collections
from typing import List
sys.setrecursionlimit(10000)
def dfs(stack:List[int],node:int) -> bool:
    for num in graph[node]:
        if not visited_dfs[num]:
            visited_dfs[num] = True
            stack.append(num)
            if dfs(stack,num):
                return True
            stack.pop()
        elif visited_dfs[num] and len(stack) >= 3 and stack[-2] != num and num in stack: # 계속 stack in node 해서 부담스러운데
            circle.extend(stack[stack.index(num):])
            return True

def bfs(i:int) -> int:
    visit = set([i])
    stack = collections.deque([i])
    cnt = -1
    while stack:
        cnt += 1
        for _ in range(len(stack)):
            node = stack.pop()
            if output[node]:
                return output[node] + cnt
            for j in graph[node]:
                if j not in visit:
                    visit.add(j)
                    stack.appendleft(j)





node_num = int(sys.stdin.readline())
graph = collections.defaultdict(list)
output = [False for _ in range(node_num + 1)]
visited_dfs = [0 for _ in range(node_num + 1)]
visited_dfs[1] = True
circle = [] # circle인 노드들
for _ in range(node_num):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs([1], 1) # circle의 node 확인

for c in circle:
    output[c] = 1

for i in range(1, node_num + 1):
    print(bfs(i) - 1, end = " ")