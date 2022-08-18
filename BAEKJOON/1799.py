import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
black, white  = 0,0
dp = [-1 for _ in range(2*N-1)]
chess = [(0,i) if i < N else (i -N + 1,N-1) for i in range(2*N - 1)] #각 노드별 시작점
def func(n:int, size :int,is_black:bool) -> None:
    if 2*N - 2 < n:
        if is_black:
            global black
            black = max(black, size)
        else:
            global white
            white = max(white,size)
        return
    x,y = chess[n][0], chess[n][1]
    cnt = 0
    while 0<=x < N and 0<=y <N:
        if matrix[x][y]: # 말 놓은 수 있음
            if is_black:
                for i in range(0,n,2):
                    if -1 < dp[i]: 
                        if abs(x - (chess[i][0] + dp[i])) == abs(y - (chess[i][1] - dp[i])):  
                            break
                else:
                    dp[n] = cnt
                    func(n+2,size+1,is_black)
                
            else:
                for i in range(1,n,2):
                    if -1 < dp[i]: 
                        if abs(x - (chess[i][0] + dp[i])) == abs(y - (chess[i][1] - dp[i])):   
                            break
                else:
                    dp[n] = cnt
                    func(n+2,size+1,is_black)
        x += 1
        y -= 1
        cnt += 1
    if is_black:
        dp[n] = -1
        func(n+2,size,is_black)
    else:
        dp[n] = -1
        func(n+2,size,is_black)
func(0,0,True)
func(1,0,False)
print(white+black)
