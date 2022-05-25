import sys
N = int(sys.stdin.readline())
consulting = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]
print(consulting)
def dfs(index, chance, profit):
    if index == len(consulting) -1:
        if not chance and consulting[-1][0] == 1:
            profit += consulting[-1][1]
        return profit
    max_profit = 0
    if chance <= 0 : # chance == 0
        if index + consulting[index][0] -1 < len(consulting):
            max_profit = max(max_profit, dfs(index +1, consulting[index][0] -1, profit + consulting[index][1])) # 선택함
        max_profit = max(max_profit,dfs(index + 1, chance -1 , profit)) # 선택 안 함
    else:
        max_profit = max(max_profit,dfs(index +1, chance-1,profit))
    return max_profit
print(dfs(0,0,0))