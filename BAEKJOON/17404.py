from typing import List
import sys
input = sys.stdin.readline
def check(dp:List[List[int]],index:int) -> int:
    for i in range(1,len(dp)): 
        if i == 1:
            dp[i][index] = float('inf') # 선택 못 하게
            dp[i][(index+1)%3] += dp[0][0] # 다 동일
            dp[i][(index+2)%3] += dp[0][0]
        elif i == len(dp) - 1:
            dp[i][(index+1)%3] += min(dp[i-1][(index+2)%3],dp[i-1][index]) 
            dp[i][(index+2)%3] += min(dp[i-1][index],dp[i-1][(index+1)%3])
        else:
            dp[i][0] += min(dp[i-1][1],dp[i-1][2])
            dp[i][1] += min(dp[i-1][0],dp[i-1][2])
            dp[i][2] += min(dp[i-1][0],dp[i-1][1])
    return min(dp[-1])

N = int(input())
dp = [list(map(int,input().split())) for _ in range(N)]
dp1 = [dp[i][:] if i != 0 else [dp[0][0]] * 3 for i in range(N)]
dp2 = [dp[i][:] if i != 0 else [dp[0][1]] * 3 for i in range(N)]
dp3 = [dp[i][:] if i != 0 else [dp[0][2]] * 3 for i in range(N)]
dp1[-1][0],dp2[-1][1],dp3[-1][2] = float('inf'),float('inf'),float('inf')
print (min(check(dp1,0),check(dp2,1),check(dp3,2)))

