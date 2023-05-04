from collections import deque
from typing import List
def solution(m:int, n:int, puddles:List[List[int]]):
    matrix = [[0] * m for _ in range(n)]
    v = set([(j-1,i -1) for i,j in puddles])
    matrix[0][0] = 1
    q, d = deque([(0,0)]), [[0,1],[1,0]]
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            for i,j in d:
                dx, dy = x +i, y + j
                if (dx,dy) not in v and 0<=dx<n and 0<=dy<m:
                    q.append((dx,dy))
                    v.add((dx,dy))
                    u = matrix[dx-1][dy] if 0 < dx  else 0
                    l = matrix[dx][dy -1] if 0 < dy else 0
                    matrix[dx][dy] = (u + l) % 1000000007
    return matrix[-1][-1] % 1000000007
