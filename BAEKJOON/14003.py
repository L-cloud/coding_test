import collections
from linecache import cache
import sys,bisect
from collections import deque,defaultdict
input = sys.stdin.readline
N,nums = int(input()),list(map(int,input().split()))
dp,cache,index_dp = [], defaultdict(deque),[]
for i in range(N):
    index = bisect.bisect_left(dp, nums[i])
    if len(dp) - 1 < index:
        dp.append(nums[i])
        index_dp.append(i)
    else:
        dp[index] = nums[i]
        index_dp[index] = i
    cache[index].append([nums[i],i])
for i in range(len(dp)-2,-1,-1):
    while index_dp[i+1] < index_dp[i] : # 뒤 인덱스가 더 큼
        num,index = cache[i].pop()
        dp[i],index_dp[i] = num,index

print(len(dp))
print(*dp)