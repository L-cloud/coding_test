import sys

num_list = []
for _ in range(int(sys.stdin.readline())):
    num_list.append(int(sys.stdin.readline()))

max_num = max(num_list)
dp = [0] * (max_num + 1)
dp[1],dp[2],dp[3] = 1,2,4

for n in range(4,max_num + 1):
    dp[n] = (dp[n-3] + dp[n -2] + dp[n - 1]) % 1000000009

for i in num_list:
    print(dp[i])