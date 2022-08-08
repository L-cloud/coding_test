from collections import deque
N = int(input())
dp,cnt = [True] * (N+1),0
for i in range(2,N // 2):
    num = 2
    if dp[i]:
        while i * num < N +1:
            dp[i*num] = False
            num += 1
decimals = [index for index, value in enumerate(dp) if value and 1 < index ]
# 연속합... 
q = deque()
for decimal in decimals:
    q.append(decimal)
    while N < sum(q):
        q.popleft()
    if sum(q) == N:
        cnt += 1
print(cnt) 
