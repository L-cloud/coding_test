import sys
from typing import List
def w(d:List[int]) -> List[int]:
    d[1],d[4],d[0],d[3] = d[0],d[3],d[4],d[1]
    return d
def e(d:List[int]) -> List[int]:
    d[4],d[1],d[0],d[3] = d[0],d[3],d[1],d[4]
    return d
def s(d:List[int]) -> List[int]:
    d[2],d[5],d[0],d[3] = d[0],d[3],d[5],d[2]
    return d
def n(d:List[int]) -> List[int]:
    d[5],d[2],d[0],d[3] = d[0],d[3],d[2],d[5]
    return d
input = sys.stdin.readline
N,M,x,y,_ = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
k = list(map(int,input().split()))
d = [0] * 6
fun = [None,e,w,n,s]
dx,dy = [None,0,0,-1,1],[None,1,-1,0,0]
for c in k:
    xx,yy = x + dx[c], y + dy[c]
    if 0<=xx<N and 0<=yy<M:
        x,y = xx,yy
        d = fun[c](d)
        if matrix[x][y]:
            d[0] = matrix[x][y]
            matrix[x][y] = 0
        else:
            matrix[x][y] = d[0]
        print(d[3])