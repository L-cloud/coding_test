import sys
sys.setrecursionlimit(10000)
def dfs(m:int, n:int, cnt:int)->None:
    if m == row -1 and n == col - 1:
        visited[m][n] = min(cnt, visited[m][n])
        return 
    if visited[m][n] <= cnt:
        return
    visited[m][n] = cnt
    if maze[m][n] == '1':
        if 0 < m:
            if maze[m-1][n] == "1":
                dfs(m - 1, n, cnt + 1)
        if m < row - 1:
            if maze[m + 1][n] == "1":
                dfs(m + 1, n, cnt + 1)
        if 0 < n:
            if maze[m][n - 1] == "1":
                dfs(m, n - 1 , cnt + 1)
        if n < col - 1:
            if maze[m][n + 1] == "1":
                dfs(m, n + 1, cnt + 1)
    return
row, col = map(int, sys.stdin.readline().split())
maze, visited = [], [[row * col for _ in range(col)] for _ in range(row)]
for _ in range(row):
    maze.append(list(sys.stdin.readline().rstrip()))
dfs(0,0,1)
print(visited[row-1][col-1])