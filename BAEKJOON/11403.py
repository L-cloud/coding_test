import sys,collections
input = sys.stdin.readline
N = int(input())
dp = collections.defaultdict(set)
for i in range(N):
    dp[i] = set([i for i,v in enumerate(map(int,input().split())) if v])
for i in range(N):
    tempt = set(dp[i]) # new object
    while tempt:
        node = tempt.pop()
        for n in dp[node]:
            if n not in dp[i]:
                dp[i].add(n)
                tempt.add(n)
dp = (list(['1' if j in dp[i] else '0' for j in range(N)] for i in range(N)))
for i in range(N):
    print(*dp[i])

