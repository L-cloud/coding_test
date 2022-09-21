
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
nums = [int(input()) for _ in range(N)]
dp = [0] * N * 4
def make_segment(idx:int,left:int, right:int) -> None:
    if left == right:
        dp[idx] = nums[left]
        return dp[idx]
    left_ = make_segment(idx*2,left, (left+right)// 2)
    right_ = make_segment(idx*2 +1 ,(left + right) // 2 + 1 ,right)
    dp[idx] = left_ + right_
    return dp[idx]

# start, end = 구간 합, left, right = 구하려고 하는 거
def section_sum(idx:int,start:int,end:int,left:int,right:int) -> int:
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return dp[idx]
    return section_sum(idx*2, start, (end+start)// 2, left, right) + section_sum(idx*2+1,(start + end) // 2 + 1, end,left, right)

def change_condition(idx:int, start:int, end:int, index:int, value:int) -> None:
    if start <= index <= end:
        dp[idx]+= value
        if start != end:
            change_condition(idx*2, start, (start+end)// 2, index, value)
            change_condition(idx*2+1, (start+end)//2 + 1, end, index, value)

make_segment(1,0,len(nums)-1)

for _ in range(K+M):
    a, b, c = map(int, input().split())
    if a == 1:
        value = c - nums[b-1]
        nums[b-1] = c
        change_condition(1,0,len(nums)-1,b-1,value)
    else:
        print(section_sum(1,0,len(nums)-1, b-1,c-1))

