import sys
from typing import Callable, List
input = sys.stdin.readline
N,M= map(int,input().split())
nums = [int(input()) for _ in range(N)]
max_sagment,min_sagment = [0]* 4 * N, [0] * 4 * N
def make_sagment(dp:List[int],idx:int, left:int, right:int,func:Callable)->int:
    if left == right:
        dp[idx] = nums[left]
        return dp[idx]
    left_ = make_sagment(dp,idx*2, left,(left+right)//2, func)
    right_ = make_sagment(dp,idx*2+1,(left+right)//2 + 1,right, func)
    dp[idx] = func(left_,right_)
    return dp[idx]
def find_num(sag:List[int],idx:int,start:int,end:int,left:int,right:int, func:Callable) ->int:
    if right < start or end < left:
        return None
    if left <= start and  end <= right:
        return sag[idx]
    left_ = find_num(sag,idx*2,start,(start+end)//2,left,right,func)
    right_ = find_num(sag,idx*2+1,(start+end)//2+1, end,left, right, func)
    if left_ != None and right_ != None:
        return func(left_,right_)
    return left_ if left_ else right_

make_sagment(max_sagment,1,0,N-1,max)
make_sagment(min_sagment,1,0,N-1,min)
for _ in range(M):
    a,b = map(int,input().split())
    print(find_num(min_sagment,1,0,N-1,a-1,b-1,min), find_num(max_sagment,1,0,N-1,a-1,b-1,max))

