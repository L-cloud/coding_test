import sys
input = sys.stdin.readline
def check(i:int,j:int):
    tempt = [(i,j)]
    dx,dy = [1,-1,0,0],[0,0,-1,1]
    while tempt:
        node = tempt.pop()
        for i in range(4):
            x,y = dx[i] + node[0],dy[i] + node[1]
            if 0<= x < len(matrix) and 0<= y < len(matrix[0]) and not visited[x][y] and matrix[x][y]:
                visited[x][y] = True
                tempt.append((x,y))
for _ in range(int(input())):
    N,M,K = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a,b = map(int,input().split())
        matrix[a][b] = 1
    visited = [[False for _ in range(M)]for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] and not visited[i][j]:
                visited[i][j] = True
                check(i,j)
                cnt += 1
    print(cnt)
