import math
N = int(input())
dp = [4 for _ in range(N+1)]
dp[0] = 0
sqr = 1
for i in range(1,N+1):
    for j in range(int(math.sqrt(i)),0,-1):
        dp[i] = min(1 + dp[i-j**2],dp[i])
print(dp[-1])
