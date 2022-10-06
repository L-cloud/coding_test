from typing import List,Union
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
hole, red, blue = [],[],[]
for i in range(N): # 초기화
    for j in range(M):
        if matrix[i][j] == 'O':
            hole = [i,j]
        elif matrix[i][j] =='B':
            blue = [i,j]
        elif matrix[i][j] == 'R':
            red = [i,j]
v = {tuple(red)+tuple(blue) : 0}
answer = 11
def dfs(red:List[int],blue:List[int],cnt:int) -> None:
    global answer
    if answer <= cnt:
        return
    for i in range(4):
        r = red[:]
        b = blue[:]
        move(r,b,i)
        if b == hole: 
            pass
        elif r == hole:
            answer = min(answer,cnt)
        elif tuple(r) + tuple(b) not in v or cnt <  v[tuple(r) + tuple(b)] : 
            v[tuple(r) + tuple(b)] = cnt
            dfs(r,b,cnt+1)
        matrix[r[0]][r[1]] = '.'
        matrix[b[0]][b[1]] = '.'
        matrix[red[0]][red[1]] = 'R'
        matrix[blue[0]][blue[1]] = 'B'
        matrix[hole[0]][hole[1]] = 'O'
def move(red:List[int], blue:List[int], index:int)->None:
    d = [[0,1],[1,0],[0,-1],[-1,0]]
    if index == 0: # 오른쪽
        if red[1] <= blue[1]:
            go(blue,d[index],'B')
            go(red,d[index],'R')
            return
        go(red,d[index],'R')
        go(blue,d[index],'B')
    elif index == 1: # 아래
        if red[0] <= blue[0]:
            go(blue,d[index],'B')
            go(red,d[index],'R')
            return red, blue
        go(red,d[index],'R')
        go(blue,d[index],'B')
    elif index == 2: # 왼쪽
        if blue[1] <= red[1]:
            go(blue,d[index],'B')
            go(red,d[index],'R')
            return 
        go(red,d[index],'R')
        go(blue,d[index],'B')
    else: #위
        if blue[0]<= red[0]:
            go(blue,d[index],'B')
            go(red,d[index],'R')
            return
        go(red,d[index],'R')
        go(blue,d[index],'B')
def go(x:List[int], d:List[int],color:str)-> List[int]:
    while 0<=x[0]+d[0]<len(matrix) and 0<=x[1]+d[1] <len(matrix[0]) and matrix[x[0] + d[0]][x[1] + d[1]] == '.' :
        matrix[x[0]][x[1]] = '.'
        x[0] += d[0]
        x[1] += d[1]
        matrix[x[0]][x[1]] = color
    if matrix[x[0] + d[0]][x[1] + d[1]] == 'O':
        matrix[x[0]][x[1]] = '.'
        x[0] += d[0]
        x[1] += d[1]

         
dfs(red,blue,1)
print(answer if answer != 11 else -1)
