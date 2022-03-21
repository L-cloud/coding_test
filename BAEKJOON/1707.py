import sys
import collections
def bfs(num:int) -> bool:
    if color[num]: # 이미 방문함
        return True
    red = 1
    blue = 2
    color[num] = 1# 처음 노드 그냥 red
    stack = collections.deque([num])
    while stack:
        for _ in range(len(stack)):
            node_ = stack.pop()
            next_color = red if color[node_] == blue else blue # stack에 넣을 때 마다(인접한거임) 색을 바꿔줌 초기 색은 red
            for n in graph[node_]:
                if color[n] and color[n] != next_color:  # 이미 색이 칠해졌고 근데 그 색이 다른 색이 아니라 같은 색
                    return False
                if not color[n]: # 색이 안 칠해져있다면
                    stack.appendleft(n)
                    color[n] = next_color
                # 색 칠해져있는건 이미 탐사한거임
    return True

for _ in range(int(sys.stdin.readline())):
    node_num, edge_num = map(int, sys.stdin.readline().split())
    color = [0 for _ in range(node_num + 1)]
    graph = collections.defaultdict(list)
    for _ in range(edge_num):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    flag = True
    for num in range(1,node_num + 1):
        if not bfs(num):
            flag = False
    if flag:
        print("YES")
    else:
        print("No")

