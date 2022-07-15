import sys
input = sys.stdin.readline
def width(i:int, j:int) -> None: #가로
    if 0< j+1 < N and not matrix[i][j+1]:
        prev = sum(dp[i][j]) -dp[i][j][1] if sum(dp[i][j]) - dp[i][j][1] else 1
        dp[i][j+1][0] += prev 
def length(i:int, j:int) -> None: # 세로
    if 0<= i +1 < N and not matrix[i + 1][j]:
        prev = sum(dp[i][j]) - dp[i][j][0] if sum(dp[i][j]) -dp[i][j][0] else 1
        dp[i+1][j][1] += prev  
def diagonal(i:int, j:int) -> None: # 대각선
    if 0< i+1 < N and 0 < j+1 < N and not matrix[i][j+1] and not matrix[i+1][j] and not matrix[i+1][j+1]:
        prev = sum(dp[i][j]) if sum(dp[i][j])  else 1
        dp[i+1][j+1][2] += prev  
N = int(input())
matrix = [list(map(int,input().split()))for _ in range(N)]
dp = [[[0,0,0] for _ in range(N)]for _ in range(N)]
func = [width,length,diagonal]
dp[0][1][0] = 1 # dp초기화
for i in range(N):
    for j in range(N):
        for k in range(3):
            if k!= 2 and (dp[i][j][k] or dp[i][j][2]): # 가로라면 가로만, 세로라면 세로만 혹은 대각으로 들어옴
                func[k](i,j)
            elif k == 2 and sum(dp[i][j]): # 어느 방향으로든 들어오기는 함
                func[k](i,j)
print(sum(dp[-1][-1]))