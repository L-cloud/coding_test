import sys
from typing import List
input = sys.stdin.readline
N = int(input())
m = list(map(int,input().split()))
ans = [0]
def divide(m:List[int]) -> List[int]:
    if len(m) == 1:
        return m
    l = divide(m[:len(m) // 2])
    r = divide(m[len(m)//2:])
    return conquer(l,r)
def conquer(l:List[int], r:List[int]) -> List[int]:
    t = []
    left, right = 0,0
    while left < len(l) and right < len(r):
        if l[left] <= r[right]:
            t.append(l[left])
            left += 1
        else: # 오른쪽이 더 작음
            t.append(r[right])
            right += 1
            ans[0] += (len(l) - left)
    if left != len(l) : # left가 남음
        t += l[left:]
    else:
        t += r[right:]
    return t
divide(m)
print(ans[0])
