import sys,copy

row, col , N = map(int,sys.stdin.readline().split())
dic = {}
map_ = [list(sys.stdin.readline().rstrip()) for _ in range(row)]
dic[1] = copy.deepcopy(map_)
dic[2] = [list('O' for _ in range(col)) for _ in range(row)]
bomb = {}
for i in range(row):
    for j in range(col):
        if map_[i][j] == 'O':
            bomb[(i,j)] = 0
map_ =  [list('O' for _ in range(col)) for _ in range(row)]
for key in bomb.keys():
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    for d in range(4):
        x = key[0] + dx[d]
        y = key[1] + dy[d]
        if 0<= x < row and 0<= y < col:
            map_[x][y]= '.'
    map_[key[0]][key[1]] = '.'
dic[3] = copy.deepcopy(map_) # 3초
bomb = {}
for i in range(row):
    for j in range(col):
        if map_[i][j] == 'O':
            bomb[(i,j)] = 0
map_ =  [list('O' for _ in range(col)) for _ in range(row)]
for key in bomb.keys():
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    for d in range(4):
        x = key[0] + dx[d]
        y = key[1] + dy[d]
        if 0<= x < row and 0<= y < col:
            map_[x][y]= '.'
    map_[key[0]][key[1]] = '.'
dic[4] = map_
if N == 1:
    for m in dic[1]:
        print("".join(m))
elif N % 2 == 0:
    for m in dic[2]:
        print("".join(m))
elif N % 4 == 1:
    for m in dic[4]:
        print("".join(m))
else: # N % 4 == 3
    for m in dic[3]:
        print("".join(m))
