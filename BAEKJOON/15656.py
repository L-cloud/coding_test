import sys

def dfs():
    if len(tempt) == b:
        print(*tempt)
        return
    for i in num_list:
        tempt.append(i)
        dfs()
        tempt.pop()

a, b = map(int, sys.stdin.readline().split())

num_list = sorted(list(map(int, sys.stdin.readline().split())))
tempt = []
dfs()
