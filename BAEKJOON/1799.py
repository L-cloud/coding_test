import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
size_  = 0
dp = [-1 for _ in range(2*N-1)]
chess = [(0,i) if i < N else (i -N + 1,N-1) for i in range(2*N - 1)] #각 노드별 시작점
def func(start:int,n:int, size :int) -> None:
    if 2*N - 2 < n:
        global size_
        size_ = max(size_,size)
        return
    x,y = chess[n][0], chess[n][1]
    cnt = 0
    while 0<=x < N and 0<=y <N:
        if matrix[x][y]: # 말 놓은 수 있음
            for i in range(start,n,2):
                if -1 < dp[i]: 
                    if abs(x - (chess[i][0] + dp[i])) == abs(y - (chess[i][1] - dp[i])):  
                        break
            else:
                dp[n] = cnt
                func(start,n+2,size+1)
                
        x += 1
        y -= 1
        cnt += 1
    dp[n] = -1
    func(start,n+2,size)
func(0,0,0)
size_1 = size_
size_ = 0
func(1,1,0)
print(size_1 + size_)
