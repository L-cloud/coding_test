import sys

n = int(sys.stdin.readline())

dp =[0,1,1]

for i in range(2,n+1):
    dp[2] = (dp[0] + dp[1]) % 1000000
    dp[0] = dp[1]
    dp[1] = dp[2]
print(dp[2])