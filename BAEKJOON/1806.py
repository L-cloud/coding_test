import sys, collections
input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int,input().split()))
sum_num, q = 0, collections.deque()
cnt = float('inf')
for num in nums:
    sum_num += num
    q.append(num)
    if sum_num < S:
        continue
    while q and S <= sum_num :
        cnt = min(cnt, len(q))
        sum_num -= q.popleft()
print(cnt if cnt < float('inf') else 0)
