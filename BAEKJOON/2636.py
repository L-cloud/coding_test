[200~# 1. 빈칸을 돌면서 빈 칸인지 내부 공간인지 확인한다.
        # 2. 치즈를 돌면서 얼마나 접촉했는지 확인한다.

import sys
input = sys.stdin.readline
def check_air(r:int,c:int,v:set[int]):
    v.add((r,c))
    visited[r][c],flag = True, True
    for k in range(4):
        if not flag:
            break
        row, col = r+dx[k], c+dy[k]
        if 0<= row < N and 0<= col < M:
            if (row,col) not in v: # 방문 안 함
                if not matrix[row][col] and not visited[row][col]: # 갈 수 있는 곳
                    flag = check_air(row,col,v)
                elif visited[row][col]: # visited임
                    flag = False
        else: # 범위를 벗어남
            flag = False
    return flag
def check() -> None:
    output = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                cnt = 0
                for k in range(4):
                    x, y = dx[k] + i ,dy[k] + j
                    if 0<= x <N and 0<= y <M and not air[x][y]:
                        cnt += 1
                if 1 < cnt:
                    output.append((i,j))
    for i, j in output:
        matrix[i][j] = 0
    return True if output else False

N,M = map(int, input().split())
matrix = [list(map(int, input().split()))for _ in range(N)]
cheeze = True
time,dx,dy = 0,[0,1,0,-1], [1,0,-1,0]
while cheeze:
    visited = [[False for _ in range(M)] for _ in range(N)]
    air = [[matrix[i][j] for j in range(M)] for i in range(N)]
    for i in range(N): # 치즈 내부 공간 찾기
        for j in range(M):
            if not visited[i][j] and not matrix[i][j]:
                v  = set()
                if check_air(i,j,v):
                    for r,c in v:
                        air[r][c] = -1
    cheeze = check()
    time += 1
print(time - 1)


