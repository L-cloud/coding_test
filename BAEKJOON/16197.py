import sys,collections
row, col = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(row)]
visited = set()
coin = [] 
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 'o':
            coin.extend([i,j])
visited.add(tuple([coin[0], coin[1],coin[2],coin[3]]))
coin = collections.deque([coin])
cnt = 0
dx, dy = [1,-1,0,0], [0,0,1,-1]
while coin and cnt < 10:
    cnt += 1
    for _ in range(len(coin)):
        c = coin.pop()
        for i in range(4):
            x1 ,y1 = dx[i] + c[0],dy[i] + c[1]
            x2, y2 = dx[i] + c[2], dy[i] + c[3]
            if 0<= x1 < row and 0<= y1 < col and 0<= x2 < row and 0<= y2 < col: # 둘 다 범위 내임
                if tuple([x1,y1,x2,y2]) in visited:
                    continue
                if matrix[x1][y1] == '#' and matrix[x2][y2] == '#': # 양쪽 다 벽
                    continue
                elif matrix[x1][y1] == '#': # x2, y2 만 움직임
                    coin.appendleft([c[0],c[1],x2,y2])
                    visited.add(tuple([c[0],c[1],x2,y2]))
                elif matrix[x2][y2] == '#': # x1,y1만 움직임
                    coin.appendleft([x1,y1,c[2],c[3]])
                    visited.add(tuple([x1,y1,c[2],c[3]]))
                else: # 벽이 없음
                    coin.appendleft([x1,y1,x2,y2])
                    visited.add(tuple([x1,y1,x2,y2]))
            elif (0<= x1 < row and 0<= y1 < col) or (0<= x2 < row and 0<= y2 < col):  # 둘 다 범위 내 아님 이게 왜 아님?? 
                print(cnt)
                exit()
            else: # 둘 다 떨어짐
                continue
print(-1)