import sys
input = sys.stdin.readline
N,K = map(int,input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1,N+1):
    w,v = map(int,input().split())
    if w <= K:
        for j in range(1,w):
            dp[i][j] = dp[i-1][j]
        dp[i][w] = max(dp[i-1][w], v)
        for j in range(w+1,K+1):
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j], dp[i][j-1])
    else:
        dp[i] = [dp[i-1][j] for j in range(K+1)]
print(dp[-1][-1])
