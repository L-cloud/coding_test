import sys
# DP 같은데
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

dp = [0 for _ in range(len(A + 1))]
for v1 in B:
    cnt = 0
    for i2,v2 in enumerate(A):
        if cnt < dp[i2]:
            cnt = dp[i2]
        elif v1 == v2 :
            dp[i2] = cnt + 1
print(max(dp))

# dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

# for i1,v1 in enumerate(A, 1):
#     for i2,v2 in enumerate(B, 1):
#         if v1 == v2: # 둘이 같은 경우
#             dp[i1][i2] =  dp[i1 - 1][i2 -1] + 1
#         else:
#             dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2 -1])
# print(dp[-1][-1])



