import sys
from typing import List


def bfs(visited:set, i:int, j:int, value:int)  : # ㅗ ㅜ는 없음
    if len(visited) == 4:
        max_value[0] = max(value, max_value[0])
        return
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for d in range(4):
        row = dx[d] + i
        col = dy[d] + j            
        if 0<=row < M and 0<= col < N and (row,col) not in visited:
            tempt = visited.copy()
            tempt.add((row,col))
            bfs(tempt, row, col, value + graph[row][col])

def hn(visited:List[int],i:int,j:int, value:int, v:bool, h : bool) : # ㅗ ㅜ 모양
    if len(visited) == 3:
        row = visited[1][0]
        col = visited[1][1]
        if v : # vertical 
            if col + 1 < N:
                max_value[0] = max(value + graph[row][col + 1], max_value[0])
            if  0 < col:
                max_value[0] = max(value + graph[row][col -1], max_value[0])
        else: # horizon
            if row + 1 < M:
                max_value[0] = max(value + graph[row +1][col], max_value[0])
            if 0 < row:
                max_value[0] = max(value + graph[row -1][col], max_value[0])
        return True
    tempt = visited[:]
    if v:
        if i + 1 < M:
            tempt.append([i+1,j])
            hn(tempt,i + 1,j,value + graph[i + 1][j],True,False)
    if h:
        if j + 1< N:
            tempt.append([i,j + 1])
            hn(tempt, i,j+1, value + graph[i][j + 1], False, True)
        

    



    pass

M, N = map(int, sys.stdin.readline().split())

graph = []
max_value = [float('-inf')]

for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(M):
    for j in range(N):
        bfs({(i,j)},i,j,graph[i][j])
        hn([[i,j]],i,j, graph[i][j],True,False)
        hn([[i,j]],i,j, graph[i][j],False,True)

print(max_value[0])