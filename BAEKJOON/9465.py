import sys

N = int(sys.stdin.readline())
answer = []
# 이전꺼 위 선택하면 다음꺼는 아래 선택하거나 안 하거나임
for _ in range(N):
    col = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0 for _ in range(col)] for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
    for i in range(1, col):
        if i < 2: # 
            dp[0][1],dp[1][1] = dp[1][0] + sticker[0][1], dp[0][0] + sticker[1][1]
        else: 
            dp[0][i] = max(dp[1][i -1], dp[1][i-2],dp[0][i-2]) + sticker[0][i] # 바로 전꺼 선택, 전꺼 안 뜯고 전전꺼 선택
            dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + sticker[1][i] # 위랑 동일
    answer.append(max(dp[-1][0], dp[-1][1]))
for a in answer:
    print(a)


    