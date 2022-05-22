import sys,collections

row, col = map(int, sys.stdin.readline().split())

visited1 = [list(float('inf') for _ in range(col)) for _ in range(row)] # 벽 안 부순 녀석들 방문 노드
visited2 = [list(float('inf') for _ in range(col)) for _ in range(row)] # 벽 뿌순녀석들 방문 노드
matrix = [list(map(int, sys.stdin.readline().rstrip()))for _ in range(row)]
h = collections.deque([[1,0,0]])  # 벽 부셨는가, row, col
cnt = 1
dx,dy = [1,-1,0,0],[0,0,1,-1]
while h: # 문제는 visited1, visited2 둘 다 update시켜줘야하는건데
    cnt += 1
    for _ in range(len(h)):
        node = h.pop()
        for i in range(4):
            x = node[1] + dx[i]
            y = node[2] + dy[i]
            if 0<= x < row and 0<= y < col :
                if matrix[x][y] == 1:
                    if node[0]: # 벽 부술 수 있음
                        if cnt < visited2[x][y]:
                            visited2[x][y] = cnt
                            h.appendleft([0,x,y])
                else: 
                    if node[0]: # 벽 안 부순 녀석들
                        if cnt < visited1[x][y]:
                            visited1[x][y] = cnt
                            h.appendleft([1,x,y])
                    else:
                        if cnt < visited2[x][y]:
                            visited2[x][y] = cnt
                            h.appendleft([0,x,y])
min_value = min(visited1[-1][-1], visited2[-1][-1])
if min_value == float('inf'):
    print(-1)
else:
    print(min_value)
