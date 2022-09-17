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

# ver2

import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
for i in range(1,N): # 간격
    for j in range(N-i): # 시작 노드
        min_value = 2**31
        for k in range(j,j+i): # 시작~간격 계산
            min_value = min(dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k+1][0] * matrix[j+i][1], min_value)
        dp[j][j+i] = min_value
print(dp[0][-1])

