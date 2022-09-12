import sys
input = sys.stdin.readline
N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]
dp = [[float('inf')]*N for _ in range(N)]
def divide(start:int, end:int) ->int:
    if dp[start][end] != float('inf'):
        return dp[start][end]
    if start == end:
        dp[start][end] = 0
        return 0
    elif end - start == 1: 
        dp[start][end] = nums[start][0] * nums[start][1] * nums[end][1]
        return dp[start][end]
    for i in range(end-start):
        left = divide(start,start +i)
        right = divide(start + i +1, end)
        dp[start][end] = min(dp[start][end], left + right + nums[start][0] * nums[start + i +1][0] * nums[end][1]) 
    return dp[start][end]
print(divide(0,N-1))
`
