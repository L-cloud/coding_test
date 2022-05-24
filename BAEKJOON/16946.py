import sys
sys.setrecursionlimit(10**9)
def dfs(row:int, col:int, visited:set) :
    for i in range(4):
        x = row + dx[i]
        y = col + dy[i]
        if 0<= x <len(matrix) and 0<= y < len(matrix[0]) and not matrix[x][y] and not m[x][y] and (x,y) not in visited:
            visited.add((x,y))
            dfs(x,y,visited)
    return visited
linked_group,cnt  = dict(), 0
row, col = map(int, sys.stdin.readline().split())
dx,dy = [1,-1,0,0],[0,0,1,-1]
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(row)]
m,q = [[0 for _ in range(col)] for _ in range(row)],[]
for i in range(row): # 1 찾기
    for j in range(col):
        if matrix[i][j]:
            q.append([i,j])
for i in range(row):
    for j in range(col):
        if not matrix[i][j] and not m[i][j]: # matrix [i][j] == 0
            visited = {(i,j)}
            visited = dfs(i,j,visited)
            for r,c in visited:
                m[r][c] = len(visited)
                linked_group[(r,c)] = cnt
            cnt += 1
while q:
    r,c = q.pop()
    tempt = set()
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]
        if 0<= x <row and 0<= y < col and (x,y) in linked_group and linked_group[(x,y)] not in tempt:
            matrix[r][c] += m[x][y]
            tempt.add(linked_group[(x,y)])
    matrix[r][c] %= 10

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end="")
    print("")