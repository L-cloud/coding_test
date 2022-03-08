import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    stack.append(int(sys.stdin.readline()))
max_num = max(stack)
dp = [True] * (max_num + 1)
decimal_index = []

## check decimal
for i in range(2, max_num + 1):
    index = 2
    while i * index <= max_num:
        dp[i * index] = False
        index += 1
# store decimal
for i in range(2, max_num + 1):
    if dp[i]:
        decimal_index.append(i)
for num in stack:
    gold = 0
    tempt = set()
    for index in decimal_index:
        if num <= index + 1:
            break
        if dp[num - index] and index not in tempt:
            gold += 1
            tempt.add(num - index)
            tempt.add(index)
    print(gold) 

