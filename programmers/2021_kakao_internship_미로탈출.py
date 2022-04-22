import collections, sys
sys.setrecursionlimit(100000)
def solution(n, start, end, roads, traps): # dfs
    matrix = [[0 for _ in range(n + 1)]for _ in range(n + 1)]
    graph = collections.defaultdict(set)
    cost_matrix = [[0 for _ in range(n + 1)]for _ in range(n + 1)]
    trap_condition = {trap : 0 for trap in traps}
    for i,j,cost  in roads:
        graph[i].add(j)
        graph[j].add(i)
        matrix[i][j] = 1
        if cost_matrix[i][j]: 
            cost_matrix[i][j] = min(cost, cost_matrix[i][j])
        else:
            cost_matrix[i][j] = cost
    visited = [[float('inf') for _ in range(n + 1)]for _ in range(n + 1)]
    answer = [float('inf')]
    trap_visited = [[[float('inf') for _ in range(n + 1)]for _ in range(n + 1)]for _ in range(2)]
    def dfs(node:int, cost : int):
        for edge in graph[node]:
            flag = False
            if matrix[node][edge]:
                if edge in trap_condition:
                    condition = trap_condition[edge]
                    if cost + cost_matrix[node][edge] < trap_visited[condition][node][edge]:
                        trap_visited[condition][node][edge] = cost + cost_matrix[node][edge]
                        c = trap_visited[condition][node][edge]
                        flag = True
                elif cost + cost_matrix[node][edge] < visited[node][edge]:
                    visited[node][edge] = cost + cost_matrix[node][edge]
                    flag = True
                    c = visited[node][edge]
                if flag:
                    if edge == end:
                        answer[0] = min(answer[0],c)
                        continue
                    if edge in traps:
                        edges = graph[edge]
                        trap_condition[edge] = 0 if trap_condition[edge] else 1
                        for i in edges: # 방향 바꿈
                            matrix[edge][i],matrix[i][edge] = matrix[i][edge], matrix[edge][i]
                            cost_matrix[edge][i], cost_matrix[i][edge] = cost_matrix[i][edge],cost_matrix[edge][i]
                    dfs(edge, c)
                    if edge in traps:
                        edges = graph[edge]
                        trap_condition[edge] = 0 if trap_condition[edge] else 1
                        for i in edges: # bfs 빠져 나오면 다시 또 방향 바꿈
                            matrix[edge][i],matrix[i][edge] = matrix[i][edge], matrix[edge][i]
                            cost_matrix[edge][i], cost_matrix[i][edge] = cost_matrix[i][edge],cost_matrix[edge][i]
    if start == end:
        return 0            
    dfs(start,0)    
    return answer[0]
#print(solution(	4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])) # 이거 이상
