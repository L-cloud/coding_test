import sys
from typing import List
input = sys.stdin.readline
N,K = map(int, input().split())
m = [list(map(int ,input().split())) for _ in range(N)]
d,q = [[0,1], [0,-1], [-1,0], [1,0]],[]
h, time = [[[] for _ in range(N)] for _ in range(N)], 0
for i in range(K):
    x,y,p = map(int, input().split())
    h[x-1][y-1].append(i)
    q.append([i,[x-1,y-1,p-1]])
def add(i:int, node:List[int]) -> bool:
    x,y = node[0] + d[node[-1]][0], node[1] + d[node[-1]][1]
    index = h[node[0]][node[1]].index(i)
    if 0<=x<N and 0<= y <N and m[x][y] != 2:
        if m[x][y] == 0 : h[x][y] += h[node[0]][node[1]][index:]
        if m[x][y] == 1 : h[x][y] += h[node[0]][node[1]][index:][::-1]
        for k in  h[node[0]][node[1]][index:]: q[k][1][0], q[k][1][1] = x, y
        h[node[0] - d[node[-1]][0] ][node[1] - d[node[-1]][1] ] = h[node[0] - d[node[-1]][0] ][node[1] - d[node[-1]][1]][:index]
        if len(h[x][y]) >= 4:
            print(time)
            exit()
        return True
while time < 1000:
    time += 1
    for i,node in q:
        if add(i,node) : continue
        node[-1] = node[-1] -1 if node[-1] % 2 else node[-1] + 1
        add(i,node)
print(-1)
