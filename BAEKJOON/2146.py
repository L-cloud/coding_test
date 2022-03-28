import sys, collections

def is_island(i:int, j:int, num:int) -> bool: #섬들 번호 부여해줌
    if (i,j) in island or geo[i][j] == 0:
        return False
    stack = collections.deque([(i,j)])
    land_num[num].append((i,j))
    island[(i,j)] = num
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while stack:
        for _ in range(len(stack)):
            row, col = stack.pop()
            for d in range(4):
                r = row + dx[d]
                c = col + dy[d]
                if 0<= r < len(geo) and 0<= c < len(geo) and geo[r][c] and not visited[r][c]: # 0이 아닌 녀석들만
                    stack.appendleft((r,c))
                    land_num[num].append((r,c))
                    island[(r,c)] = num
                    visited[r][c] = True
    return True

def bfs():
    min_value = float('inf')
    for key in land_num:
        stack = collections.deque(land_num[key][:]) # 섬 한개씩 돌기
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        tempt = [g[:] for g in geo]
        while stack:
            for _ in range(len(stack)):
                row, col = stack.pop()
                for d in range(4):
                    r = dx[d] + row
                    c = dy[d] + col
                    if 0<= r < len(geo) and 0<= c < len(geo):
                        if tempt[r][c] == 0:
                            tempt[r][c] = tempt[row][col] + 1
                            island[(r,c)] = key # 일단 섬1 에서 온거라 섬1로 침
                            stack.appendleft([r,c])
                        elif island[(row,col)] != island[(r,c)]: # find 
                            min_value = min(tempt[row][col] - 1, min_value) # 섬이 1로 초기화 되어있고 하나 되면 2가 되어버리니까 -1 해야함 
    return min_value



size = int(sys.stdin.readline())
island = {} # 노드에 섬들 번호 부여함 ex) [1,1] = 1  // [3,4] = 2  서로 다른 섬
geo = []
land_num = collections.defaultdict(list)
for _ in range(size):
    geo.append(list(map(int, sys.stdin.readline().split())))
num = 1
visited = [[False for _ in range(size)]for _ in range(size)]
for i in range(size): # 일단 섬 찾기
    for j in range(size):
        if is_island(i,j,num): # 섬을 찾은거니 이제 다른 섬에는 다른 번호 부여
            num += 1

print(bfs())