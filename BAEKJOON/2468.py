import sys
from collections import deque
from typing import List

input = sys.stdin.readline
N = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def check(mat: List[List[int]], water: int) -> int:
    m = [[mat[i][j] for i in range(N)] for j in range(N)]
    q = deque()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if m[i][j] > water:
                cnt += 1
                m[i][j] = -1
                q.append([i, j])
                while q:
                    node = q.pop()
                    for k in range(4):
                        x = node[0] + dx[k]
                        y = node[1] + dy[k]
                        if 0 <= x < N and 0 <= y < N and m[x][y] > water:
                            q.append([x, y])
                            m[x][y] = -1
    return cnt


cnt = 0
mat = [list(map(int, input().split())) for _ in range(N)]
for water in range(0, 101):
    cnt = max(cnt, check(mat, water))
print(cnt)

