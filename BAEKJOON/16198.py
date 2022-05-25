import sys
N = int(sys.stdin.readline())
marble = list(map(int, sys.stdin.readline().split()))
def dfs(marbel, value):
    if len(marbel) == 2:
        return value
    max_val = 0
    for i in range(1,len(marbel) - 1):
        v = dfs(marbel[:i] + marbel[i + 1 :], value + marbel[i-1] * marbel[i + 1])
        max_val = max(max_val,v)
    return max_val

print(dfs(marble,0))