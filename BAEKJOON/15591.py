import sys

N,M = map(int, sys.stdin.readline().split())
matrix = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for _ in range(N-1):
    a,b,c = map(int, sys.stdin.readline().split())
    matrix[a][b] = c
    matrix[b][a] = c


# 다수로 연결된 것을 어떻게 하지??
# 그냥 처음부터 다시 생각해보자
