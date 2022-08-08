import sys
from typing import List
input = sys.stdin.readline
def solution() ->List[int] :
    min_v = [INF] * 3
    for i in range(N-2):
        left,right  = i + 1, N -1
        while left < right:
            s = [nums[i] , nums[left] , nums[right]]
            if abs(sum(s)) < abs(sum(min_v)):
                min_v = s
            if  0 < sum(s):
                right -= 1
            elif sum(s) < 0:
                left += 1
            else:
                return min_v
    return min_v 


if __name__ == '__main__':
    N = int(input())
    INF = 1000000001
    nums = list(map(int, input().split()))
    nums.sort()
    print(*solution())

