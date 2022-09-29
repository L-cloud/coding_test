import sys
from typing import List,Union
from heapq import heappush, heappop
from collections import deque
def find_fish(row:int,col:int, matrix :List[List[int]],shark_size:int) -> Union[List[int],List[List[int]]]:
    visited = [[0]*len(matrix)for _ in range(N)]
    h = deque([[row,col]])
    dx,dy = [1,-1,0,0],[0,0,-1,1]
    cnt = 0
    answer = []
    while h :
        cnt += 1
        for _ in range(len(h)):
            row,col = h.pop()
            for i in range(4):
                x = row + dx[i]
                y = col + dy[i]
                if 0<= x < len(matrix) and 0<= y < len(matrix) and not visited[x][y] and matrix[x][y] <= shark_size and matrix[x][y] != 9:
                    visited[x][y] = cnt
                    if matrix[x][y] and matrix[x][y] < shark_size:
                        answer.append([x,y])
                    h.appendleft([x,y])
    return answer,visited



input = sys.stdin.readline 
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
shark = [[i,j] for i in range(N) for j in range(N) if matrix[i][j] == 9].pop()
shark_size, fee,time = 2,0,0
while True:
    h = []
    fishes, v = find_fish(shark[0],shark[1],matrix,shark_size)
    for fish in fishes:
        heappush(h,((v[fish[0]][fish[1]]),fish[0],fish[1]))
    if h:
        t,row,col = heappop(h)
        time += t
        fee += 1
        matrix[shark[0]][shark[1]] = 0
        matrix[row][col] = 9
        shark = [row,col]
        if fee == shark_size :
            fee = 0
            shark_size += 1
    else:
        break
print(time)       
