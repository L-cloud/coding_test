import sys
input = sys.stdin.readline
N,M = map(int,input().split())
matrix = [[float('inf') if i !=j else 0 for j in range(N)]for i in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    matrix[a-1][b-1] = 1 
    matrix[b-1][a-1] = 1

def find(index:int, node:int):
    for i, v in enumerate(matrix[node]):
        if matrix[index][node] + v < matrix[index][i]: # 지금보다 node 거쳐서 가는게 더 가까움
            matrix[index][i] = matrix[index][node] + v
            find(index, i)
min_value = float('inf')
min_index = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            find(i,j)
    if sum(matrix[i]) < min_value:
        min_value = sum(matrix[i])
        min_index = i + 1
print(min_index)
