import sys,collections

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
N = int(sys.stdin.readline())
chess = list(map(int, sys.stdin.readline().split()))
start_point = [chess[0],chess[1]]
target_point = [chess[2], chess[3]]
visited = [[False for _ in range(N)]for _ in range(N)]
q = collections.deque([start_point])
cnt = -1
while q:
    cnt += 1
    for _ in range(len(q)):
        r,c = q.pop()
        if r == target_point[0] and c == target_point[1]:
            print(cnt)
            exit()
        for d in range(6):
            row = r + dx[d]
            col = c + dy[d]
            if 0<= row < N and 0 <= col < N:
                if not visited[row][col]:
                    q.appendleft([row,col])
                    visited[row][col] = True

print(-1)