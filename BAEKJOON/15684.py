import sys
from typing import List

def possible(m:List[List[int]]) -> bool:
    for i in range(len(m[0])):
        s = i
        for j in range(len(m)):
            s = m[j][s] if m[j][s] != None else s
        if s != i:
            return False
    return True
def change(chance:int, x:int ,matrix:List[List[int]]) -> bool:
    if not chance:
        if possible(matrix):
            return True
        return False
    for i in range(x,len(matrix)):
        for j in range(len(matrix[0]) -1):
            if matrix[i][j] == None and not matrix[i][j+1]:
                matrix[i][j] = j+1
                matrix[i][j+1] = j
                if change(chance-1,i,matrix):
                    return True
                matrix[i][j] = None
                matrix[i][j+1] = None
    return False
input = sys.stdin.readline
N,M,H = map(int,input().split())
matrix = [[None]*N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    matrix[a-1][b-1] = b
    matrix[a-1][b] = b - 1


for i in range(4):
    if change(i,0,matrix):
        print(i)
        break
else:
    print(-1)

