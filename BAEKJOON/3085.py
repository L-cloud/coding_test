import sys
# 아 처음 시작이 다르다면?
def row_quest(row:int, col:int) -> int:
    i, j = row, col
    if visited[i][j]:
        return -1
    color,chance = candi[i][j], True
    cnt = 1
    visited[i][j] = True
    while j < N - 1:
        if candi[i][j + 1] == color:
            j += 1
            cnt += 1
        else:
            if chance:
                if i < N - 1:
                    if candi[i+1][j+1] == color: # 다음칸 위
                        cnt += 1
                        chance = False
                        j += 1
                        continue # 그냥 밑에 먼저
                
                if 0 < i:
                    if candi[i - 1][j+1] == color: #다음칸 아래
                        cnt += 1
                        chance = False
                        j += 1
                        continue
           
                if j < N - 2:
                    if candi[i][j + 2] == color:
                        cnt += 1
                        return cnt
            break
    if chance and 0 < col:
        if 0 < row and candi[row-1][col-1] == color:
            cnt += 1
        elif row < N -1 and candi[row + 1][col - 1] == color:
            cnt += 1
        elif 1 < col and candi[row][col -2] == color:
            cnt += 1
        
    return cnt

def col_quest(row:int, col:int) -> int:
    i, j = row, col
    if visited[i][j]:
        return -1
    color,chance = candi[i][j], True
    cnt = 1
    visited[i][j] = True
    while i < N - 1:
        if candi[i+1][j] == color:
            i += 1
            cnt += 1
            if chance:
                visited[i][j] = True
        else:
            if chance:
                if j < N - 1:
                    if candi[i+1][j+1] == color:
                        cnt += 1
                        chance = False
                        i += 1
                        continue # 그냥 밑에 먼저
                
                if 0 < j:
                    if candi[i+1][j-1] == color:
                        cnt += 1
                        chance = False
                        i += 1
                        continue
                if i < N-2 and candi[i+2][j] == color:
                    cnt += 1
                    return cnt

            break
    if chance and 0 < row:
        if 0 < col and candi[row -1][col -1] == color:
            cnt += 1
        elif col < N -1 and candi[row - 1][col + 1] == color:
            cnt += 1
        elif 1 < row and candi[row -2][col] == color:
            cnt += 1 
    return cnt
        

N = int(sys.stdin.readline())
visited =[[False for _ in range(N)]for _ in range(N)]
candi = []
cnt = 0
for _ in range(N):
    candi.append(list(map(str,sys.stdin.readline().rstrip())))

for i in range(N):
    for j in range(N):
        num = row_quest(i,j)
        if num > 0:
            cnt = max(num,cnt)

visited =[[False for _ in range(N)]for _ in range(N)]

for i in range(N):
    for j in range(N):
        num = col_quest(i,j)
        if num > 0:
            cnt = max(num,cnt)

print(cnt)