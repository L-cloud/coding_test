import sys

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(int(sys.stdin.readline())):
  num = int(sys.stdin.readline())
  if dp[num]:
    print(dp[num])
    continue
  for i in range(4,num + 1):
    dp[i] = dp[i -3] +dp[i -2] + dp[i - 1]
  print(dp[num])