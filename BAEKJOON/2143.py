import sys,collections
from typing import List
input = sys.stdin.readline

def check(nums : List[int]) -> collections.Counter:
    t = collections.Counter()
    for i in range(len(nums)):
        s = nums[i]
        t[s] += 1
        for j in range(i+1, len(nums)):
            s += nums[j]
            t[s] += 1
    return t
T = int(input())
len_a = int(input())
A = list(map(int,(input().split())))
len_b = int(input())
B = list(map(int,input().split()))
v_a,v_b = 1 << len_a - 1, 1 << len_b - 1
p_a, p_b = check(A), check(B)
cnt = 0
for key in p_a:
    if T- key in p_b:
        cnt += (p_a[key] * p_b[T-key])
print(cnt)
