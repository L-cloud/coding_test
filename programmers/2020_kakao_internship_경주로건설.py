import collections
def solution(board):
    q = collections.deque([[0,1,1,1,1,0,0]]) # cost, 상하좌우, dx, dy
    visited = [[[float('inf'),float('inf'),float('inf'),float('inf')] for _ in range(len(board))] for _ in range(len(board))]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] # 상하좌우 맞춤
    while q:
        node = q.pop()
        for i in range(4):
            r = dx[i] + node[-2]
            c = dy[i] + node[-1]
            if 0<= r < len(board) and 0<= c < len(board):
                if board[r][c] != 1:
                    if node[i + 1]: # 방향이 맞음
                        cost = node[0] + 100
                    else: # 방향 안 맞음 
                        cost = node[0] + 600 
                    if cost <= visited[r][c][i]: # node 그쪽 방향으로 안 가봄
                        if cost <= visited[r][c][i] or not visited[r][c][i]: 
                            visited[r][c][i] = cost
                        q.appendleft([cost,0,0,0,0,r,c])
                        q[0][i+1] = 1 # 방향 추가 

    return min(visited[-1][-1])


print(solution([
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 1, 0, 0],
[1, 0, 0, 0, 1],
[0, 1, 1, 0, 0]
]))