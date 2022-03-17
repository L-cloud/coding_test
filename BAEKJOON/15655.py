import sys

def dfs(start:int)->None:
    if len(tempt) == b:
        print(*tempt)
        return
    for i,v in enumerate(num_list[start:], start):
        tempt.append(v)
        dfs(i+1)
        tempt.pop()

a, b = map(int,sys.stdin.readline().split())

num_list = sorted(list(map(int, sys.stdin.readline().split())))
tempt = []

dfs(0)
