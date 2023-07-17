import sys
from collections import Counter
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x: int) -> int:
    if x != friends[x]:
        friends[x] = find(friends[x])
    return friends[x]


def union(x1: int, x2: int) -> None:
    x1 = find(x1)
    x2 = find(x2)
    if x1 < x2:
        friends[x2] = x1
    else:
        friends[x1] = x2

N,M,K = map(int,input().split())

friends = [i for i in range(N+1)]
candies = [0] + list(map(int,input().split()))
values, ans = Counter(), [0]
for _ in range(M):
    a,b = map(int,input().split())
    union(a,b)
for i in range(N+1):
    values[friends[find(i)]] += candies[i]
cnt = Counter(friends)
del cnt[0]
dp = [[0] * K for _ in range(len(cnt)+1)]

for i,key in enumerate(cnt,1): # friends key
    n, v = cnt[key], values[key] # 사람 수, value임
    for j in range(1,n):
        if K <= j:
            break
        dp[i][j] = dp[i-1][j]
    for j in range(n,K):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-n]+v)
print(dp[-1][-1])


