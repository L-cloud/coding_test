w1,w2,w3 = input().rstrip(),input().rstrip(),input().rstrip()
dp = [[[0 for _ in range(len(w3) + 1)]for _ in range(len(w2) + 1)]for _ in range(len(w1) +1)]
for i in range(1,len(w1) + 1):
    for j in range(1,len(w2) + 1):
        for k in range(1,len(w3) + 1):
            if w1[i-1] == w2[j-1] == w3[k-1]:
                dp[i][j][k] = max(dp[i][j][k -1], dp[i-1][j-1][k-1] + 1)
            else:
                dp[i][j][k] = max(dp[i][j][k-1], dp[i-1][j][k],dp[i][j-1][k])
print(dp[-1][-1][-1])