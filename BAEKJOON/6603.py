import sys
from typing import List
def dfs(num_list : List[int], stack : List[int], n:int) -> None:
    if len(stack) == n: # 해당됨
        print(" ".join(map(str,stack)))
        return
    if len(stack) + len(num_list) < n: # 길이 부족 더 할 필요 없음
        return
    for i,v in enumerate(num_list):
        stack.append(v)
        dfs(num_list[i+1:], stack, n)
        stack.pop()
while True:
    num_list = list(map(int, sys.stdin.readline().split()))
    if num_list == [0]:
        exit()
    n, r = num_list[0], num_list[1:]
    dfs(r,[],6)