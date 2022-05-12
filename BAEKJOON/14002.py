import sys,collections

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [[num[i]] for i in range(N)]
for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            if len(dp[i]) <= len(dp[j]):
                dp[i] = dp[j][:]
                dp[i].append(num[i])
dp.sort(key = lambda x: len(x))
print(len(dp[-1]))
print(*dp[-1])

# 반례 10 20 1 30
# 1 20 30 이 출력됨
