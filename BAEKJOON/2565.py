import sys
from bisect import bisect_left
input = sys.stdin.readline
nums, dp= {},{}
for _ in range(int(input())):
    value, key = map(int,input().split())
    nums[key] = value
    dp[value] = 0
l = [-1]
for key in sorted(nums.keys()):
    if l[-1] < nums[key]:
        l.append(nums[key])
        dp[nums[key]] = len(l) - 1
    else:
        dp[nums[key]] = bisect_left(l,nums[key])
        l[dp[nums[key]]] = nums[key]
print(len(nums) - max(dp.values()))
