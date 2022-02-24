import collections
import sys

thing_num, bag_weight = map(int, sys.stdin.readline().split())
weight_value_list = []
for _ in range(thing_num):
    weight_value_list.append(list(map(int,sys.stdin.readline().split())))

weight_value_list.sort()
picked_list = collections.defaultdict(set)
dp = [[0 for _ in range(bag_weight + 1)] for _ in range(thing_num + 1)]
for i in range(len(dp)):
    for j in range(len(dp[0])):
        pick_w, pick_v = 0, 0
        if i == 0 or j == 0:
            continue
        for weight, value in weight_value_list:
            if j < weight: # 무게 낮은 순으로 정렬해놔서 더 높으면 볼 필요x
                break
            if dp[i][j] < value + dp[i - 1][j - weight] and (pick_w,pick_v) not in picked_list[j]:
                dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j]) # 둘 중 하나 선택해야 하니까
                if dp[i][j] == value + dp[i - 1][j - weight]: # 현재꺼 선택해서 바꿈
                    pick_w, pick_v = weight, value
        if pick_w: # 어떤 녀석이 선택 된거임
            picked_list[j].add((pick_w,pick_v))
print(dp[-1][-1])