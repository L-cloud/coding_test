'''
상하좌우 대각선 가능

상어는 (0,0) 물고기를 먹고 움직이고 그 방향은 물고기의 방향과 같음
물고기는 번호가 작은 물고기 순서대로 이동
물고기는 1칸 이동 가능, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸
이동 불가능 칸은 상어가 있거나 공간의 경계를 넘는 칸

각 물고기는 방향이 이동할 수 있는 칸을 향할 때 까지 방향을 45도 반시계 방향으로 회전 시킴.
다른 물고기가 있는 칸으로 이동하면 그 물고기와 위치를 바꿈

물고기 이동이 끝나면 상어가 이동
상어는 방향에 있는 칸으로 이동할 수 있고, 한 번에 여러 칸을 이동할 수 있음.
상어가 해당 칸에 있는 물고기를 먹으면 그 물고기의 방향을 가지게됨.
이동 하는 동안의 물고기는 안 먹음. 물고기가 없는 칸으로 이동 불가.

최대값을 구해보자.
흐음.. 순서 기록?  dfs로 하면 될 것 같은데

'''


import sys
from typing import List

def shark_move(m:List[List[int]], d:List[List[int]] ,s:List[int], ans:int) -> None:
    t,i = [],1
    fish_move(m, d)
    while 0 <=s[0] + dx[d[s[0]][s[1]]] * i < 4 and 0<=s[1] + dy[d[s[0]][s[1]]] * i < 4 : # 해당 방향으로 계속 감
        if m[s[0] + dx[d[s[0]][s[1]]] * i][s[1] + dy[d[s[0]][s[1]]] * i]: # 물고기 있으면 추가
            t.append([s[0] +dx[d[s[0]][s[1]]] * i, s[1] + dy[d[s[0]][s[1]]] * i])
        i += 1
    if not t:
        mx_ans[0] = max(ans, mx_ans[0])
        return
    for x,y in t:
        mat = [[m[i][j] for j in range(4)] for i in range(4)]
        t_d = [[d[i][j] for j in range(4)] for i in range(4)]
        t_ans = ans + mat[x][y]
        mat[x][y] = -1
        mat[s[0]][s[1]] = 0
        shark_move(mat,t_d,[x,y],t_ans)
def fish_move(m:List[List[int]], d:List[List[int]]) -> None:
    l_order = len(get_order(m))
    k = 0
    while k < l_order:
        i,j = get_order(m)[k]
        while True:
            di = d[i][j]
            x,y = i+ dx[di], j + dy[di]
            if 0 <= x < 4 and 0 <= y < 4: # 범위 내
                if m[x][y] == -1: # 상어있음
                    d[i][j] = (d[i][j] + 1) % 8
                    continue
                break
            else:
                d[i][j] = (d[i][j] + 1) % 8
        m[x][y], m[i][j] = m[i][j],m[x][y]
        d[x][y], d[i][j] = d[i][j], d[x][y]
        k += 1

def get_order(m:List[List[int]]) -> List[int]:
    return sorted([[i,j] for i in range(4) for j in range(4) if m[i][j] > 0],key = lambda  x : m[x[0]][x[1]])

input = sys.stdin.readline
m, d = [[0] * 4 for _ in range(4)], [[0] * 4 for _ in range(4)]
for i in range(4):
    a1,b1,a2,b2,a3,b3,a4,b4 = map(int,input().split())
    m[i][0],m[i][1], m[i][2], m[i][3] = a1,a2,a3,a4
    d[i][0],d[i][1],d[i][2], d[i][3] = b1-1,b2-1,b3-1,b4 -1
dx,dy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
mx_ans = [m[0][0]]
m[0][0] = -1
shark_move(m,d,[0,0],mx_ans[0])
print(mx_ans[0])
