
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
class Node:
    def __init__(self, node:int) -> None:
        self.node = node
        self.left = None
        self.right = None
def dfs (left, i_start, i_end, p_start): # 어짜피 범위는 같음
    if i_end < i_start:
        return
    while i_start <= i_end:
        i, p = in_order[i_start], post_order[p_start]
        while i == p:
            parent = Node(i)
            parent.left = left
            left = parent
            if i_start + 1 <= i_end:
                i_start += 1
                p_start += 1
                i,p = in_order[i_start], post_order[p_start]
            else:
                return parent
        parent = Node(i)
        parent.left = left
        left = parent
        tempt = post_index[i] # 여기가 문제인가 최악
        parent.right = dfs(None,i_start=i_start + 1, i_end= tempt - p_start + i_start,p_start=p_start)
        i_start = tempt - p_start + i_start + 1
        p_start = tempt + 1
    return parent
  
N = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int, input().split()))
post_index = {v:i for i,v in enumerate(post_order)}
def pre_order(node,order):
    if not node:
        return
    order.append(node.node)
    pre_order(node.left,order)
    pre_order(node.right,order)
node = dfs(None,0,N-1,0)
order = []
pre_order(node,order)
print(*order)