import sys
import heapq
from typing import List
input = sys.stdin.readline
N,K = map(int, input().split())
m = [list(map(int ,input().split())) for _ in range(N)]
direction = [[0,1], [0,-1], [-1,0], [1,0]]
pq = []
h = [[[] for _ in range(N)] for _ in range(N)]
for i in range(K):
    x,y,d = map(int, input().split())
    h[x-1][y-1].append([i,d-1])
    heapq.heappush(pq, (i,[x-1,y-1,d-1]))
def check(x:int, y:int, node:List[int]):
    if 0<= x < N and 0<= y < N and m[x][y] != 2:
        if m[x][y] == 0 : h[x][y] += h[node[0]][node[1]]
        if m[x][y] == 1: 
            h[x][y] += h[node[0]][node[1]][::-1]
            heapq.heappush(pq, (h[x][y][0][0], [x,y, h[x][y][0][1]]))
        h[node[0]][node[1]] = []
        return True
time = 0
min_val = -1
while time < 1000:
    while pq:
        i, node = heapq.heappop(pq)
        if i <= min_val : continue
        min_val = i
        x = node[0] + direction[node[2]][0]
        y = node[1] + direction[node[2]][1]
        if check(x,y,node) : continue
        node[2] = node[2] - 1 if node[2] % 2 else node[2] + 1
        x = node[0] + direction[node[2]][0]
        y = node[1] + direction[node[2]][1]
        h[node[0]][node[1]][0][1] = node[2]
        check(x,y,node)
    time += 1
    for i in range(N):
        for j in range(N):
            if h[i][j]: 
                min_val = min(min_val, h[i][j][0][0])
                heapq.heappush(pq,(h[i][j][0][0], [i,j,h[i][j][0][1]]))
            if len(h[i][j]) >= 4:
                print(time)
                exit(0)
    min_val -= 1
print(-1)
