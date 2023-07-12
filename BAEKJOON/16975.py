from typing import List
import sys
def make_seg(m:List[int]) -> List[int]:
    output = [0] * len(m) * 4
    dfs(output,1,0,len(user_input) - 1)
    return output

def dfs(m:List[int], index:int, left:int,right:int) -> int:
    if left == right:
        m[index] = user_input[left]
        return m[index]
    l = dfs(m,index*2, left,(left + right) // 2)
    r = dfs(m,index*2+1, (left + right) // 2 + 1, right)
    m[index] = l + r
    return m[index]

def update(index:int, left:int, right:int, target_left:int, target_right:int, value:int) -> int:
    if  target_right < left or right < target_left:
        return seg[index]
    if left == right:
        seg[index] += value
        return seg[index]
    if target_left <= left and right <= target_right: # 완전히 포함
        lazy[index] += value
        seg[index] += (right - left + 1) * value
        return seg[index]
    if lazy[index]:
        push_down(left, (left + right) // 2, index, index*2)
        push_down((left + right)// 2 + 1, right, index, index*2 + 1)
        lazy[index] = 0
    l = update(index*2,left, (left + right) // 2 ,target_left,target_right,value)
    r  = update(index*2 + 1,(left + right) // 2 + 1,  right,target_left,target_right,value)
    seg[index] = l + r
    return seg[index]

def push_down(left:int, right:int, lazy_index:int, seg_index:int) -> None:
    if left != right: # leaf가 아님
        lazy[seg_index] += lazy[lazy_index]
    seg[seg_index] += (right - left + 1) * lazy[lazy_index]

def query(target:int) -> int:
    update(1,0,N-1,target,target,0) # 그냥 업데이트 때림
    t = find(1, 0, N - 1, target)
    return seg[t]

def find(index:int,left:int, right:int,target:int) -> int:
    if target < left or right < target:
        return 0
    if left == right == target:
        return index
    l = find(index*2,left, (left + right) // 2, target)
    r = find(index*2 + 1, (left + right) // 2 + 1, right, target)
    return max(l,r)
input = sys.stdin.readline
N = int(input())
user_input = list(map(int,input().split()))
seg = make_seg(user_input)
lazy = [0] * len(seg)
for _ in range(int(input())):
    cmd,*l = map(int,input().split())
    if cmd == 1:
        update(1,0,N-1,l[0] -1,l[1]-1,l[2])
    else: print(query(l[0] -1))
