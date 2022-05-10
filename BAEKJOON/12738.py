import sys,bisect

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [num[0]]
for i in num:
    if dp[-1] <  i:
        dp.append(i)
    else:
        index = bisect.bisect_left(dp,i)
        dp[index] = i # 교체
print(len(dp))