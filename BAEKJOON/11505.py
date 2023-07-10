import sys
from typing import List


def make_seg(m: List[int]) -> List[int]:
    tree = [1] * (len(m) * 4)
    make_tree(m, tree, 1, 0, len(m) - 1)
    return tree

def make_tree(m: List[int], tree: List[int], index: int, left: int, right: int) -> int:
    if right == left:
        tree[index] = m[right]
        return tree[index]
    l = make_tree(m, tree, index * 2, left, (left + right) // 2)
    r = make_tree(m, tree, index * 2 + 1, (left + right) // 2+ 1, right)
    tree[index] = (l * r) % 1000000007
    return tree[index]

def call(index:int,f_l:int,f_r:int,left:int,right:int) -> int:
    if left == f_l and right == f_r:
        return seg[index]
    if right < f_l or f_r < left:
        return 1
    if f_l <= left and right <= f_r:
        return seg[index]
    l = call(index*2,f_l,f_r,left,(left + right) // 2)
    r = call(index*2 + 1, f_l,f_r,(left + right)//2 + 1, right)
    return (l*r) % 1000000007

def change(m_index:int,index:int,c:int,left:int,right:int) -> None:
    if left == right == m_index:
        seg[index] = c
        return
    if left <= m_index and m_index <= right:
        change(m_index,index*2,c,left,(left + right) // 2)
        change(m_index,index*2 + 1,c, (left+right)//2 +1, right)
        seg[index] = (seg[index*2] * seg[index*2 + 1]) % 1000000007


input = sys.stdin.readline
N,M,K = map(int,input().split())
matrix = [int(input()) for _ in range(N)]
seg = make_seg(matrix)
for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        if matrix[b-1] == 0 or b == 0:
            matrix[b - 1] = c
            seg = make_seg(matrix)
        else:
            change(b-1,1,c,0,len(matrix) -1)
            matrix[b-1] = c
    else:
        print(int(call(1,b-1,c-1,0,len(matrix) - 1)))
