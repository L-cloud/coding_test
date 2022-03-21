import sys
def dfs(course:set,bi:int, bj:int, i:int, j:int) -> None:
    if visited[i][j]:
        return
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[i][j] = True
    course.add((i,j))
    for n in range(4):
        r = dx[n] + i
        c = dy[n] + j
        if 0<= r < len(matrix) and 0<= c < len(matrix[0]) and matrix[r][c] == matrix[i][j]: # 같은 문자열만
            if not(bi == r and bj == c) and (r,c) in course:
                print("Yes")
                return #exit()으로 나중에 교체
            dfs(course,i,j,r,c)
    return

while True:
    row, col = map(int, sys.stdin.readline().split())
    matrix = []

    for _ in range(row):
        matrix.append(list(map(str, sys.stdin.readline().rstrip())))
    visited = [[False for _ in range(col)]for _ in range(row)]
    for i in range(row):
        for j in range(col):
            dfs(set(),0,0,i,j)

    print("No")