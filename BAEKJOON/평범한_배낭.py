import sys

thing_num, bag_weight = map(int, sys.stdin.readline().split())
weight_value_list = []
for _ in range(thing_num):
    weight_value_list.append(list(map(int,sys.stdin.readline().split())))

# 이거 순서는 상관 없는가?
dp = [[0 for _ in range(bag_weight + 1)] for _ in range(thing_num)]
for i in range(len(dp)):
    for j in range(len(dp[0])):
        if  j < weight_value_list[i][0]:
             dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], weight_value_list[i][1] + dp[i - 1][j - weight_value_list[i][0]])
print(dp[-1][-1])