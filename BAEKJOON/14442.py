import sys
from collections import deque
row, col, K = map(int, sys.stdin.readline().split())
if row == 1 and col == 1:
    print(1)
    exit()
matrix = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(row)]
visited = [[[False for _ in range(col)]for _ in range(row)] for _ in range(K+1)]
dq, cnt = deque([[K,0,0]]),1  
visited[K][0][0] = 0
dx, dy = [1,-1,0,0],[0,0,-1,1]
while dq:
    cnt += 1
    for _ in range(len(dq)):
        node = dq.pop()
        for i in range(4):
            x = node[1] + dx[i]
            y = node[2] + dy[i]
            if 0<= x < row and 0<= y < col:
                if x == row-1 and y == col-1:
                    print(cnt)
                    exit()
                if matrix[x][y] and node[0]: # matrix[x][y] == 1 
                    if not visited[node[0]-1][x][y]:
                        visited[node[0]-1][x][y] = True
                        dq.appendleft([node[0]- 1, x, y])
                elif not matrix[x][y] : # 뚫려있음
                    if not visited[node[0]][x][y]:
                        visited[node[0]][x][y] = True
                        dq.appendleft([node[0], x, y])
print(-1)

