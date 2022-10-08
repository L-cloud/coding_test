# 상하좌우 네 방향 중 하나로 이동
# 같은 값 = 합쳐짐
# 한 번 이동 합쳐진 블록 다시 합체 x 
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값
# 블록은 2의 제곱 꼴
# 최대 5번 이동
# 그냥 구현?
import sys,copy
from typing import List
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
ans = max(matrix[i][j] for j in range(N) for i in range(N))
mat_order  = [[[i for i in range(N)],[i for i in range(N)]], [[i for i in range(N-1,-1,-1)],[i for i in range(N)]],
                [[i for i in range(N)],[i for i in range(N)]], [[i for i in range(N)],[i for  i in range(N-1,-1,-1)]]]
move_order = [[-1,0],[1,0],[0,-1],[0,1]]
visited = {}
def dfs(matrix:List[List[int]],cnt : int):
    for k in range(4):
        v = set()
        m  = copy.deepcopy(matrix)
        flag = False # 변화 하였는가
        dx,dy = move_order[k][0],move_order[k][1]
        for i in mat_order[k][0]:
            for j in mat_order[k][1]:
                x,y = i,j
                if  matrix[i][j]:
                    while 0<=x+dx<len(m) and 0<=y+dy<len(m) and not m[x+dx][y+dy]:
                        m[x][y] = 0
                        x += dx
                        y += dy
                        m[x][y] = matrix[i][j]
                        flag = True
                    if 0<=x+dx<len(m) and 0<=y+dy<len(m) and (x+dx, y+dy) not in v and m[x+dx][y+dy] == matrix[i][j]:
                        m[x][y] = 0
                        m[x+dx][y+dy] *= 2
                        flag = True
                        global ans
                        ans = max(ans,m[x+dx][y+dy])
                        v.add((x+dx,y+dy))
        if flag and cnt < 5:
            tempt = tuple(tuple(m[i]) for i in range(len(m)))
            if tempt not in visited or cnt + 1 < visited[tempt] :
                visited[tempt] = cnt + 1
                dfs(m,cnt + 1)
dfs(matrix,1)
print(ans)
