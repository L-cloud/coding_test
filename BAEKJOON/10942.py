import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [[1 if i == j  else 0 for j in range(N)]for i in range(N)]

for i in range(N-1):
    if nums[i] == nums[i+1]:
        dp[i][i + 1] = 1
for i in range(2, N):
    for j in range(N-i):
        if nums[j] == nums[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][j+i] = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])