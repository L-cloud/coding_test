import sys,itertools
input = sys.stdin.readline
N,M = map(int, input().split())
nums = list(itertools.accumulate(map(int, input().split()),initial = 0))
for _ in range(M):
    a, b = map(int, input().split())
    print(nums[b] - nums[a-1])

