import sys

def dfs(row : int, col : int) -> bool:
    if visited[row][col]:
        return False
    visited[row][col] = True
    if land[row][col] == 1:
        if  0 < row:
            dfs(row - 1,col)
        if row < m - 1:
            dfs(row + 1, col)
        if 0 < col:
            dfs(row, col -1)
        if col < n - 1:
            dfs(row, col + 1)
        if 0 < row and 0 < col :
            dfs(row - 1, col - 1)
        if row < m - 1 and col < n - 1:
            dfs(row + 1, col + 1)
        if 0 < row and col < n - 1:
            dfs(row - 1, col + 1)
        if row < m - 1 and 0 < col:
            dfs(row + 1, col - 1) 
        return True
    return False


while True:
    n, m = map(int, sys.stdin.readline().split()) # col, row
    if n == m == 0:
        exit()
    land, island = [], 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    for _ in range(m):
        land.append(list(map(int, sys.stdin.readline().split())))
    for row in range(m):
        for col in range(n):
            if dfs(row,col):
                island += 1

    print(island)
