from typing import List
from collections import deque
def solution(maps:List[List[int]]) -> int:
    s,v = deque([(0,0)]),{(0,0)}
    t = 1
    dx,dy = [0,1,0,-1], [1,0,-1,0]
    while s:
        for _ in range(len(s)):
            r,c = s.popleft()
            if (r,c) == (len(maps) -1,len(maps[0]) - 1):
                return t
            for i in range(4):
                x,y = r + dx[i], c + dy[i]
                if 0<=x<len(maps) and 0<=y<len(maps[0]) and (x,y) not in v and maps[x][y]:
                    s.append((x,y))
                    v.add((x,y))
        t+=1
    return -1
