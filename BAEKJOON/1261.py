import sys
import collections
M, N = map(int, sys.stdin.readline().split())
dq, maze, stack = collections.deque([]), [], [(0,0)]
visited = [[False for _ in range(M)]for _ in range(N)]
visited[0][0]= True
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))
time, level = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    flag = False
    level += 1 # 레벨 순서 보장
    while stack:
        row, col = stack.pop()
        if row == N -1 and col == M -1:
            print(time)
            exit()
        for i in range(4):
            r = row + dx[i]
            c = col + dy[i]
            if 0<= r < N and 0<= c < M and not visited[r][c]:
                visited[r][c] = True
                if maze[r][c]:
                    dq.appendleft((r,c))
                else:
                    stack.append((r,c))
    for _ in range(len(dq)): 
        row, col = dq.pop()
        if maze[row][col]: # 1 이라는 말
            flag = True
        for i in range(4):
            r = row + dx[i]
            c = col + dy[i]
            if 0<= r < N and 0<= c < M and not visited[r][c]:
                visited[r][c] = True
                if maze[r][c]:
                    dq.appendleft((r,c))
                else:
                    stack.append((r,c))
    if flag:
        time += 1
    for v in visited:
        print(v)
    print("tiem=",time)
    print('-----------------')