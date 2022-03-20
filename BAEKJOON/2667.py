import sys
import collections
def dfs(row:int, col:int) -> int:
    if visited[row][col]:
        return 0
    dx = [-1,1,0,0] # 아 까먹어서 블로그 봄..
    dy = [0,0,-1,1]
    num = 0
    stack = collections.deque([[row, col]])
    while stack:
        i, j = stack.pop()
        if visited[i][j]:
            continue
        if houses[i][j] == '0':
            visited[i][j] = True
            continue
        else:
            num += 1 # apartment
            for x in range(4):
                row_ = dx[x] + i
                col_ = dy[x] + j
                if 0 <= row_ < len(houses) and 0 <= col_ < len(houses) and not visited[row_][col_]:
                    stack.appendleft([row_,col_])
            visited[i][j] = True

    return num



matrix = int(sys.stdin.readline())
houses = []
for _ in range(matrix):
    houses.append(list(map(str,sys.stdin.readline().rstrip())))
visited= [[False for _ in range(matrix)] for _ in range(matrix)]
comple = []
for i in range(matrix):
    for j in range(matrix):
        h = dfs(i,j)
        if h:
            comple.append(h)
print(len(comple))
for i in sorted(comple):
    print(i)
