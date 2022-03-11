import sys
card_num = int(sys.stdin.readline())

p_list = list(map(int, sys.stdin.readline().split()))
money = [[0 for _ in range(card_num + 1)] for _ in range(card_num + 1)]

for num1 in range(1, card_num + 1):
    for num2 in range(1, card_num + 1):
        if num2 < num1:
            money[num1][num2] = money[num1 - 1][num2]
            continue
        money[num1][num2] = max(money[num1-1][num2 - num1] + p_list[num1 -1], money[num1][num2 -num1] + p_list[num1 - 1],money[num1 - 1][num2])
print(money[-1][-1])
