import sys

N = int(sys.stdin.readline())
dp = [[1 for _ in range(10)]for _ in range(N + 1)]
# if N > 1:
#     for i in range(10):
#         dp[2][i] = 10 -i

for k in range(2,N + 1):
    for n in range(10):
        if n > 0:
            dp[k][n] = dp[k][n-1] - dp[k-1][n-1]
        else:
            dp[k][n] = (sum(dp[k-1]))

print(sum(dp[N])%10007) 