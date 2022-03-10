import sys


num = int(sys.stdin.readline())
dp = [0] * (num + 1)
if num < 2:
    print(num)
    exit()
dp[1] = 1
dp[2] = 3

for i in range(3, num + 1):
    dp[i] = (dp[i -2] * 2 + dp[i - 1]) % 10007
print(dp[-1])