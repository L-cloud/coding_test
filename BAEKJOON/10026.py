import sys
from typing import List
input = sys.stdin.readline
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
v1,v2 = [[False for _ in range(N)] for _ in range(N)], [[False for _ in range(N)] for _ in range(N)]
def check(color:List[str],i:int,j:int,visited:List[bool]):
    tempt,dx,dy = [(i,j)],[1,-1,0,0],[0,0,-1,1]
    visited[i][j] = True
    while tempt:
        r,c = tempt.pop()
        for i in range(4):
            row, col = r + dx[i], c + dy[i]
            if 0<=row < len(matrix) and 0<= col < len(matrix) and matrix[row][col] in color and not visited[row][col]:
                tempt.append((row,col))
                visited[row][col] = True
answer = [0,0]
for color in (['R'],['G'],['B']):
    for i in range(N):
        for j in range(N):
            if not v1[i][j] and matrix[i][j] in color:
                check(color,i,j,v1)
                answer[0] += 1
for color in (['R','G'],['B']):
    for i in range(N):
        for j in range(N):
            if not v2[i][j] and matrix[i][j] in color:
                check(color,i,j,v2)
                answer[1] += 1
print(*answer)

        
