import sys,collections
input = sys.stdin.readline
def width(i:int, j:int) -> bool: #가로
    if 0< j+1 < N and not matrix[i][j+1]:
        q.appendleft([i,j+1,0])
        return True
    return False
def length(i:int, j:int) -> bool: # 세로
    if 0<= i +1 < N and not matrix[i + 1][j]:
        q.appendleft([i+1,j,1])
        return True
    return False
def diagonal(i:int, j:int) -> bool: # 대각선
    if 0< i+1 < N and 0 < j+1 < N and not matrix[i][j+1] and not matrix[i+1][j] and not matrix[i+1][j+1]:
        q.appendleft([i+1,j+1,2])
        return True
    return False 
def for_index(i:int, j:int) -> bool: # 함수 인덱스 맞추기 위해서
    return False
N = int(input())
matrix = [list(map(int,input().split()))for _ in range(N)]
func = {0:[width,for_index,diagonal], 1:[for_index,length,diagonal], 2:[width,length,diagonal]}
cnt = 0
q = collections.deque([[0,1,0]])
while q:
    for _ in range(len(q)):
        i,j,k = q.pop()
        if i == j == N-1:
            cnt += 1
            continue
        for fun in func[k]:
            fun(i,j)
print(cnt)




