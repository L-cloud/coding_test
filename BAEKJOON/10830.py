import sys
from typing import List
input = sys.stdin.readline
N, B = map(int,input().split())
matrix = [list(map(int,input().split()))for _ in range(N)]
def dfs(A:List[int],B:int) -> None:
    if B == 1:
        tempt = [[A[i][j] % 1000 for j in range(N)] for i in range(N)]
        return tempt
    if B % 2 == 0:
        A = dfs(A,B//2)
        return multi(A,A)
    else:
        tempt = dfs(A,B//2)
        tempt = multi(tempt,tempt)
        return multi(tempt,A)
def multi(A:List[int],B:List[int]) -> List[int]:
    tempt = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tempt[i][j] += A[i][k] * B[k][j]
            tempt[i][j] %= 1000
    return tempt
output = dfs(matrix,B)
for i in range(N):
    print(*output[i])