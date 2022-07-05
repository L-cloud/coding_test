import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
matrix = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    matrix[a][b] = min(matrix[a][b], c)

for i in range(1,N +1):
    h = []
    for index,j in enumerate(matrix[i]):
        if j != float('inf'):
            heapq.heappush(h,(j,index))
    while h:
        cost, index = heapq.heappop(h)
        for index2,c in enumerate(matrix[index]):
            if cost + c < matrix[i][index2] and index2 != i:
                matrix[i][index2] = cost + c
                heapq.heappush(h,(cost+ c,index2))

for i in range(1,N+1):
    for j in range(1,N+1):
        if matrix[i][j] == float('inf'):
            print(0 ,end = " ")
        else:
            print(matrix[i][j], end = " ")
    print()