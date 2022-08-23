import sys
input = sys.stdin.readline

N = int(input())
stair = [int(input()) for _ in range(N)]
dp = [[stair[i], stair[i]] for i in range(N)]
for i in range(N -1):
    dp[i + 1][0] += dp[i][1] 
    if i + 2 < N:
        dp[i + 2][1] += max(dp[i]) 
print(max(dp[-1]))
