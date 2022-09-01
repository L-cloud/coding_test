import sys,bisect
input = sys.stdin.readline
N = int(input())
num1, num2 = list(map(int, input().split())),list(map(int,input().split()))
dic,dp = {num2[i] : i for i in range(N)},[]
for num in num1:
    index = bisect.bisect_left(dp,dic[num])
    if len(dp) -1 < index:
        dp.append(dic[num])
    else:
        dp[index] = dic[num]
print(len(dp))
